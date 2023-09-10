def main():
    grocery = {}

    while True:
        try:
            item = input("Please enter your grocery list here: ").lower()

            if item in grocery:

                grocery[item] += 1

            else:
                grocery[item] = 1

        except EOFError:
            for key in sorted(grocery.keys()):
                print(grocery[key], key.upper())

            break


main()
