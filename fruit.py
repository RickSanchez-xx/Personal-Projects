def main():
    fruits = {
        "apple": "100",
        "avocado": "80",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew melon": "50",
        "kiwi": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberry": "50",
        "cherry": "100",
        "tangerine": "50",
        "watermelon": "80"
    }
    item = input("Please enter your selection of fruit: ")
    print(item)

    for key in fruits:
        if key in item.lower():
            print("Calories: ", fruits[key])


main()
