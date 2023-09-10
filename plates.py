def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    check_valid = True
    counter = 0

    if len(s) < 2 or len(s) > 6:
        check_valid = False
        return check_valid

    if s[0].isdigit() or s[1].isdigit():
        check_valid = False
        return check_valid

    for char in s:
        if not char.isalnum():
            check_valid = False
            return check_valid

        if counter > 1 and char.isalpha():
            check_valid = False
            return check_valid

        if char.isdigit():
            counter += 1

        if counter == 1 and char == '0':
            check_valid = False
            return check_valid

    return check_valid


main()

