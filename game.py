import random
import contextlib


def main():
    lvl = get_level()
    generate_integer(lvl)


def get_level():
    while True:
        with contextlib.suppress(ValueError):
            level = input("Please enter the level you'd wish to start from: ")
            lvl = int(level)

            if lvl in [1, 2, 3]:
                return lvl
            else:
                raise ValueError


def generate_integer(lvl):
    player_score = 0

    for i in range(1, 11):
        if lvl == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif lvl == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)

        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        player_try = 1
        while player_try <= 3:
            try:
                user_in = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                player_try += 1
                continue
            else:
                answer = x + y
                if user_in == answer:
                    player_score += 1
                    break
                else:
                    print("EEE")
                    if player_try == 3:
                        print(f"{x} + {y} = {answer} ")
                        player_try += 1

                print()
                print(f"Score: {player_score}")


if __name__ == "__main__":
    main()
