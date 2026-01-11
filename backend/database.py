"""
Database operations for calculator app using SQLite
"""
import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'calculator.db')

def get_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def init_db():
    """Initialize the database and create tables if they don't exist"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result REAL NOT NULL,
            operation_type TEXT CHECK(operation_type IN ('arithmetic', 'scientific')),
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully")

def save_calculation(expression, result, operation_type='arithmetic'):
    """
    Save a calculation to the database

    Args:
        expression (str): The mathematical expression
        result (float): The calculated result
        operation_type (str): 'arithmetic' or 'scientific'

    Returns:
        int: The ID of the inserted record
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO calculations (expression, result, operation_type, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (expression, result, operation_type, datetime.now()))

    calculation_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return calculation_id

def get_history(limit=10):
    """
    Get the latest calculations from the database

    Args:
        limit (int): Number of records to retrieve (default: 10)

    Returns:
        list: List of calculation dictionaries
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id, expression, result, operation_type, timestamp
        FROM calculations
        ORDER BY id DESC
        LIMIT ?
    ''', (limit,))

    rows = cursor.fetchall()
    conn.close()

    # Convert rows to dictionaries
    calculations = []
    for row in rows:
        calculations.append({
            'id': row['id'],
            'expression': row['expression'],
            'result': row['result'],
            'operation_type': row['operation_type'],
            'timestamp': row['timestamp']
        })

    return calculations

def delete_calculation(calculation_id):
    """
    Delete a specific calculation by ID

    Args:
        calculation_id (int): The ID of the calculation to delete

    Returns:
        bool: True if deleted, False if not found
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM calculations WHERE id = ?', (calculation_id,))
    rows_affected = cursor.rowcount

    conn.commit()
    conn.close()

    return rows_affected > 0

def clear_history():
    """
    Delete all calculations from the database

    Returns:
        int: Number of records deleted
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) as count FROM calculations')
    count = cursor.fetchone()['count']

    cursor.execute('DELETE FROM calculations')

    conn.commit()
    conn.close()

    return count

# Initialize database when module is imported
if __name__ == '__main__':
    init_db()
    print(f"Database created at: {DB_PATH}")
