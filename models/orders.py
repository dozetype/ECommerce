from util import sql_util
from models import order_items
from datetime import datetime

def list_orders(cursor):
    """
    List all orders
    :param cursor: cursor to the mysql connection
    """
    try:
        orders = sql_util.get_list(cursor, "orders")
        if not orders:
            print("No orders found")
            return

        print("\n--- Order List ---")
        print(f"{'ID':<5} {'Customer ID':<12} {'Date(Y-M-D H:min:sec)':<20}")
        print("-" * 50)
        for order in orders:
            order_date = order[2].strftime("%Y-%m-%d %H:%M:%S") if order[2] else "N/A"
            print(f"{order[0]:<5} {order[1]:<12} {order_date:<20}")

    except Exception as e:
        print(f"Error: {e}")

def add_order(conn, customer_id, items_ordered):
    try:
        if not items_ordered:
            print("No items ordered")
            return

        cursor = conn.cursor()
        now = datetime.now()
        cursor.execute("INSERT INTO orders(customer_id, order_date) VALUES (%s, %s)", (customer_id, now.strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        order_id = cursor.lastrowid
        order_items.add_order_item(conn, order_id, items_ordered)
        if cursor.rowcount != 0:
            print(f"Order {order_id} added successfully.")
        else:
            print(f"Order {order_id} not added successfully.")

    except Exception as e:
        print(f"Error: {e}")