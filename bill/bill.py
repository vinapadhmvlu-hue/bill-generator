class MenuItem:
    """Node for Linked List representing a menu item."""
    def __init__(self, name, price):   # fixed
        self.name = name
        self.price = price
        self.next = None


class Menu:
    """Linked List to store the menu."""
    def __init__(self):   # fixed
        self.head = None

    def add_item(self, name, price):
        new_item = MenuItem(name, price)
        if not self.head:
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item

    def get_menu_items(self):
        items = []
        current = self.head
        while current:
            items.append((current.name, current.price))
            current = current.next
        return items

    def bubble_sort_by_price(self):
        items = self.get_menu_items()
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j][1] > items[j + 1][1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items


class Stack:
    """Stack for undo functionality."""
    def __init__(self):   # fixed
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


class BillGenerator:
    """Main class to handle bill generation."""
    def __init__(self):   # fixed
        self.menu = Menu()
        self.orders = []
        self.order_stack = Stack()

    def add_menu_item(self, name, price):
        self.menu.add_item(name, price)

    def display_menu(self):
        menu_items = self.menu.bubble_sort_by_price()
        print("\nMenu (sorted by price):")
        for idx, (name, price) in enumerate(menu_items, 1):
            print(f"{idx}. {name} - ₹{price:.2f}")

    def take_order(self, item_index):
        menu_items = self.menu.bubble_sort_by_price()
        if 0 < item_index <= len(menu_items):
            item_name, item_price = menu_items[item_index - 1]
            self.orders.append((item_name, item_price))
            self.order_stack.push((item_name, item_price))
            print(f"Added {item_name} to the cart.")
        else:
            print("Invalid item selection.")

    def undo_last_order(self):
        last = self.order_stack.pop()
        if last and last in self.orders:
            self.orders.remove(last)
            print(f"Removed {last[0]} from the cart.")
        else:
            print("Nothing to undo.")

    def generate_bill(self):
        print("\n--- Bill ---")
        total = 0
        for name, price in self.orders:
            print(f"{name} - ₹{price:.2f}")
            total += price
        gst = total * 0.18  # 18% GST
        grand_total = total + gst
        print(f"Subtotal: ₹{total:.2f}")
        print(f"GST (18%): ₹{gst:.2f}")
        print(f"Total: ₹{grand_total:.2f}")


# Main Execution
if __name__ == "__main__":   # fixed
    bill_gen = BillGenerator()

    # Adding menu items
    bill_gen.add_menu_item("Burger", 120.00)
    bill_gen.add_menu_item("Pizza", 250.00)
    bill_gen.add_menu_item("Pasta", 180.00)
    bill_gen.add_menu_item("Salad", 100.00)
    bill_gen.add_menu_item("Fries", 80.00)
    bill_gen.add_menu_item("Coke", 50.00)

    while True:
        # Display menu
        bill_gen.display_menu()

        # Take user input for ordering
        print("\nEnter the item number to add to the cart (0 to finish, -1 to undo last item):")
        try:
            choice = int(input("Your choice: "))
            if choice == 0:
                break
            elif choice == -1:
                bill_gen.undo_last_order()
            else:
                bill_gen.take_order(choice)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate the final bill
    bill_gen.generate_bill()
