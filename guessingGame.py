import random

tries = 5
rNo= random.randint(1,10)

print("number guessing game ")
while tries >0:
    print("attempt ",6-tries,":")

    b=int(input("enter your guess: "))
    if rNo == b :
        print("congratulation you won")
        break
    elif b > rNo:
        print("your number was too high")
        
    elif b < rNo:
        print("your number was too low")
        
    tries -=1

print(f"congratulation you lost , the correct number was {rNo} ")

