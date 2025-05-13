from models import products

def main_menu():
    while True:
        print("\n1. List Products")
        print("2. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            products.list_products()
        elif choice == '2':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()