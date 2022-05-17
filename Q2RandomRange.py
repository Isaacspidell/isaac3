#user inputs 2 random numbers, computer generates a random number between the two inputed numbers
import random
print("I will generate a random number between the 2 numbers you give me")
print("!Please Enter 2 Random Numbers!")
a=int(input())
b=int(input())
print(random.randint(a, b))