from util import sql_util
def list_customers(cursor):
    try:
        customers = sql_util.get_list(cursor, "customers")
        if not customers:
            print("\nNo customer found.")
            return

        print("\n--- Customers List ---")
        print(f"{'ID':<5} {'Name':<20} {'Email':<10}")
        print("-" * 45)

        for cust in customers:
            print(f"{cust[0]:<5} {cust[1]:<20} {cust[2]:<10}")

    except Exception as e:
        print(f"Error: {e}")


def add_customer(conn, name, email):
    try:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO customers (name, email)
                                SELECT %s, %s WHERE NOT EXISTS (SELECT 1 FROM customers WHERE name = %s)
                              """, (name, email, name))
        conn.commit()
        if cursor.rowcount == 1:
            print("\nCustomer added successfully.")
        else:
            print("\nError: The customer already exists.")

    except Exception as e:
        print(f"Error: {e}")

def update_customer(conn):
    try:
        cursor = conn.cursor()
        list_customers(cursor)
        id = input("Which customer to update?\nEnter customer ID: ")
        name = input("Enter new customer name: ")
        email = input("Enter new customer email: ")
        cursor.execute("""UPDATE customers SET name = %s, email = %s WHERE id = %s""", (name, email, id))
        if cursor.rowcount == 0:
            print("No customer found with that ID.")
        else:
            conn.commit()
            print(f"Customer ID {id} updated successfully.")
    except Exception as e:
        print(f"Error: {e}")