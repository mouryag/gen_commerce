# import mysql.connector

# # Database connection details
# config = {
#     'user': 'Users',
#     'password': 'AIagents2024Green',
#     'host': '34.89.125.152',
#     'port': '3306',
#     'database': 'product-table',
# }

# conn = None
# cursor = None

# try:
#     print("Connecting to the database...")
#     conn = mysql.connector.connect(**config)
#     cursor = conn.cursor()

#     # Query to select some rows from the table
#     query = "SELECT * FROM amazon_products LIMIT 10"
#     cursor.execute(query)

#     # Fetch and print results
#     results = cursor.fetchall()
#     for row in results:
#         print(row)

# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# except Exception as ex:
#     print(f"Exception: {ex}")

# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()
#     print("Database connection closed.")



import sqlite3

# Database connection details (local file)
db_file = 'products.db'

conn = None
cursor = None

try:
    print("Connecting to the database...")
    conn = sqlite3.connect(db_file)  # Connects to the SQLite database (creates file if not exists)
    cursor = conn.cursor()

    # # Create table if it doesn't exist
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS amazon_products (
    #     id INTEGER PRIMARY KEY,
    #     product_name TEXT,
    #     price REAL,
    #     rating REAL
    # )
    # ''')

    # # Insert sample data if the table is empty
    # cursor.execute('SELECT COUNT(*) FROM amazon_products')
    # if cursor.fetchone()[0] == 0:
    #     sample_data = [
    #         ('Laptop', 999.99, 4.5),
    #         ('Headphones', 199.99, 4.3),
    #         ('Smartphone', 799.49, 4.7)
    #     ]
    #     cursor.executemany('INSERT INTO amazon_products (product_name, price, rating) VALUES (?, ?, ?)', sample_data)
    #     conn.commit()
    #     print("Sample data inserted.")

    # Query to select some rows from the table
    query = "SELECT * FROM amazon_products LIMIT 10"
    cursor.execute(query)

    # Fetch and print results
    results = cursor.fetchall()
    for row in results:
        print(row)

except sqlite3.Error as err:
    print(f"Error: {err}")
except Exception as ex:
    print(f"Exception: {ex}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed.")
