import random as r
import time as t

name = input("Type your Name please")
print("Hi there", name)
t.sleep(2)
print("in this Game i'm gonna think a positive integer number between 1 and 20 and you gonna try to guess it")
t.sleep(4)
print("you have no more then 10 tries until you find the right number")
t.sleep(3)
print("good luck")


def angelo():
    ran = r.randrange(1, 20)
    tries = 0
    count = 10
    usernum = 0
    while usernum != ran:
        try:
            usernum = int(input("type a number"))
            tries = tries + 1
            count = count - 1
            if usernum < ran:
                print("your number is lower")
            if usernum > ran:
                print("Your number is greater")
            if usernum == ran:
                print("congratulations.... you got it ")
                t.sleep(1)
                print("the right number was", ran)
                t.sleep(1)
                print("and your total tries are", tries)
            if count == 0:
                print("you are out of tries.... GAME OVER")
                break
        except:
            print("you should type an integer number")


angelo()
