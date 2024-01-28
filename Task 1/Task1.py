def calculate_price(num_pizzas, is_delivery, is_tuesday, used_app):
    pizza_price = 12.00
    delivery_cost = 2.50
    app_discount = 0.25
    tuesday_discount = 0.50

    while not isinstance(num_pizzas, int) or num_pizzas < 0:
        print("Please enter a positive integer!")
        num_pizzas = input("How many pizzas ordered? ")

    while is_delivery.lower() not in ['y', 'n']:
        print('Please answer "Y" or "N".')
        is_delivery = input("Is delivery required? ")

    while is_tuesday.lower() not in ['y', 'n']:
        print('Please answer "Y" or "N".')
        is_tuesday = input("Is it Tuesday? ")

    while used_app.lower() not in ['y', 'n']:
        print('Please answer "Y" or "N".')
        used_app = input("Did the customer use the app? ")

    total_price = num_pizzas * pizza_price

    if is_tuesday.lower() == 'y':
        total_price *= (1 - tuesday_discount)

    if is_delivery.lower() == 'y':
        total_price += delivery_cost if num_pizzas < 5 else 0

    if used_app.lower() == 'y':
        total_price *= (1 - app_discount)

    return total_price


def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas = input("How many pizzas ordered? ")
    is_delivery = input("Is delivery required? ")
    is_tuesday = input("Is it Tuesday? ")
    used_app = input("Did the customer use the app? ")

    total_price = calculate_price(int(num_pizzas), is_delivery, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")


if __name__ == "__main__":
    main()