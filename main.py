from config.db_config import get_connection
from models import products
from models import customers
from models import orders
from models import order_items

cust_id = 0
def login():
   return 3


def main_menu(cursor):
    while True:
        choice = input("Enter choice: ")
        match choice:
            case "1": #List Products
                products.list_products(cursor)
            case "2": #List Customers
                customers.list_customers(cursor)
            case "3": #List Orders
                orders.list_orders(cursor)
            case "4": #List Order Items
                order_items.list_order_items(cursor)
            case "5": #Add New Product
                name = input("Enter product name: ")
                price = input("Enter product price: ")
                stock = input("Enter product stock: ")
                products.add_products(conn, name, price, stock)
            case "6": #Add New Customer
                name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                customers.add_customer(conn, name, email)
            case "7": #Update Customer
                customers.update_customer(conn)
            case "8": #Adding new order for customer order
                orders.add_order(conn, cust_id, [(6,2)])
            case "9": #delete a customer
                customers.delete_customer(conn)
            case "0": # Exit
                print("Exiting program.")
                break
            case _:
                print("INVALID INPUT")

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()

    cust_id = login()
    main_menu(cursor)

    cursor.close()
    conn.close()

