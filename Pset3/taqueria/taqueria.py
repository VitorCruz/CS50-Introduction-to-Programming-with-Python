
def main():
    taqueria_menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    item = input("Order an item: ").title()
    result = make_orders(item, taqueria_menu)
    print("\nTotal:", result)

def make_orders(item, taqueria_menu):
    price = 0
    while True:
        try:
            price += taqueria_menu[item]
            print("Total:", f'${price:.2f}')
            item = input("Order an item: ").title()
        except KeyError:
            item = input("Item not in menu, insert another one: ").title()
        except EOFError:
            break

    return f'${price:.2f}'

if __name__ == "__main__":
    main()