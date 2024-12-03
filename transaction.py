import psycopg2

def establish_connection():
    try:
        conn = psycopg2.connect(
            dbname='cs623HW',
            user='jaisheelpaladugu',
            password='080103',
            host='localhost',
            port=5432
        )
        conn.autocommit = False
        print("Successfully connected to the database.")
        return conn
    except Exception as error:
        print(f"Failed to connect to the database: {error}")
        return None

def process_transaction(conn, sql_statements):
    try:
        with conn.cursor() as cursor:
            for sql in sql_statements:
                cursor.execute(sql)
            conn.commit()
            print("Transaction completed successfully.")
    except Exception as error:
        conn.rollback()
        print(f"Error occurred. Rolling back transaction. Error: {error}")

if __name__ == "__main__":
    conn = establish_connection()
    if conn:
        transaction_list = [
            # Transaction 5
            [
                """
                INSERT INTO Product (prodid, pname, price) 
                VALUES ('p100', 'cd', 5) 
                ON CONFLICT (prodid) DO NOTHING;
                """,
                """
                INSERT INTO Stock (prodid, depid, quantity) 
                VALUES ('p100', 'd2', 50) 
                ON CONFLICT (prodid, depid) DO NOTHING;
                """
            ],
            # Transaction 6
            [
                """
                INSERT INTO Depot (depid, addr, volume) 
                VALUES ('d100', 'Chicago', 100) 
                ON CONFLICT (depid) DO NOTHING;
                """,
                """
                INSERT INTO Stock (prodid, depid, quantity) 
                VALUES ('p1', 'd100', 100) 
                ON CONFLICT (prodid, depid) DO NOTHING;
                """
            ],
            #Transaction 3
            [
                "UPDATE Product SET prodid = 'pp1' WHERE prodid = 'p1';",
                "UPDATE Stock SET prodid = 'pp1' WHERE prodid = 'p1';"
            ],
            # Transaction 4
            [
                "UPDATE Depot SET depid = 'dd1' WHERE depid = 'd1';",
                "UPDATE Stock SET depid = 'dd1' WHERE depid = 'd1';"
            ],
