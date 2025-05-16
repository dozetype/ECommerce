from util import sql_util

def list_order_items(cursor):
    try:
        order_items = sql_util.get_list(cursor, "order_items")
        if not order_items:
            print("No order items found")
            return

        print("\n--- Order Items List ---")
        print(f"{'ID':<5} {'Order ID':<10} {'Product ID':<12} {'Quantity':<12}")
        print("-" * 50)
        for item in order_items:
            print(f"{item[0]:<5} {item[1]:<10} {item[2]:<12} {item[3]:<12}")

    except Exception as e:
        print(f"Error: {e}")

def add_order_item(conn, order_id, items_ordered: list):
    try:
        cursor = conn.cursor()
        items_with_order_id = [(order_id, item[0], item[1]) for item in items_ordered]

        cursor.executemany("INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                           items_with_order_id)
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")

