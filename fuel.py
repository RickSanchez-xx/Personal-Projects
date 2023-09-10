def main():
    while True:
        fuel = input("Please enter your fuel level, MUST BE IN FRACTION!: ")
        try:

            num, denom = fuel.split("/")

            new_num = int(num)
            new_denom = int(denom)

            x = new_num / new_denom

            if x <= 1:
                break

        except(ValueError, ZeroDivisionError):
            pass

    percentage = x * 100

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(percentage)


main()
