def main():
    innerVoice = str(input("Please enter you CapsLock txt here:")).lower()
    print(innerVoice)


main()


"""
def main():
    while True:
        word = input("Please enter all your words in UPPER-CASE!: ")
        try:
            if word.isupper():
                print("Success! All your words are UPPER-CASE")
                print(word, end="")
                break

            else:
                if word != word.isupper():
                    print("Aww You've failed!, Please try again!")
                    continue

        except IndexError:
            continue


main()
"""