# ==========================
# Project: Skeleton Template
# ==========================

def main():
    print("Welcome to my Python App")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            feature_one()
        elif choice == "2":
            feature_two()
        elif choice == "3":
            print("Goodbye Dipto 👋")
            break
        else:
            print("Invalid choice")

def show_menu():
    print("\n--- MENU ---")
    print("1. Feature One")
    print("2. Feature Two")
    print("3. Exit")

def feature_one():
    print("This is Feature One")

def feature_two():
    print("This is Feature Two")

# Program starts here
if __name__ == "__main__":
    main()

