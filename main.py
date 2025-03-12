
# Part of case-study #2: Cost of goods, income and revenue
# Developers: Aliev Timur, Shostenko Artyom

import ru_local as ru


def clean_input(input_text):
    """Clearing text from extra spaces"""
    return input_text.strip()


def get_product_data():
    """Requesting product data from the user"""
    products = []

    while True:
        print(ru.ENTER_PRODUCT)
        user_input = input().strip()
        if user_input.lower() == ru.STOP:
            break
        print(ru.ENTER_EXPENSES)
        consignment_input = input().strip()
        try:
            name, quantity, price = user_input.split()
            quantity = int(quantity)
            price = float(price)
            total_revenue = quantity * price
            consignment_quantity, consignment_expenses = consignment_input.split()
            consignment_quantity = int(consignment_quantity)
            consignment_expenses = float(consignment_expenses)
            expenses = consignment_expenses / consignment_quantity
            total_expenses = expenses * quantity
            income = price - expenses
            total_income = total_revenue - total_expenses
            product = {
                'name': clean_input(name),
                'quantity': quantity,
                'price': price,
                'total_revenue': total_revenue,
                'item_expenses': expenses,
                'total_expenses': total_expenses,
                'income': income,
                'total_income': total_income
            }
            products.append(product)
        except ValueError:
            print(ru.INVALID_INPUT)

    return products


def display_report(products):
    """Outputs a report of items and their costs"""
    print(f"\n{ru.PRODUCT_REPORT}")
    revenue_all_products = 0
    income_all_products = 0

    for product in products:
        revenue_all_products += product['total_revenue']
        income_all_products += product['total_income']
        print(
            f"{product['name']} - {ru.QUANTITY}: {product['quantity']}, "
            f"{ru.COST_OF_ONE_ITEM}: {product['price']:.2f}, "
            f"{ru.TOTAL_PRODUCT_REVENUE}: {product['total_revenue']:.2f}\n"
            f"{ru.EXPENSES_ON_ONE_ITEM}: {product['item_expenses']:.2f}, "
            f"{ru.TOTAL_EXPENSES_ON_THE_PRODUCT}: {product['total_expenses']:.2f}\n"
            f"{ru.INCOME_FROM_ITEM}: {product['income']:.2f}, "
            f"{ru.TOTAL_PRODUCT_INCOME}: {product['total_income']:.2f}\n"
        )

    print(f"\n{ru.TOTAL_REVENUE}: {revenue_all_products:.2f}")
    print(f"\n{ru.TOTAL_INCOME}: {income_all_products:.2f}")


def main():
    """The main function"""
    products = get_product_data()
    display_report(products)


if __name__ == "__main__":
    main()
