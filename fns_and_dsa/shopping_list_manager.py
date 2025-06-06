def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        
        # Get user choice as integer
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        # Add item
        if choice == 1:
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: {item}")
            else:
                print("Error: Item name cannot be empty")
        
        # Remove item
        elif choice == 2:
            if not shopping_list:
                print("The list is empty")
                continue
                
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed: {item}")
            else:
                print(f"Error: {item} not found in list")
        
        # View list
        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty")
            else:
                print("\nCurrent Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
        
        # Exit program
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break
        
        # Invalid choice
        else:
            print("Invalid choice. Please enter a number 1-4")

if __name__ == "__main__":
    main()