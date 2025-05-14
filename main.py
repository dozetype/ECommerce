from db_config import get_connection
from models import products
from models import customers
from models import orders
from models import orderItems


def main_menu(cursor):
    while True:
        print("\n--- Main Menu ---")
        print("1. List Products")
        print("2. List Customers")
        print("3. List Orders")
        print("4. List Order Items")
        print("5. Add New Product")
        print("0. Exit")
        choice = input("Enter choice: ")
        match choice:
            case "1":
                products.list_products(cursor)
            case "2":
                customers.list_customers(cursor)
            case "3":
                orders.list_orders(cursor)
            case "4":
                orderItems.list_order_items(cursor)
            case "5":
                name = input("Enter product name: ")
                price = input("Enter product price: ")
                stock = input("Enter product stock: ")
                products.update_products(conn, name, price, stock)
            case "0":
                print("Exiting program.")
                break
            case _:
                print("INVALID INPUT")

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    main_menu(cursor)
    
cursor.close()
conn.close()