import emoji


def main():
    users = input("Please enter your wished emoji: ")

    output = emoji.emojize(users)

    print("This is the output: ", output)
    print(emoji.emojize(":thumbs_up:"))


main()
