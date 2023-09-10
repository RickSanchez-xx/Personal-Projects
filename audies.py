import inflect

p = inflect.engine()

names = []

while True:

    try:

        name = input("Please enter your name: ").title()
        names.append(name)

    except EOFError:
        print()

        break

output = p.join(names)
print("Adieu, adieu, to " + output)
