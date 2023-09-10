def main():
    menu = {
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

    result = 0

    while True:
        try:
            item = input("Please enter you choice from the menu: ").title()

            if item in menu:
                result += menu[item]
                print("Total: $", end="")
                print("{:.2f}".format(result))

        except EOFError:
            break
        print()


main()
