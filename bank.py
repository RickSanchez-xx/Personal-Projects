def main():
    greeting = input("Hi please enter your greeting: ").strip().lower()
    if greeting.startswith("hello"):
        print("You'd get $0!")
    elif greeting.startswith("h"):
        print("You'd get $20!")
    else:
        print("Congratulations! You'd get $100!")


main()
