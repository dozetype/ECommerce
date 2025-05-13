from db_config import get_connection

def list_products():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id, name, price, stock FROM products"
    cursor.execute(query)
    products = cursor.fetchall()

    print("\n--- Product List ---")
    for prod in products:
        print(f"ID: {prod[0]}, Name: {prod[1]}, Price: ${prod[2]:.2f}, Stock: {prod[3]}")

    cursor.close()
    conn.close()
