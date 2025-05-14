import mysql

def list_products(cursor):
    try:
        cursor.execute("SELECT id, name, price, stock FROM products")
        products = cursor.fetchall()

        if not products:
            print("\nNo products found.")
            return

        print("\n--- Product List ---")
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Stock':<6}")
        print("-" * 45)

        for prod in products:
            print(f"{prod[0]:<5} {prod[1]:<20} ${prod[2]:<10.2f} {prod[3]:<6}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_products(conn, name, price, stock):
    try:
        conn.cursor().execute("""
                       INSERT INTO products (name, price, stock)
                       SELECT %s, %s, %s
                       WHERE NOT EXISTS (SELECT 1
                                         FROM products
                                         WHERE name = %s)
                       """, (name, price, stock, name)) #insert only if name don't exist in products
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")