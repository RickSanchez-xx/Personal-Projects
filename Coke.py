def main():
    amount_due = 50

    while amount_due < 0:
        print("Hello, Please insert $50c to get a cold coke!", + amount_due)

        coin = int(input("Amount Due: "))

        if coin in [25, 10, 5]:
            amount_due -= coin

        total = abs(amount_due)

        print("Changed owned: ", total)


main()
