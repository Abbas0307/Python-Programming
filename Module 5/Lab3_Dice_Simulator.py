# MODULE 5 - LAB 3: Dice Simulator using random module

import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("===== DICE SIMULATOR =====")

    while True:
        choice = input("Press Enter to roll the dice or type Q to quit: ").strip().upper()

        if choice == "Q":
            print("Thanks for playing!")
            break

        result = roll_dice()
        print("You rolled:", result)


if __name__ == "__main__":
    main()
