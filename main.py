
items = {
    "apple": 5.99,
    "banana": 3.50,
    "bread": 2.25,
}

cart = []

def display_items():
    print("\nAvailable items in store:")
    for item, price in items.items():
        print(f" {item}: {price}")

def add_to_cart():
    item = input("Enter the name of the item you want to add: ")
    if item in items:
        cart.append(item)
        print(f"Added {item} to your shopping cart.")
    else:
        print("Sorry, that item is not available in the store.")
def view_cart():
    if not cart:
        print("Your shopping cart is empty.")
    else:
        print("\nYour shopping cart contents:")
        total = 0
        for item in cart:
            price = items[item]
            print(f" {item}: {price}")
            total += price
        
        print(f"\nTotal: {total}")
def main():
    
    while True:
    
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            display_items()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            print("Thank you for using the shopping cart program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
