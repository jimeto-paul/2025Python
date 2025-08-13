#Written by Jimeto Onyeabo on 2nd December 2024.
#This piece of code calculates the circumference of a circle
#The equation for the circumference of a circle is pi * diameter

import math

import pi

radius = float(input("Enter in the radius value: "))
pi = math.pi
job = input("Enter in A to calculate area or C to calculate cirumference: ")

if job == "C" or job == "c":
    print("The circumference of the circle will be outputted as an integer ( rounded to the nearest whole number)")

#This program takes an input from the user (the radius) to calculate the circumference
#have to convert the input to integer
    radius = float(input("Enter in the radius: "))
#Calm lil calculating statement
    print("Calculating...")
#Variable that holds the value of circumference and makes it an integer
    circumference = float(radius*pi*2)

    print(f"The circumference of the circle is {circumference}")
elif job == "A" or job == "a":
    print("The formula for the area of a circle is 2pi(radius^2)")
    area = (pi * (radius*radius))
    print(area)
else:
    print("Re-run the program")

