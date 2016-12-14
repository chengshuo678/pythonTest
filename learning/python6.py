# a guess game
import random


secret = random.randint(1,20)
print("I choose a number between 1 and 20 ,Please guess it")

count = 0
while 1:
    count = count + 1

    num = int(input())
    if secret == num:
        print("you are right,it is " ,str(num)," you make it in ",str(count)," times")
        break
    elif secret > num :
        print("your num is too low")
    else:
        print("your num is too high")
    print("take a guess again:")