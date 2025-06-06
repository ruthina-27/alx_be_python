def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Must be exactly this variable name
    while True:
        display_menu()  # Must call this function
        
        try:
            choice = int(input("Enter your choice (1-4): "))  # Must accept numeric input
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == 2:
            if not shopping_list:
                print("The list is empty.")
                continue
                
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
                
        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\nCurrent Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
                    
        elif choice == 4:
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()