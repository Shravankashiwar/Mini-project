class Inventory:
    def _init_(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                print(f"{quantity} {item_name}(s) removed from inventory.")
            else:
                print("Insufficient quantity in inventory.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        print("\nInventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. Display inventory")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(item_name, quantity)
        elif choice == '3':
            inventory.display_inventory()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if _name_ == "_main_":
    main()