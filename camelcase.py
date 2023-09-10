def main():
    camelCase = input("Please enter your camelCase: ")

    print("snake_case: ", end="")

    for letter in camelCase:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")

    print()


main()
