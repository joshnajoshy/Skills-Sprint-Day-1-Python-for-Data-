# define variables

name = "Joshna"
age = 23
is_happy = True
my_float = 9.6

#print(age)

# reassign age

age = 30

#print(name)
#print("My age is", age)
#print(is_happy)
#print(my_float)

# exercise

favourite_food = "Roast Dinner"
birth_year = 2001
#print("I was born in", birth_year, "and my favourite food is a", favourite_food)

# using sys library

import sys

num_1 = 1
float_2 = 8.3
string_1 = "hi"
#print(num_1)
#print(type(num_1))
#print(sys.getsizeof(num_1))
#print(sys.getsizeof(float_2))
#print(sys.getsizeof(string_1))
#print(sys.getsizeof(is_happy))

#casting (type convertion)

my_number = 5
#can convert this integer into a float
my_float = float(my_number)
my_string = "123"
#convert string to integer
my_int = int(my_string)
#print(type(my_int))
#print(my_float)
#print(type(my_string))
#print(my_float)
#print(int(False))
float_3 = 3.14
num_3 = int(float_3)
string_3 = "60"
float_4 = float(string_3)
#print(num_3)
#print(float_4)
#print(int(3.9))
#print(float("45"))

# arithmatic and comparison operators

## add number
#print(5 + 5)
## divide number
#print(10//3)
## multiply number
#print(5*3)
## modulus
#print(10 % 3)

# using the input function(method)

# my_num_4 = int(input("Please enter a number to multiply by 2: "))
# print(my_num_4 * 2)

# sum 2 input numbers

# my_num_5 = int(input("Please enter a number: "))
# my_num_6 = int(input("Please enter another number: "))
# print("The sum is :", my_num_5 + my_num_6)

# check if 10 is greater than 5

# print(10 > 5)

# if(10 > 5):
   # print("True")
# else:
   # print("False")

# challenges

# num_1 = float(input("Please give a number to convert to a float : "))
# print(num_1)
# print(int(num_1/4))
#
# name = input("What is your name ? ")
# print("Hello", name)

height = int(input("Please give a height in meters: "))
width = int(input("Please give a width in meters: "))
area = height * width
print("Area of rectangle is", area)

