#control flow is how computers decide what to do next
#conditional statements: if, elif, else
#comparision oporators
#logical operators
#loops
#control statements
age = 80

#if age is greater than 30, print message you are getting old

# if age >= 30:
#     print("You are getting older")
# elif age <= 17:
#     print("You are not getting in")
# else:
#     print("You are in your late teens or 20's")

# user_score = int(input("Please give your exam score (0-100) : "))
# print(user_score)
#
# if user_score >= 90:
#     print("A grade")
# elif user_score >= 80:
#     print("B grade")
# elif user_score >= 70:
#     print("C grade")
# else:
#     print("Fail")

# combine operators and comparison

age_1 = 32
has_id = True

# if age is greater than 18 and id they can come in else entry denied
# using and
# if age >= 18 and has_id:
#     print("Entry allowed")
# else:
#     print("Access denied")

# using or
# day = "Sat"
#
# if day == "Sat" or day == "Sun":
#     print("Its the weekend")
# else:
#     print("sadly its not the weekend")

light_on = False

#if light not on print turn off the light

# if not light_on:
#     print("turn light on")
# ask user for a number
#check if number is between the range 10 - 20
# user_num = int(input("Enter a number: "))
# print(user_num)
# if user_num >= 10 and user_num <= 20:
#     print("Between 10 and 20")
# else:
#     print("Outside range")


# loops - iterate over lists
# loop through a list
# fruits = ["banana", "apple", "pear"]
# #for loop
# for fruit in fruits:
#     print("I like", fruit)
#
# # loop within a range
# # range(5) gonna do it 5 times
# # range takes more than 1 input
# for index in range(5):
#     print(index)

# while loop - will continue while a condition is true / met

# num_2 = 1
# while num_2 < 5:
#     print(num_2)
#     num_2 += 1
#
# # print all even numbers from 2 to 20
# for index in range (2,21,2):
#     print(index)
#
# count = 10
# while count >= 1:
#     print(count)
#     count -= 1

# create a guessing game
# create a random number between 1 - 10
# ask user to guess a random number between 1 and 10
# use loop to continue until user gets it right

# import random
# random_number = random.randint(1,10)
# print(random_number)
# user_guess = 0
# while user_guess != random_number:
#     user_guess = int(input("Please give a guess: "))
#     if random_number < user_guess:
#         print("Your guess is too low")
#     elif random_number > user_guess:
#         print("Your guess is too high")
#     else:
#         print("Your guess is correct")
## dictionaries - are used to organise data as key value pairs
# how to declare
my_dictionary = {
    "first_name": "Joshna",
    "last_name": "Joshy",
    "address": "Los Angeles, CA"
}
# print(my_dictionary)
#
# # get a value using the key
#
# print("My name is ", my_dictionary["first_name"])
#
# # change value
# my_dictionary["first_name"] = "John"
# print(my_dictionary)
#
# # add a new key value
# my_dictionary["job"] = "Engineer"
# print(my_dictionary)
# # check if there is a key in dictionary
# print("do they have a job in the dictionary", "job" in my_dictionary)
#
# #list all keys
# print(my_dictionary.keys())
# #list all values
# print(my_dictionary.values())
#
# # loop through dictionaries
#
# for keys, values in my_dictionary.items():
#     print(keys, values)
#
# # deleting a key value pair
# del my_dictionary["job"]
# print(my_dictionary)
#
# # loop through just keys
#
# for key in my_dictionary:
#     print(key)
#
# # remove everything from dictionary
# my_dictionary.clear()
# print(my_dictionary)

customer = []
customer_input = ""
print("enter customer details (first name and last name) and type exit to quit")
while customer_input != "exit":
    first_name = input("Please give your first name: ")
    last_name = input("Please give your last name: ")
    customer.append({"first_name": first_name, "last_name": last_name})
    customer_input = input("if you want to exit type exit otherwise press enter to continue : ")
    if customer_input == "exit":
        print(customer)

for person in customer:
    first_name = input("Do you want to search for customer with first name yes or no (to search for customer with last name) ? ")
    if first_name == "yes":
        first_name = input("Please give the first name: ")
        if person["first_name"] == first_name:
            print(person)
        else:
            print("no customer found")

    else:
        last_name = input("Please give the last name: ")
        if person["last_name"] == last_name:
            print(person)
        else:
            print("no customer found")



