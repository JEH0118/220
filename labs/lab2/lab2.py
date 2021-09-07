


import math
"""
Name: Jonathan Helfgott
<lab2>.py
Problem: math issues solved in python
"""


def sum_of_threes():
    sum = eval(input("What is  your upper bound number?:"))
    output = 0

    for i in range(3, sum + 1, 3):
        output = output + i
    print(output)
sum_of_threes()


def multiplication_table():
    for i in range(1,11):
        print(i, end="\t")
    print()

    for x in range(1,11):
        print(x,":", end="\t")
        for y in range(1,11):
            print(x*y, end="\t")
        print()
multiplication_table()

def traingle_area():
    length_a= eval(input(" length of side A?"))
    length_b = eval(input(" length of side B"))
    length_c =eval(input("length of side C"))
    side = (length_a+length_b+length_c)/2
    area = math.sqrt(side*(side-length_a)*(side-length_b)*(side-Length_c))
    print("The area of the triangle is", area)
traingle_area()

def sumSquares():
    lower_bound=eval(input("what is  lower bound?"))
    upper_bound=eval(input("what is  upper bound"))
    for i in range(lower_bound,upper_bound):
        x = l**2 +i**2 +u**2
        print(x)
sumSquares()

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = 1

for i in range(1, exponent + 1):
    power = power * number






