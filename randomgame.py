import sys
import random

first = int(sys.argv[1])
second = int(sys.argv[2])
third = random.randint(first, second)
while True:
    try:
        guess = int(input("Input your number 1~10: "))
        if first <= guess <= second:
            if guess == third:
                print("Win!!!")
                break
        else:
            print('Hey bro, I said 1~10')
    except ValueError:
        print("Error: Input number")