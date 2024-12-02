import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="cs623_project",   # Replace with your database name
            user="jaisheelpaladugu",          # Replace with your PostgreSQL username
            password="080103", # Replace with your PostgreSQL password
            host="localhost",
            port="5432"               # Default PostgreSQL port
        )
        print("Connected to the database successfully!")
        conn.close()
    except Exception as e:
        print(f"Error connecting to the database: {e}")

# Test the connection
if __name__ == "__main__":
    connect_to_db()
