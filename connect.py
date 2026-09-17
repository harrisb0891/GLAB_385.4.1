import mysql.connector as mydbconnection
from mysql.connector import Error


def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
            database='classicmodels',
            user='root',
            password='password'
        )


    except Error as e:
        print(f'❌ Error: {e}')
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('✅ Connected.')

        cursor = conn.cursor()

if __name__ == "__main__":
    connect()