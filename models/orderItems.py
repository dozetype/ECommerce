import mysql

def list_order_items(cursor):
    try:
        cursor.execute("SELECT id, order_id, product_id, quantity FROM order_items")
        order_items = cursor.fetchall()
        if not order_items:
            print("No order items found")
            return

        print("\n--- Order Items List ---")
        print(f"{'ID':<5} {'Order ID':<10} {'Product ID':<12} {'Quantity':<12}")
        print("-" * 50)
        for item in order_items:
            print(f"{item[0]:<5} {item[1]:<10} {item[2]:<12} {item[3]:<12}")


    except mysql.connector.Error as err:
        print(f"Error: {err}")