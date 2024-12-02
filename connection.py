import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="cs623_project",   
            user="jaisheelpaladugu",          
            password="080103", 
            host="localhost",
            port="5432"               
        )
        print("Connected to the database successfully!")
        conn.close()
    except Exception as e:
        print(f"Error connecting to the database: {e}")


if __name__ == "__main__":
    connect_to_db()
