"""
TPC-C specific utilities for OLTP benchmarking
This module provides functions for TPC-C schema creation, data generation, and transaction execution.
"""

import pandas as pd
import random
import time
import sys
import io
from datetime import datetime
from faker import Faker

# Initialize Faker
fake = Faker()

# Constants
DISTRICTS_PER_WAREHOUSE = 10
CUSTOMERS_PER_DISTRICT = 3000
ITEMS = 100000


def create_tpcc_schema(conn, is_postgres=True):
    """
    Creates the 9 TPC-C tables in the target database.
    
    Args:
        conn: Database connection object
        is_postgres: Whether this is a PostgreSQL connection (default: True)
    """
    schema_prefix = "tpcc." if is_postgres else ""
    real_type = "DECIMAL(10, 4)" if is_postgres else "DOUBLE"
    num_type = "DECIMAL(12, 2)" if is_postgres else "DOUBLE"
    
    queries = [
        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}warehouse (
            w_id INT NOT NULL,
            w_name TEXT,
            w_street_1 TEXT,
            w_street_2 TEXT,
            w_city TEXT,
            w_state CHAR(2),
            w_zip CHAR(9),
            w_tax {real_type},
            w_ytd {num_type}
        );""",
        
        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}district (
            d_id INT NOT NULL,
            d_w_id INT NOT NULL,
            d_name TEXT,
            d_street_1 TEXT,
            d_street_2 TEXT,
            d_city TEXT,
            d_state CHAR(2),
            d_zip CHAR(9),
            d_tax {real_type},
            d_ytd {num_type},
            d_next_o_id INT
        );""",

        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}customer (
            c_id INT NOT NULL,
            c_d_id INT NOT NULL,
            c_w_id INT NOT NULL,
            c_first TEXT,
            c_middle CHAR(2),
            c_last TEXT,
            c_street_1 TEXT,
            c_street_2 TEXT,
            c_city TEXT,
            c_state CHAR(2),
            c_zip CHAR(9),
            c_phone CHAR(16),
            c_since TIMESTAMP,
            c_credit CHAR(2),
            c_credit_lim {num_type},
            c_discount {real_type},
            c_balance {num_type},
            c_ytd_payment {num_type},
            c_payment_cnt INT,
            c_delivery_cnt INT,
            c_data TEXT
        );""",
        
        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}history (
            h_c_id INT,
            h_c_d_id INT,
            h_c_w_id INT,
            h_d_id INT,
            h_w_id INT,
            h_date TIMESTAMP,
            h_amount {num_type},
            h_data TEXT
        );""",

        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}item (
            i_id INT NOT NULL,
            i_im_id INT,
            i_name TEXT,
            i_price {num_type},
            i_data TEXT
        );""",
        
        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}stock (
            s_i_id INT NOT NULL,
            s_w_id INT NOT NULL,
            s_quantity INT,
            s_dist_01 CHAR(24),
            s_dist_02 CHAR(24),
            s_dist_03 CHAR(24),
            s_dist_04 CHAR(24),
            s_dist_05 CHAR(24),
            s_dist_06 CHAR(24),
            s_dist_07 CHAR(24),
            s_dist_08 CHAR(24),
            s_dist_09 CHAR(24),
            s_dist_10 CHAR(24),
            s_ytd INT,
            s_order_cnt INT,
            s_remote_cnt INT,
            s_data TEXT
        );""",

        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}orders (
            o_id INT NOT NULL,
            o_d_id INT NOT NULL,
            o_w_id INT NOT NULL,
            o_c_id INT,
            o_entry_d TIMESTAMP,
            o_carrier_id INT,
            o_ol_cnt INT,
            o_all_local INT
        );""",
        
        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}new_order (
            no_o_id INT NOT NULL,
            no_d_id INT NOT NULL,
            no_w_id INT NOT NULL
        );""",
        
        f"""CREATE TABLE IF NOT EXISTS {schema_prefix}order_line (
            ol_o_id INT NOT NULL,
            ol_d_id INT NOT NULL,
            ol_w_id INT NOT NULL,
            ol_number INT NOT NULL,
            ol_i_id INT,
            ol_supply_w_id INT,
            ol_delivery_d TIMESTAMP,
            ol_quantity INT,
            ol_amount {num_type},
            ol_dist_info CHAR(24)
        );"""
    ]
    
    print(f"Creating 9 TPC-C tables ({'PostgreSQL' if is_postgres else 'DuckDB'})...")
    if is_postgres:
        with conn.cursor() as cursor:
            for q in queries:
                cursor.execute(q)
        conn.commit()
    else:
        for q in queries:
            conn.execute(q)
    print("Tables created.")


def generate_mock_data(scale_factor):
    """
    Generates mock data for TPC-C tables and returns dict of DataFrames.
    
    Args:
        scale_factor: Number of warehouses to generate
        
    Returns:
        Dictionary of pandas DataFrames for each TPC-C table
    """
    print(f"Generating mock data for {scale_factor} warehouse(s)...")
    
    # 1. Item
    items = []
    for i in range(1, ITEMS + 1):
        items.append({
            "i_id": i,
            "i_im_id": random.randint(1, 10000),
            "i_name": fake.text(max_nb_chars=24),
            "i_price": round(random.uniform(1.00, 100.00), 2),
            "i_data": fake.text(max_nb_chars=50)
        })
    df_item = pd.DataFrame(items)

    # 2. Warehouse
    warehouses = []
    for w in range(1, scale_factor + 1):
        warehouses.append({
            "w_id": w,
            "w_name": fake.company(),
            "w_street_1": fake.street_address(),
            "w_street_2": fake.secondary_address(),
            "w_city": fake.city(),
            "w_state": fake.state_abbr(),
            "w_zip": fake.zipcode(),
            "w_tax": round(random.uniform(0.0000, 0.2000), 4),
            "w_ytd": 300000.00
        })
    df_warehouse = pd.DataFrame(warehouses)
    
    districts = []
    customers = []
    stocks = []
    
    for w_id in range(1, scale_factor + 1):
        # 3. Stock
        for i_id in range(1, ITEMS + 1):
            stocks.append({
                "s_i_id": i_id,
                "s_w_id": w_id,
                "s_quantity": random.randint(10, 100),
                "s_dist_01": fake.password(length=24),
                "s_dist_02": fake.password(length=24),
                "s_dist_03": fake.password(length=24),
                "s_dist_04": fake.password(length=24),
                "s_dist_05": fake.password(length=24),
                "s_dist_06": fake.password(length=24),
                "s_dist_07": fake.password(length=24),
                "s_dist_08": fake.password(length=24),
                "s_dist_09": fake.password(length=24),
                "s_dist_10": fake.password(length=24),
                "s_ytd": 0,
                "s_order_cnt": 0,
                "s_remote_cnt": 0,
                "s_data": fake.text(max_nb_chars=50)
            })
            
        for d_id in range(1, DISTRICTS_PER_WAREHOUSE + 1):
            # 4. District
            districts.append({
                "d_id": d_id,
                "d_w_id": w_id,
                "d_name": fake.city(),
                "d_street_1": fake.street_address(),
                "d_street_2": fake.secondary_address(),
                "d_city": fake.city(),
                "d_state": fake.state_abbr(),
                "d_zip": fake.zipcode(),
                "d_tax": round(random.uniform(0.0000, 0.2000), 4),
                "d_ytd": 30000.00,
                "d_next_o_id": 3001
            })
            
            # 5. Customer
            for c_id in range(1, CUSTOMERS_PER_DISTRICT + 1):
                customers.append({
                    "c_id": c_id,
                    "c_d_id": d_id,
                    "c_w_id": w_id,
                    "c_first": fake.first_name(),
                    "c_middle": "OE",
                    "c_last": fake.last_name(),
                    "c_street_1": fake.street_address(),
                    "c_street_2": fake.secondary_address(),
                    "c_city": fake.city(),
                    "c_state": fake.state_abbr(),
                    "c_zip": fake.zipcode(),
                    "c_phone": fake.phone_number(),
                    "c_since": fake.date_time_this_decade(),
                    "c_credit": "GC",
                    "c_credit_lim": 50000.00,
                    "c_discount": round(random.uniform(0.0000, 0.5000), 4),
                    "c_balance": -10.00,
                    "c_ytd_payment": 10.00,
                    "c_payment_cnt": 1,
                    "c_delivery_cnt": 0,
                    "c_data": fake.text(max_nb_chars=100)
                })

    df_district = pd.DataFrame(districts)
    df_customer = pd.DataFrame(customers)
    df_stock = pd.DataFrame(stocks)
    
    # Empty tables for dynamic data
    df_history = pd.DataFrame(columns=["h_c_id", "h_c_d_id", "h_c_w_id", "h_d_id", "h_w_id", "h_date", "h_amount", "h_data"])
    df_orders = pd.DataFrame(columns=["o_id", "o_d_id", "o_w_id", "o_c_id", "o_entry_d", "o_carrier_id", "o_ol_cnt", "o_all_local"])
    df_new_order = pd.DataFrame(columns=["no_o_id", "no_d_id", "no_w_id"])
    df_order_line = pd.DataFrame(columns=["ol_o_id", "ol_d_id", "ol_w_id", "ol_number", "ol_i_id", "ol_supply_w_id", "ol_delivery_d", "ol_quantity", "ol_amount", "ol_dist_info"])

    print("Mock data generated.")
    return {
        "warehouse": df_warehouse,
        "district": df_district,
        "customer": df_customer,
        "history": df_history,
        "item": df_item,
        "stock": df_stock,
        "orders": df_orders,
        "new_order": df_new_order,
        "order_line": df_order_line
    }


def load_data_postgres(conn, tables_df):
    """Loads data into PostgreSQL using psycopg2.copy_expert."""
    print("Loading data into PostgreSQL...")
    start_time = time.time()
    
    table_names = ["warehouse", "district", "customer", "history", "item", "stock", "orders", "new_order", "order_line"]
    
    with conn.cursor() as cursor:
        for table in table_names:
            df = tables_df[table]
            if df.empty:
                print(f"  Skipping empty table: {table}")
                continue
                
            print(f"  Loading {table} ({len(df)} rows)...")
            
            buffer = io.StringIO()
            df.to_csv(buffer, index=False, header=False, sep='\t', na_rep='\\N')
            buffer.seek(0)
            
            try:
                cursor.execute(f"TRUNCATE tpcc.{table} CASCADE;")
                copy_sql = f"COPY tpcc.{table} FROM STDIN WITH (FORMAT CSV, DELIMITER E'\\t', NULL '\\N')"
                cursor.copy_expert(copy_sql, buffer)
            except Exception as e:
                print(f"Error loading table {table}: {e}")
                conn.rollback()
                return
    
    conn.commit()
    end_time = time.time()
    print(f"PostgreSQL load complete in {end_time - start_time:.2f} seconds.")


def load_data_duckdb(conn, tables_df):
    """Loads data into DuckDB using DataFrames."""
    print("Loading data into DuckDB...")
    start_time = time.time()
    
    table_names = ["warehouse", "district", "customer", "history", "item", "stock", "orders", "new_order", "order_line"]
    
    try:
        for table in table_names:
            df = tables_df[table]
            if df.empty:
                print(f"  Skipping empty table: {table}")
                continue
                
            print(f"  Loading {table} ({len(df)} rows)...")
            conn.register(f'df_{table}', df)
            conn.execute(f"TRUNCATE {table};")
            conn.execute(f"INSERT INTO {table} SELECT * FROM df_{table};")
            conn.unregister(f'df_{table}')
            
    except Exception as e:
        print(f"Error loading table {table}: {e}")
        return
        
    end_time = time.time()
    print(f"DuckDB load complete in {end_time - start_time:.2f} seconds.")


# SQL Queries for PostgreSQL (uses %s)
PG_SQL = {
    "get_district": "SELECT d_next_o_id, d_tax FROM tpcc.district WHERE d_w_id = %s AND d_id = %s FOR UPDATE",
    "inc_next_o_id": "UPDATE tpcc.district SET d_next_o_id = d_next_o_id + 1 WHERE d_w_id = %s AND d_id = %s",
    "get_customer": "SELECT c_discount, c_last, c_credit FROM tpcc.customer WHERE c_w_id = %s AND c_d_id = %s AND c_id = %s",
    "create_order": "INSERT INTO tpcc.orders (o_id, o_d_id, o_w_id, o_c_id, o_entry_d, o_ol_cnt, o_all_local) VALUES (%s, %s, %s, %s, %s, %s, 1)",
    "create_new_order": "INSERT INTO tpcc.new_order (no_o_id, no_d_id, no_w_id) VALUES (%s, %s, %s)",
    "get_item": "SELECT i_price, i_name, i_data FROM tpcc.item WHERE i_id = %s",
    "get_stock": "SELECT s_quantity, s_data, s_dist_01 FROM tpcc.stock WHERE s_i_id = %s AND s_w_id = %s FOR UPDATE",
    "update_stock": "UPDATE tpcc.stock SET s_quantity = %s, s_ytd = s_ytd + %s, s_order_cnt = s_order_cnt + 1 WHERE s_i_id = %s AND s_w_id = %s",
    "create_order_line": "INSERT INTO tpcc.order_line (ol_o_id, ol_d_id, ol_w_id, ol_number, ol_i_id, ol_supply_w_id, ol_quantity, ol_amount, ol_dist_info) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "payment_w": "UPDATE tpcc.warehouse SET w_ytd = w_ytd + %s WHERE w_id = %s",
    "payment_d": "UPDATE tpcc.district SET d_ytd = d_ytd + %s WHERE d_w_id = %s AND d_id = %s",
    "payment_c": "UPDATE tpcc.customer SET c_balance = c_balance - %s, c_ytd_payment = c_ytd_payment + %s, c_payment_cnt = c_payment_cnt + 1 WHERE c_w_id = %s AND c_d_id = %s AND c_id = %s",
    "payment_h": "INSERT INTO tpcc.history (h_c_id, h_c_d_id, h_c_w_id, h_d_id, h_w_id, h_date, h_amount) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    "order_status": "SELECT o_id, o_c_id, o_entry_d, o_carrier_id FROM tpcc.orders WHERE o_w_id = %s AND o_d_id = %s AND o_c_id = %s ORDER BY o_id DESC LIMIT 1",
    "order_status_lines": "SELECT ol_i_id, ol_supply_w_id, ol_quantity, ol_amount, ol_delivery_d FROM tpcc.order_line WHERE ol_w_id = %s AND ol_d_id = %s AND ol_o_id = %s"
}

# SQL Queries for DuckDB (uses ?)
DUCK_SQL = {
    "get_district": "SELECT d_next_o_id, d_tax FROM district WHERE d_w_id = ? AND d_id = ?",
    "inc_next_o_id": "UPDATE district SET d_next_o_id = d_next_o_id + 1 WHERE d_w_id = ? AND d_id = ?",
    "get_customer": "SELECT c_discount, c_last, c_credit FROM customer WHERE c_w_id = ? AND c_d_id = ? AND c_id = ?",
    "create_order": "INSERT INTO orders (o_id, o_d_id, o_w_id, o_c_id, o_entry_d, o_ol_cnt, o_all_local) VALUES (?, ?, ?, ?, ?, ?, 1)",
    "create_new_order": "INSERT INTO new_order (no_o_id, no_d_id, no_w_id) VALUES (?, ?, ?)",
    "get_item": "SELECT i_price, i_name, i_data FROM item WHERE i_id = ?",
    "get_stock": "SELECT s_quantity, s_data, s_dist_01 FROM stock WHERE s_i_id = ? AND s_w_id = ?",
    "update_stock": "UPDATE stock SET s_quantity = ?, s_ytd = s_ytd + ?, s_order_cnt = s_order_cnt + 1 WHERE s_i_id = ? AND s_w_id = ?",
    "create_order_line": "INSERT INTO order_line (ol_o_id, ol_d_id, ol_w_id, ol_number, ol_i_id, ol_supply_w_id, ol_quantity, ol_amount, ol_dist_info) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    "payment_w": "UPDATE warehouse SET w_ytd = w_ytd + ? WHERE w_id = ?",
    "payment_d": "UPDATE district SET d_ytd = d_ytd + ? WHERE d_w_id = ? AND d_id = ?",
    "payment_c": "UPDATE customer SET c_balance = c_balance - ?, c_ytd_payment = c_ytd_payment + ?, c_payment_cnt = c_payment_cnt + 1 WHERE c_w_id = ? AND c_d_id = ? AND c_id = ?",
    "payment_h": "INSERT INTO history (h_c_id, h_c_d_id, h_c_w_id, h_d_id, h_w_id, h_date, h_amount) VALUES (?, ?, ?, ?, ?, ?, ?)",
    "order_status": "SELECT o_id, o_c_id, o_entry_d, o_carrier_id FROM orders WHERE o_w_id = ? AND o_d_id = ? AND o_c_id = ? ORDER BY o_id DESC LIMIT 1",
    "order_status_lines": "SELECT ol_i_id, ol_supply_w_id, ol_quantity, ol_amount, ol_delivery_d FROM order_line WHERE ol_w_id = ? AND ol_d_id = ? AND ol_o_id = ?"
}


def run_new_order(conn, sql, is_postgres, scale_factor):
    """Simplified TPC-C New-Order Transaction"""
    w_id = random.randint(1, scale_factor)
    d_id = random.randint(1, DISTRICTS_PER_WAREHOUSE)
    c_id = random.randint(1, CUSTOMERS_PER_DISTRICT)
    ol_cnt = random.randint(5, 15)
    
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql["get_district"], (w_id, d_id))
        district_result = cursor.fetchone()
        if not district_result:
            return False
        d_next_o_id, d_tax = district_result
        
        cursor.execute(sql["inc_next_o_id"], (w_id, d_id))
        cursor.execute(sql["get_customer"], (w_id, d_id, c_id))
        customer_result = cursor.fetchone()
        if not customer_result:
            return False
        c_discount, c_last, c_credit = customer_result

        o_id = d_next_o_id
        o_entry_d = datetime.now()
        cursor.execute(sql["create_order"], (o_id, d_id, w_id, c_id, o_entry_d, ol_cnt))
        cursor.execute(sql["create_new_order"], (o_id, d_id, w_id))
        
        total_amount = 0
        
        for ol_number in range(1, ol_cnt + 1):
            i_id = random.randint(1, ITEMS)
            
            cursor.execute(sql["get_item"], (i_id,))
            item_result = cursor.fetchone()
            if not item_result:
                continue  # Skip this line item if item doesn't exist
            i_price, i_name, i_data = item_result
            
            cursor.execute(sql["get_stock"], (i_id, w_id))
            stock_result = cursor.fetchone()
            if not stock_result:
                continue  # Skip this line item if stock doesn't exist
            s_quantity, s_data, s_dist_01 = stock_result
            
            if s_quantity > 10:
                s_quantity = s_quantity - 1
            else:
                s_quantity = s_quantity - 1 + 91
            
            cursor.execute(sql["update_stock"], (s_quantity, 1, i_id, w_id))
            
            ol_amount = 1 * i_price
            total_amount += ol_amount
            
            cursor.execute(sql["create_order_line"], (o_id, d_id, w_id, ol_number, i_id, w_id, 1, ol_amount, s_dist_01))
            
        conn.commit()
        return True
        
    except Exception as e:
        if is_postgres: 
            conn.rollback()
        print(f"  [Error] New Order TX failed: {e}")
        return False
    finally:
        cursor.close()


def run_payment(conn, sql, is_postgres, scale_factor):
    """Simplified TPC-C Payment Transaction"""
    w_id = random.randint(1, scale_factor)
    d_id = random.randint(1, DISTRICTS_PER_WAREHOUSE)
    c_id = random.randint(1, CUSTOMERS_PER_DISTRICT)
    h_amount = round(random.uniform(1.00, 5000.00), 2)
    h_date = datetime.now()
    
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql["payment_w"], (h_amount, w_id))
        if cursor.rowcount == 0:
            return False
            
        cursor.execute(sql["payment_d"], (h_amount, w_id, d_id))
        if cursor.rowcount == 0:
            return False
            
        cursor.execute(sql["payment_c"], (h_amount, h_amount, w_id, d_id, c_id))
        if cursor.rowcount == 0:
            return False
            
        cursor.execute(sql["payment_h"], (c_id, d_id, w_id, d_id, w_id, h_date, h_amount))
        
        conn.commit()
        return True

    except Exception as e:
        if is_postgres: 
            conn.rollback()
        print(f"  [Error] Payment TX failed: {e}")
        return False
    finally:
        cursor.close()


def run_order_status(conn, sql, scale_factor):
    """Simplified TPC-C Order-Status Transaction (Read-Only)"""
    w_id = random.randint(1, scale_factor)
    d_id = random.randint(1, DISTRICTS_PER_WAREHOUSE)
    c_id = random.randint(1, CUSTOMERS_PER_DISTRICT)
    
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql["order_status"], (w_id, d_id, c_id))
        order = cursor.fetchone()
        
        if order:
            o_id, o_c_id, o_entry_d, o_carrier_id = order
            cursor.execute(sql["order_status_lines"], (w_id, d_id, o_id))
            order_lines = cursor.fetchall()
        
        return True

    except Exception as e:
        print(f"  [Error] Order Status TX failed: {e}")
        return False
    finally:
        cursor.close()


def run_benchmark(db_name, conn, sql_map, is_postgres, scale_factor, total_transactions=200):
    """Runs the mixed transaction workload against the given DB."""
    
    print(f"\n--- Running TPC-C Benchmark on {db_name} ---")
    
    tx_counts = {"new_order": 0, "payment": 0, "order_status": 0}
    tx_failures = {"new_order": 0, "payment": 0, "order_status": 0}
    
    start_time = time.time()
    
    for i in range(total_transactions):
        val = random.uniform(0, 100)
        
        if val <= 45:
            tx_counts["new_order"] += 1
            if not run_new_order(conn, sql_map, is_postgres, scale_factor):
                tx_failures["new_order"] += 1
                
        elif val <= 90:
            tx_counts["payment"] += 1
            if not run_payment(conn, sql_map, is_postgres, scale_factor):
                tx_failures["payment"] += 1
        
        else:
            tx_counts["order_status"] += 1
            if not run_order_status(conn, sql_map, scale_factor):
                tx_failures["order_status"] += 1

    end_time = time.time()
    
    total_time = end_time - start_time
    tps = total_transactions / total_time
    
    print(f"--- {db_name} Results ---")
    print(f"  Total Transactions: {total_transactions}")
    print(f"  Total Time: {total_time:.2f} seconds")
    print(f"  Transactions Per Second (TPS): {tps:.2f}")
    print("  Transaction Mix (Success/Total):")
    print(f"    New Order:    {tx_counts['new_order'] - tx_failures['new_order']} / {tx_counts['new_order']}")
    print(f"    Payment:      {tx_counts['payment'] - tx_failures['payment']} / {tx_counts['payment']}")
    print(f"    Order Status: {tx_counts['order_status'] - tx_failures['order_status']} / {tx_counts['order_status']}")
