import random
secret_number = random.randint(1,10)
attempts = 3
while attempts >0:
    guess = int(input("guess the number (between 1 and 10):"))
    if guess <1 or guess >10:
        print("your guess is out of range. please guess a number between 1 and 10.")
        continue
    attempts -=1
    if guess <secret_number:
        print("too high. try again.")
    elif guess > secret_number:
        print("too high. try again.")
    else:
        print("congratulations! you guessed the correct number.")
        break
    
number = int(input("enter the number for which you want the multiplication table: "))
for i in range(1,11):
    result = number *i
    print(number,"x",i,"=",result)

def calculate_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in meters: "))
bmi = calculate_bmi(weight,height)
print("your bmi is:",round(bmi,2))
    
    
