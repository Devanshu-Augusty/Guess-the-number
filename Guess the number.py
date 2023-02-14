# Guess the number 
import random
print("---------------WELCOME GENIUS---------------")
print("\n============================================")
print("You will get 2 chances to Guess the number")
print("The number is between 1 and 10")
print("============================================\n")
n = random.randint(1,10)
x = int(input("Guess the number: "))
if(x == n):
    print("Nailed it, You're a GENIUS")
else:
    print("\nWrong Guess, 1 chance left\n")
    if(n == 10):
        print("Hint: Football Legend")
    elif(n % 2 == 0):
        print("Hint: Divisible by 2")
    elif(n % 3 == 0):
        print("Hint: Divisible by 3")
    elif(n == 5):
        print("Hand")
    elif(n == 7):
        print("Hint: Cricket Legend")
    elif(n == 1):
        print("Hint: You never got this position in your life")
    print("============================================")
    x2 = int(input("Guess the number: "))
    if(x2 == n):
        print("Correct, Nice one")
        print("============================================")
    else:
        print("\nWrong guess, The level of NOOBNESS is unbelievable")
        print("\nThe correct ans is:",n)
        print("\nBetter luck next time")
        print("============================================")
