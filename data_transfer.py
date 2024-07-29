import sqlite3
import mysql.connector
import os

# Paths and credentials
sqlite_db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'GBds@28102001'
mysql_database = 'django'

# List of tables to transfer
tables = [
    'accounts_user',
    'accounts_user_followers',
    'accounts_user_groups',
    'accounts_user_user_permissions',
    'accounts_userprofile',
    'auth_group',
    'auth_group_permissions',
    'auth_permission',
    'chat_comment',
    'chat_post',
    'django_admin_log',
    'django_content_type',
    'django_migrations',
    'django_session'
]

# SQLite connection
sqlite_conn = sqlite3.connect(sqlite_db_path)
sqlite_cursor = sqlite_conn.cursor()

# MySQL connection
mysql_conn = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)
mysql_cursor = mysql_conn.cursor()

def transfer_table_data(table_name):
    # Fetch data from SQLite
    sqlite_cursor.execute(f"SELECT * FROM {table_name}")
    rows = sqlite_cursor.fetchall()

    if rows:
        # Prepare insert query
        column_names = [desc[0] for desc in sqlite_cursor.description]
        # Use INSERT IGNORE to avoid errors due to duplicate primary keys
        insert_query = f"INSERT IGNORE INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(column_names))})"
        
        # Insert data into MySQL
        try:
            mysql_cursor.executemany(insert_query, rows)
            print(f"Data transferred for table: {table_name}")
        except mysql.connector.Error as err:
            print(f"Error transferring data for table {table_name}: {err}")

# Transfer data for all tables
for table in tables:
    transfer_table_data(table)

# Commit changes and close connections
mysql_conn.commit()

sqlite_conn.close()
mysql_conn.close()

print("Data transfer completed successfully for all tables.")
