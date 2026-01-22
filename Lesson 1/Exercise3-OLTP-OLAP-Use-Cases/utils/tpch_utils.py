"""
TPC-H specific utilities for OLAP benchmarking
This module provides functions for TPC-H data transfer and query execution.
"""

import pandas as pd
import sys
import time
import io
from .db_utils import map_duckdb_to_postgres_type, ensure_tpch_schema


# TPC-H tables in an order that respects foreign key constraints
TPCH_TABLES = [
    'region',
    'nation',
    'part',
    'supplier',
    'partsupp',
    'customer',
    'orders',
    'lineitem'
]


def transfer_table(table_name, duck_conn, pg_conn):
    """
    Transfers a single table from DuckDB to PostgreSQL (into 'tpch' schema).
    
    Args:
        table_name: Name of the table to transfer
        duck_conn: DuckDB connection object
        pg_conn: PostgreSQL connection object
    """
    print(f"\n--- Processing table: {table_name} ---")
    
    try:
        # 1. Extract from DuckDB
        print(f"  Extracting '{table_name}' from DuckDB...")
        start_time = time.time()
        query = f"SELECT * FROM {table_name}"
        df = duck_conn.query(query).df()
        extract_time = time.time() - start_time
        print(f"  Extracted {len(df)} rows in {extract_time:.2f} seconds.")

        if df.empty:
            print(f"  Skipping load for '{table_name}' as it contains no data.")
            return

        # 2. Get schema from DuckDB and create DDL
        print(f"  Generating schema for '{table_name}'...")
        schema_df = duck_conn.query(f"DESCRIBE SELECT * FROM {table_name}").df()
        columns_sql = []
        for _, row in schema_df.iterrows():
            col_name = row['column_name']
            pg_type = map_duckdb_to_postgres_type(row['column_type'])
            columns_sql.append(f'"{col_name}" {pg_type}')
        
        create_table_sql = f"CREATE TABLE tpch.{table_name} ({', '.join(columns_sql)});"

        # 3. Load into PostgreSQL using psycopg2.copy_expert
        print(f"  Loading '{table_name}' into PostgreSQL schema 'tpch' using COPY...")
        start_time = time.time()
        
        buffer = io.StringIO()
        df.to_csv(buffer, index=False, header=False, sep='\t', na_rep='\\N')
        buffer.seek(0)
        
        with pg_conn.cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS tpch.{table_name} CASCADE;")
            cursor.execute(create_table_sql)
            
            copy_sql = f"COPY tpch.{table_name} FROM STDIN WITH (FORMAT CSV, DELIMITER E'\\t', NULL '\\N')"
            cursor.copy_expert(copy_sql, buffer)
            
        pg_conn.commit()
        
        load_time = time.time() - start_time
        print(f"  Successfully loaded '{table_name}' into 'tpch' in {load_time:.2f} seconds.")

    except Exception as e:
        print(f"Error processing table '{table_name}': {e}")
        try:
            pg_conn.rollback()
        except Exception as rb_e:
            print(f"  Error during rollback: {rb_e}")
        print("Stopping script.")
        sys.exit(1)


def transfer_all_tables(duck_conn, pg_conn):
    """
    Transfers all TPC-H tables from DuckDB to PostgreSQL.
    
    Args:
        duck_conn: DuckDB connection object
        pg_conn: PostgreSQL connection object
        
    Returns:
        Total time taken for the transfer
    """
    print("Starting TPC-H data transfer from DuckDB to PostgreSQL (schema 'tpch')...")
    
    # Ensure the tpch schema exists
    ensure_tpch_schema(pg_conn)
    
    script_start_time = time.time()
    
    try:
        with duck_conn:
            for table in TPCH_TABLES:
                transfer_table(table, duck_conn, pg_conn)
    finally:
        if pg_conn:
            pg_conn.close()
            print("\nPostgreSQL connection closed.")
            
    script_end_time = time.time()
    total_time = script_end_time - script_start_time
    
    print(f"\n--- Transfer Complete ---")
    print(f"All {len(TPCH_TABLES)} tables transferred successfully to schema 'tpch'.")
    print(f"Total time: {total_time:.2f} seconds.")
    
    return total_time


# TPC-H Query String (all 22 queries minus query 22 which is shown separately)
TPCH_QUERY_STRING = """
SELECT
    l_returnflag,
    l_linestatus,
    sum(l_quantity) AS sum_qty,
    sum(l_extendedprice) AS sum_base_price,
    sum(l_extendedprice * (1 - l_discount)) AS sum_disc_price,
    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) AS sum_charge,
    avg(l_quantity) AS avg_qty,
    avg(l_extendedprice) AS avg_price,
    avg(l_discount) AS avg_disc,
    count(*) AS count_order
FROM
    tpch.lineitem
WHERE
    l_shipdate <= CAST('1998-09-02' AS date)
GROUP BY
    l_returnflag,
    l_linestatus
ORDER BY
    l_returnflag,
    l_linestatus;

SELECT
    s_acctbal,
    s_name,
    n_name,
    p_partkey,
    p_mfgr,
    s_address,
    s_phone,
    s_comment
FROM
    tpch.part,
    tpch.supplier,
    tpch.partsupp,
    tpch.nation,
    tpch.region
WHERE
    p_partkey = ps_partkey
    AND s_suppkey = ps_suppkey
    AND p_size = 15
    AND p_type LIKE '%BRASS'
    AND s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND r_name = 'EUROPE'
    AND ps_supplycost = (
        SELECT
            min(ps_supplycost)
        FROM
            tpch.partsupp,
            tpch.supplier,
            tpch.nation,
            tpch.region
        WHERE
            p_partkey = ps_partkey
            AND s_suppkey = ps_suppkey
            AND s_nationkey = n_nationkey
            AND n_regionkey = r_regionkey
            AND r_name = 'EUROPE')
ORDER BY
    s_acctbal DESC,
    n_name,
    s_name,
    p_partkey
LIMIT 100;

SELECT
    l_orderkey,
    sum(l_extendedprice * (1 - l_discount)) AS revenue,
    o_orderdate,
    o_shippriority
FROM
    tpch.customer,
    tpch.orders,
    tpch.lineitem
WHERE
    c_mktsegment = 'BUILDING'
    AND c_custkey = o_custkey
    AND l_orderkey = o_orderkey
    AND o_orderdate < CAST('1995-03-15' AS date)
    AND l_shipdate > CAST('1995-03-15' AS date)
GROUP BY
    l_orderkey,
    o_orderdate,
    o_shippriority
ORDER BY
    revenue DESC,
    o_orderdate
LIMIT 10;

SELECT
    o_orderpriority,
    count(*) AS order_count
FROM
    tpch.orders
WHERE
    o_orderdate >= CAST('1993-07-01' AS date)
    AND o_orderdate < CAST('1993-10-01' AS date)
    AND EXISTS (
        SELECT
            *
        FROM
            tpch.lineitem
        WHERE
            l_orderkey = o_orderkey
            AND l_commitdate < l_receiptdate)
GROUP BY
    o_orderpriority
ORDER BY
    o_orderpriority;

SELECT
    n_name,
    sum(l_extendedprice * (1 - l_discount)) AS revenue
FROM
    tpch.customer,
    tpch.orders,
    tpch.lineitem,
    tpch.supplier,
    tpch.nation,
    tpch.region
WHERE
    c_custkey = o_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey = s_nationkey
    AND s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND r_name = 'ASIA'
    AND o_orderdate >= CAST('1994-01-01' AS date)
    AND o_orderdate < CAST('1995-01-01' AS date)
GROUP BY
    n_name
ORDER BY
    revenue DESC;

SELECT
    sum(l_extendedprice * l_discount) AS revenue
FROM
    tpch.lineitem
WHERE
    l_shipdate >= CAST('1994-01-01' AS date)
    AND l_shipdate < CAST('1995-01-01' AS date)
    AND l_discount BETWEEN 0.05
    AND 0.07
    AND l_quantity < 24;

SELECT
    supp_nation,
    cust_nation,
    l_year,
    sum(volume) AS revenue
FROM (
    SELECT
        n1.n_name AS supp_nation,
        n2.n_name AS cust_nation,
        extract(year FROM l_shipdate) AS l_year,
        l_extendedprice * (1 - l_discount) AS volume
    FROM
        tpch.supplier,
        tpch.lineitem,
        tpch.orders,
        tpch.customer,
        tpch.nation n1,
        tpch.nation n2
    WHERE
        s_suppkey = l_suppkey
        AND o_orderkey = l_orderkey
        AND c_custkey = o_custkey
        AND s_nationkey = n1.n_nationkey
        AND c_nationkey = n2.n_nationkey
        AND ((n1.n_name = 'FRANCE'
                AND n2.n_name = 'GERMANY')
            OR (n1.n_name = 'GERMANY'
                AND n2.n_name = 'FRANCE'))
        AND l_shipdate BETWEEN CAST('1995-01-01' AS date)
        AND CAST('1996-12-31' AS date)) AS shipping
GROUP BY
    supp_nation,
    cust_nation,
    l_year
ORDER BY
    supp_nation,
    cust_nation,
    l_year;

SELECT
    o_year,
    sum(
        CASE WHEN nation = 'BRAZIL' THEN
            volume
        ELSE
            0
        END) / sum(volume) AS mkt_share
FROM (
    SELECT
        extract(year FROM o_orderdate) AS o_year,
        l_extendedprice * (1 - l_discount) AS volume,
        n2.n_name AS nation
    FROM
        tpch.part,
        tpch.supplier,
        tpch.lineitem,
        tpch.orders,
        tpch.customer,
        tpch.nation n1,
        tpch.nation n2,
        tpch.region
    WHERE
        p_partkey = l_partkey
        AND s_suppkey = l_suppkey
        AND l_orderkey = o_orderkey
        AND o_custkey = c_custkey
        AND c_nationkey = n1.n_nationkey
        AND n1.n_regionkey = r_regionkey
        AND r_name = 'AMERICA'
        AND s_nationkey = n2.n_nationkey
        AND o_orderdate BETWEEN CAST('1995-01-01' AS date)
        AND CAST('1996-12-31' AS date)
        AND p_type = 'ECONOMY ANODIZED STEEL') AS all_nations
GROUP BY
    o_year
ORDER BY
    o_year;

SELECT
    nation,
    o_year,
    sum(amount) AS sum_profit
FROM (
    SELECT
        n_name AS nation,
        extract(year FROM o_orderdate) AS o_year,
        l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity AS amount
    FROM
        tpch.part,
        tpch.supplier,
        tpch.lineitem,
        tpch.partsupp,
        tpch.orders,
        tpch.nation
    WHERE
        s_suppkey = l_suppkey
        AND ps_suppkey = l_suppkey
        AND ps_partkey = l_partkey
        AND p_partkey = l_partkey
        AND o_orderkey = l_orderkey
        AND s_nationkey = n_nationkey
        AND p_name LIKE '%green%') AS profit
GROUP BY
    nation,
    o_year
ORDER BY
    nation,
    o_year DESC;

SELECT
    c_custkey,
    c_name,
    sum(l_extendedprice * (1 - l_discount)) AS revenue,
    c_acctbal,
    n_name,
    c_address,
    c_phone,
    c_comment
FROM
    tpch.customer,
    tpch.orders,
    tpch.lineitem,
    tpch.nation
WHERE
    c_custkey = o_custkey
    AND l_orderkey = o_orderkey
    AND o_orderdate >= CAST('1993-10-01' AS date)
    AND o_orderdate < CAST('1994-01-01' AS date)
    AND l_returnflag = 'R'
    AND c_nationkey = n_nationkey
GROUP BY
    c_custkey,
    c_name,
    c_acctbal,
    c_phone,
    n_name,
    c_address,
    c_comment
ORDER BY
    revenue DESC
LIMIT 20;

SELECT
    ps_partkey,
    sum(ps_supplycost * ps_availqty) AS value
FROM
    tpch.partsupp,
    tpch.supplier,
    tpch.nation
WHERE
    ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND n_name = 'GERMANY'
GROUP BY
    ps_partkey
HAVING
    sum(ps_supplycost * ps_availqty) > (
        SELECT
            sum(ps_supplycost * ps_availqty) * 0.0001000000
        FROM
            tpch.partsupp,
            tpch.supplier,
            tpch.nation
        WHERE
            ps_suppkey = s_suppkey
            AND s_nationkey = n_nationkey
            AND n_name = 'GERMANY')
ORDER BY
    value DESC;

SELECT
    l_shipmode,
    sum(
        CASE WHEN o_orderpriority = '1-URGENT'
            OR o_orderpriority = '2-HIGH' THEN
            1
        ELSE
            0
        END) AS high_line_count,
    sum(
        CASE WHEN o_orderpriority <> '1-URGENT'
            AND o_orderpriority <> '2-HIGH' THEN
            1
        ELSE
            0
        END) AS low_line_count
FROM
    tpch.orders,
    tpch.lineitem
WHERE
    o_orderkey = l_orderkey
    AND l_shipmode IN ('MAIL', 'SHIP')
    AND l_commitdate < l_receiptdate
    AND l_shipdate < l_commitdate
    AND l_receiptdate >= CAST('1994-01-01' AS date)
    AND l_receiptdate < CAST('1995-01-01' AS date)
GROUP BY
    l_shipmode
ORDER BY
    l_shipmode;

SELECT
    c_count,
    count(*) AS custdist
FROM (
    SELECT
        c_custkey,
        count(o_orderkey)
    FROM
        tpch.customer
    LEFT OUTER JOIN tpch.orders ON c_custkey = o_custkey
    AND o_comment NOT LIKE '%special%requests%'
GROUP BY
    c_custkey) AS c_orders (c_custkey,
        c_count)
GROUP BY
    c_count
ORDER BY
    custdist DESC,
    c_count DESC;

SELECT
    100.00 * sum(
        CASE WHEN p_type LIKE 'PROMO%' THEN
            l_extendedprice * (1 - l_discount)
        ELSE
            0
        END) / sum(l_extendedprice * (1 - l_discount)) AS promo_revenue
FROM
    tpch.lineitem,
    tpch.part
WHERE
    l_partkey = p_partkey
    AND l_shipdate >= date '1995-09-01'
    AND l_shipdate < CAST('1995-10-01' AS date);

WITH revenue AS (
    SELECT
        l_suppkey AS supplier_no,
        sum(l_extendedprice * (1 - l_discount)) AS total_revenue
    FROM
        tpch.lineitem
    WHERE
        l_shipdate >= CAST('1996-01-01' AS date)
        AND l_shipdate < CAST('1996-04-01' AS date)
    GROUP BY
        supplier_no
)
SELECT
    s_suppkey,
    s_name,
    s_address,
    s_phone,
    total_revenue
FROM
    tpch.supplier,
    revenue
WHERE
    s_suppkey = supplier_no
    AND total_revenue = (
        SELECT
            max(total_revenue)
        FROM revenue)
ORDER BY
    s_suppkey;

SELECT
    p_brand,
    p_type,
    p_size,
    count(DISTINCT ps_suppkey) AS supplier_cnt
FROM
    tpch.partsupp,
    tpch.part
WHERE
    p_partkey = ps_partkey
    AND p_brand <> 'Brand#45'
    AND p_type NOT LIKE 'MEDIUM POLISHED%'
    AND p_size IN (49, 14, 23, 45, 19, 3, 36, 9)
    AND ps_suppkey NOT IN (
        SELECT
            s_suppkey
        FROM
            tpch.supplier
        WHERE
            s_comment LIKE '%Customer%Complaints%')
GROUP BY
    p_brand,
    p_type,
    p_size
ORDER BY
    supplier_cnt DESC,
    p_brand,
    p_type,
    p_size;

SELECT
    sum(l_extendedprice) / 7.0 AS avg_yearly
FROM
    tpch.lineitem,
    tpch.part
WHERE
    p_partkey = l_partkey
    AND p_brand = 'Brand#23'
    AND p_container = 'MED BOX'
    AND l_quantity < (
        SELECT
            0.2 * avg(l_quantity)
        FROM
            tpch.lineitem
        WHERE
            l_partkey = p_partkey);

SELECT
    c_name,
    c_custkey,
    o_orderkey,
    o_orderdate,
    o_totalprice,
    sum(l_quantity)
FROM
    tpch.customer,
    tpch.orders,
    tpch.lineitem
WHERE
    o_orderkey IN (
        SELECT
            l_orderkey
        FROM
            tpch.lineitem
        GROUP BY
            l_orderkey
        HAVING
            sum(l_quantity) > 300)
    AND c_custkey = o_custkey
    AND o_orderkey = l_orderkey
GROUP BY
    c_name,
    c_custkey,
    o_orderkey,
    o_orderdate,
    o_totalprice
ORDER BY
    o_totalprice DESC,
    o_orderdate
LIMIT 100;

SELECT
    sum(l_extendedprice * (1 - l_discount)) AS revenue
FROM
    tpch.lineitem,
    tpch.part
WHERE (p_partkey = l_partkey
    AND p_brand = 'Brand#12'
    AND p_container IN ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG')
    AND l_quantity >= 1
    AND l_quantity <= 1 + 10
    AND p_size BETWEEN 1 AND 5
    AND l_shipmode IN ('AIR', 'AIR REG')
    AND l_shipinstruct = 'DELIVER IN PERSON')
    OR (p_partkey = l_partkey
        AND p_brand = 'Brand#23'
        AND p_container IN ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK')
        AND l_quantity >= 10
        AND l_quantity <= 10 + 10
        AND p_size BETWEEN 1 AND 10
        AND l_shipmode IN ('AIR', 'AIR REG')
        AND l_shipinstruct = 'DELIVER IN PERSON')
    OR (p_partkey = l_partkey
        AND p_brand = 'Brand#34'
        AND p_container IN ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG')
        AND l_quantity >= 20
        AND l_quantity <= 20 + 10
        AND p_size BETWEEN 1 AND 15
        AND l_shipmode IN ('AIR', 'AIR REG')
        AND l_shipinstruct = 'DELIVER IN PERSON');

SELECT
    s_name,
    s_address
FROM
    tpch.supplier,
    tpch.nation
WHERE
    s_suppkey IN (
        SELECT
            ps_suppkey
        FROM
            tpch.partsupp
        WHERE
            ps_partkey IN (
                SELECT
                    p_partkey
                FROM
                    tpch.part
                WHERE
                    p_name LIKE 'forest%')
                AND ps_availqty > (
                    SELECT
                        0.5 * sum(l_quantity)
                    FROM
                        tpch.lineitem
                    WHERE
                        l_partkey = ps_partkey
                        AND l_suppkey = ps_suppkey
                        AND l_shipdate >= CAST('1994-01-01' AS date)
                        AND l_shipdate < CAST('1995-01-01' AS date)))
            AND s_nationkey = n_nationkey
            AND n_name = 'CANADA'
    ORDER BY
        s_name;

SELECT
    s_name,
    count(*) AS numwait
FROM
    tpch.supplier,
    tpch.lineitem l1,
    tpch.orders,
    tpch.nation
WHERE
    s_suppkey = l1.l_suppkey
    AND o_orderkey = l1.l_orderkey
    AND o_orderstatus = 'F'
    AND l1.l_receiptdate > l1.l_commitdate
    AND EXISTS (
        SELECT
            *
        FROM
            tpch.lineitem l2
        WHERE
            l2.l_orderkey = l1.l_orderkey
            AND l2.l_suppkey <> l1.l_suppkey)
    AND NOT EXISTS (
        SELECT
            *
        FROM
            tpch.lineitem l3
        WHERE
            l3.l_orderkey = l1.l_orderkey
            AND l3.l_suppkey <> l1.l_suppkey
            AND l3.l_receiptdate > l3.l_commitdate)
    AND s_nationkey = n_nationkey
    AND n_name = 'SAUDI ARABIA'
GROUP BY
    s_name
ORDER BY
    numwait DESC,
    s_name
LIMIT 100;

SELECT
    cntrycode,
    count(*) AS numcust,
    sum(c_acctbal) AS totacctbal
FROM (
    SELECT
        substring(c_phone FROM 1 FOR 2) AS cntrycode,
        c_acctbal
    FROM
        tpch.customer
    WHERE
        substring(c_phone FROM 1 FOR 2) IN ('13', '31', '23', '29', '30', '18', '17')
        AND c_acctbal > (
            SELECT
                avg(c_acctbal)
            FROM
                tpch.customer
            WHERE
                c_acctbal > 0.00
                AND substring(c_phone FROM 1 FOR 2) IN ('13', '31', '23', '29', '30', '18', '17'))
            AND NOT EXISTS (
                SELECT
                    *
                FROM
                    tpch.orders
                WHERE
                    o_custkey = c_custkey)) AS custsale
GROUP BY
    cntrycode
ORDER BY
    cntrycode;
"""
