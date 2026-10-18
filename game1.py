import random

number = random.randint(1 , 20)

print("guess the number between 1 to 20 and start the game!")

for i in range(3):
    mynumber = int(input("my number is:"))
    
    if mynumber == number:
        print("COOLL! IT'S CORRECT")
        break
    elif mynumber > number:
        print("oh no! it's bit greater than orignal")
    else:
         print("oops! it's less than orignal")
         
else:
    print(f"GAME OVER! ***** the number is this: {number}")