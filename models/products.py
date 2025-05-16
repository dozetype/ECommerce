from util import sql_util

def list_products(cursor):
    try:
        products = sql_util.get_list(cursor, "products")
        if not products:
            print("\nNo products found.")
            return

        print("\n--- Product List ---")
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Stock':<6}")
        print("-" * 45)

        for prod in products:
            print(f"{prod[0]:<5} {prod[1]:<20} ${prod[2]:<10.2f} {prod[3]:<6}")

    except Exception as e:
        print(f"Error: {e}")

def add_products(conn, name, price, stock):
    try:
        # insert only if name don't exist in products
        conn.cursor().execute("""
                       INSERT INTO products (name, price, stock)
                       SELECT %s, %s, %s WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = %s)
                       """, (name, price, stock, name))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")

def update_products(conn):
    try:
        cursor = conn.cursor()
        list_products(cursor)
        id = input("Which product to update?\nEnter product ID: ")
        name = input("Enter new customer name: ")
        email = input("Enter new customer email: ")
        cursor.execute("""UPDATE customers
                          SET name  = %s,
                              email = %s
                          WHERE id = %s""", (name, email, id))
        if cursor.rowcount == 0:
            print("No customer found with that ID.")
        else:
            conn.commit()
            print(f"Customer ID {id} updated successfully.")
    except Exception as e:
        print(f"Error: {e}")