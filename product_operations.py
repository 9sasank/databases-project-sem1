
import psycopg2

def connect_to_db():
    """Function to connect to the PostgreSQL database"""
    try:
        conn = psycopg2.connect(
            dbname="cs623_project",  # Your database name
            user="jaisheelpaladugu",         # Your username
            password="080103",  # Your password
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

def delete_product(prodid):
    """Function to delete a product from the Product and Stock tables"""
    try:
        conn = connect_to_db()
        if conn is None:
            return

        cur = conn.cursor()
        conn.autocommit = False
        
        # Delete from Stock table
        cur.execute("DELETE FROM stock WHERE prodid = %s", (prodid,))
        # Delete from Product table
        cur.execute("DELETE FROM product WHERE prodid = %s", (prodid,))
        
        conn.commit()
        print(f"Product {prodid} deleted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

# Call the function to test (replace with any valid prodid)
if _name_ == "_main_":
    print("Starting product operations...")
    delete_product('P1')  # Replace 'P1' with the product ID you want to delete