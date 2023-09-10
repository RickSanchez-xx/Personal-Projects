import random

while True:
    try:
        lvl = int(input("Please enter your level of desire: "))

        if lvl < 0:
            break

    except:
        pass

    ran_num = random.randint(1, lvl)

    while True:
        try:
            gss = int(input("Please enter your guess: "))

            if gss > 0:
                if gss < ran_num:
                    print("Too Small!")

                elif gss > ran_num:
                    print("Too large!!")

                else:
                    print("This is perfect you win!!")
                    break

        except:
            pass
