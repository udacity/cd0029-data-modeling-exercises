"""
Database utility functions for Exercise 3: OLTP vs OLAP Use Cases
This module provides reusable connection and query execution functions.
"""

import psycopg2
import duckdb
import sys


def create_pg_connection(dbname='postgres', user='postgres', password='postgres', 
                        host='127.0.0.1', port='5432'):
    """
    Creates a psycopg2 connection to PostgreSQL.
    
    Args:
        dbname: Database name (default: 'postgres')
        user: Username (default: 'postgres')
        password: Password (default: 'postgres')
        host: Host address (default: '127.0.0.1')
        port: Port number (default: '5432')
    
    Returns:
        psycopg2 connection object
    
    Raises:
        SystemExit: If connection fails
    """
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = False  # Control transactions manually
        return conn
    except Exception as e:
        print(f"Error: Could not connect to PostgreSQL.")
        print(f"Details: {e}")
        print("Please check the connection parameters.")
        sys.exit(1)


def connect_to_duckdb(database='tpch.duckdb', read_only=False):
    """
    Connects to the DuckDB database file.
    
    Args:
        database: Path to DuckDB database file (default: 'tpch.duckdb')
        read_only: Whether to open in read-only mode (default: False)
    
    Returns:
        duckdb connection object
    
    Raises:
        SystemExit: If connection fails
    """
    try:
        conn = duckdb.connect(database=database, read_only=read_only)
        print(f"Successfully connected to DuckDB at '{database}'.")
        return conn
    except Exception as e:
        print(f"Error: Could not connect to DuckDB at '{database}'.")
        print(f"Details: {e}")
        sys.exit(1)


def execute_query(conn, sql_query, fetch=False):
    """
    Execute a SQL query on the given connection.
    
    Args:
        conn: Database connection object (psycopg2 or similar)
        sql_query: SQL query string to execute
        fetch: Whether to fetch and return results (default: False)
    
    Returns:
        Query results if fetch=True, None otherwise
    """
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        if fetch:
            results = cursor.fetchall()
            print(results)
            return results
        conn.commit()
    finally:
        cursor.close()


def ensure_tpcc_schema(conn):
    """
    Ensures the 'tpcc' schema exists in PostgreSQL.
    
    Args:
        conn: psycopg2 connection object
    """
    with conn.cursor() as cursor:
        cursor.execute("CREATE SCHEMA IF NOT EXISTS tpcc;")
    conn.commit()
    print("Successfully ensured 'tpcc' schema exists.")


def ensure_tpch_schema(conn):
    """
    Ensures the 'tpch' schema exists in PostgreSQL.
    
    Args:
        conn: psycopg2 connection object
    """
    with conn.cursor() as cursor:
        cursor.execute("CREATE SCHEMA IF NOT EXISTS tpch;")
    conn.commit()
    print("Successfully ensured 'tpch' schema exists.")


def map_duckdb_to_postgres_type(duckdb_type):
    """
    Maps DuckDB data types to compatible PostgreSQL data types.
    
    Args:
        duckdb_type: DuckDB type string
    
    Returns:
        PostgreSQL compatible type string
    """
    duckdb_type = duckdb_type.upper()
    
    if duckdb_type == 'VARCHAR':
        return 'TEXT'
    if duckdb_type == 'DOUBLE':
        return 'DOUBLE PRECISION'
    if duckdb_type.startswith('DECIMAL') or duckdb_type.startswith('NUMERIC'):
        return duckdb_type  # e.g., DECIMAL(15, 2)
    if duckdb_type in ('INTEGER', 'BIGINT', 'DATE', 'TIMESTAMP'):
        return duckdb_type
    
    # Default fallback
    return 'TEXT'
