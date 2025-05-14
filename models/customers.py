import mysql

def list_customers(cursor):
    try:
        cursor.execute("SELECT id, name, email FROM customers")
        customers = cursor.fetchall()

        if not customers:
            print("\nNo customer found.")
            return

        print("\n--- Customers List ---")
        print(f"{'ID':<5} {'Name':<20} {'Email':<10}")
        print("-" * 45)

        for cust in customers:
            print(f"{cust[0]:<5} {cust[1]:<20} {cust[2]:<10}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
