#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

print ("Guessing Game");

import random

while True:
    y = random.randint(1, 9);
    a = int(input("Enter a number:\n"));
    if a > y:
        print("Too high");
        print("The number was " + str(y));
        if str(input("Continue or Exit?(C/E):\n")) == "C":
            continue
        else:
            break
    elif a < y:
        print ("Too low");
        print("The number was " + str(y));
        if str(input("Continue or Exit?(C/E):\n")) == "C":
            continue
        else:
            break
    elif a == y:
        print ("Exactly Right!");
        print("The number was " + str(y));
        if str(input("Continue or Exit?(C/E):\n")) == "C":
            continue
        else:
                break
