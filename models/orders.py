import mysql

def list_orders(cursor):
    try:
        cursor.execute("SELECT id, customer_id, order_date FROM orders")
        orders = cursor.fetchall()
        if not orders:
            print("No orders found")
            return

        print("\n--- Order List ---")
        print(f"{'ID':<5} {'Customer ID':<12} {'Date(Y-M-D H:min:sec)':<20}")
        print("-" * 50)
        for order in orders:
            order_date = order[2].strftime("%Y-%m-%d %H:%M:%S") if order[2] else "N/A"
            print(f"{order[0]:<5} {order[1]:<12} {order_date:<20}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")