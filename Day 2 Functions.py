# functions - a reusable block of code that we can use again
# DRY - don't repeat yourself
# functions can be triggered by user in front end
# def name_function (parameter):
#       return something (optional)
# print function print("Hello")
# def hello():
#     print("Hello World")
#
# hello() - not good usage of a function because you can do the same with print("Hello")

## function with arguments
# def add(num_1, num_2):
#     print(num_1 + num_2)
#
# add(2,4)
## print vs return
# print() -> displays something on the screen for the user
# return -> gives a value back to the caller so it can be stored or reused
# def add_and_print(a,b):
#     print(a + b)
#
# def add_and_return(a,b):
#     return a + b
#
# result = add_and_print(10,20) # >> no value as print doesnt give an output to store
# result_2 = add_and_return(10,20)
#
# print(result) # >> prints none because print cannot assign to a variable
# print(result_2)

# scope in functions -> global scope and local
# global -> can modify outside the function, exists across our program
# local -> defined inside the function and cannot modify outside

# def set_name():
#     name = "Joshna"
#     print(name) # -> this works cause variable is local scope
# print(name) # -> because variable doesn't exist outside function
#
# set_name() # -> call function to print name

# def change_name():
#     global global_name
#     global_name = "Joshna"
#
# global_name = "JJ"
# change_name()
# print(global_name)
# # ->  Joshna

# 1- My First Python Function

# def my_first_function(word):
#     print("I love", word)
#
# my_first_function("coding")
#
# # 2- Function tripler()
#
# def tripler(num_1):
#     return num_1 * 3
#
# result_1 = tripler(5)
# result_2 = tripler(6)
# result_3 = tripler(10)
#
# print(result_1)
# print(result_2)
# print(result_3)
#
# # 3- Greeter MVP
#
# def greet(name):
#     return "Hello " + name
#
# greeting_1 = greet("Joshna")
# print(greeting_1)
#
# # 4- Even or Odd? MVP
#
# def is_even(num_2):
#     if num_2 % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# check_number_is_even = is_even(5)
# print(check_number_is_even)
#
# # 5- Word Multiplier MVP
#
# def repeat_word(word,times):
#     return (word + " ") * times
#
# repeated_word = repeat_word("Python", 5)
# print(repeated_word)
#
# # 6- Factorial (Stretch) MVP
#
# def factorial(n):
#     total = 1
#     for index in range(1, n + 1):
#         total *= index
#     return total
#
# calculate_factorial = factorial(5)
# calculate_factorial_2 = factorial(8)
# print(calculate_factorial)
# print(calculate_factorial_2)

# lambda expressions
# lambda arguments: expression

# def sum(a,b):
#     return a + b
#
# sum_lambda = lambda a, b: a + b # -> same way to write a function
#
# print(sum_lambda(1, 2))
# print(sum(2,3))
#
# import math
#
# def circle_perimeter(radius):
#     return 2 * math.pi * radius
#
# def circle_area(radius):
#     return math.pi * radius ** 2
#
# circle_perimeter_lambda = lambda r: 2 * math.pi * r
# circle_area_lambda = lambda r: math.pi * r ** 2
#
# def triangle_area(a, b, c):
#     s = (a + b + c) / 2
#     return math.sqrt(s * (s - a) * (s - b) * (s - c))
#
# # convert to lambda syntax
# triangle_area_lambda = lambda a , b , c: math.sqrt(((a + b + c)/2) * ((a + b + c)/2) - a) * (((a + b + c)/2) - b) * (((a + b + c)/2) - c)
#
# # lambda function in practice
# # lambda functions can take multiple arguments
# # they cannot contain multiple expressions or statements
# # simple operations
#
# add = lambda a, b, c: a + b + c
#
# def multiplier(n):
#     return lambda x: x * n # -> can use it like this as well
#
# doubler = multiplier(3)
# tripler = multiplier(3)
# print(doubler(3))
# print(tripler(3))

## map, filter and reduce

# Map -> apply a function to each element

# numbers = [1,2,3]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)
#
# # Filter - filter elements based on a condition

# numbers = range(1,10)
# evens = list(filter(lambda x: x % 2 == 0, numbers)) # -> because returning list and not a single value
# odds = list(filter(lambda x: x % 2 != 0, numbers))
# print(evens) # -> returns a list of all even numbers
# print(odds)
#
# # Reduce -> "reduces" a list to a single value (require an import for this, functools)
# # List comprehensions will often provide a more Pythonic alternative

# from functools import reduce
# numbers = [1,2,3]
# sum_all = reduce(lambda a, b: a + b, numbers)
# product_all = reduce(lambda a, b: a * b, numbers) # -> can also input list directly [2, 3, 3] instead of having numbers
# print(sum_all)
# print(product_all)

## challenges

# num_list = [2, 5, 7, 32, 100, 9, 56, 74, 97, 22, 13, 80]
# even_nums = list(filter(lambda x: x % 2 == 0, num_list))
# # print(even_nums)
# multiply_three = list(map(lambda x: x * 3, num_list))
# # print(multiply_three)
# from functools import reduce
# sum_nums = reduce(lambda x, y: x + y, num_list)
# print(sum_nums)












