# what are lists ?
# mutable and allow duplicate values, multiple values stored in one variable
## declare a list : with [ ]

coaches_list = ["Ollie", "Sam", "Luke", "Bex"]

# to know length of list
#
# print(len(coaches_list))
#
# # to call an item from a list
#
# print(coaches_list[0])
#
# # up to the third element
# #slice
# print(coaches_list[:3])
#
# # first 2 elements
# print(coaches_list[0:2])
#
# # check if value in list
#
# print("Ollie" in coaches_list)
#
# # change value of item in list
#
# coaches_list[1] = "Jake"
# print(coaches_list)
#
# # change list with multiple items this adds these people not change value of 1 and 2
# coaches_list[1:2] = ["John", "Smith"]
# print(coaches_list)
#
# # print the last coach using negative indexing
# print(coaches_list[-1])
#
# coaches_list[4:5] = ["Steve", "Jose"]
# print(coaches_list[-1])
#
# # print out the word loco from variable
#
# challenge_1 = "cool"
# # with negative indexing
# print(challenge_1[-1] + challenge_1[-2] + challenge_1[-4] + challenge_1[-3])
# # or print(challenge_1[-1:-3:-1] + challenge_1[0:2]
#
# # list methods
# num_list = [10,2,5,7,20,76]
#
# # insert 450 in the second position
#
# num_list.insert(2,450)
# print(num_list)
#
# # remove first item in list
# num_list.pop(0)
# print(num_list)
#
# # remove last item in list
# num_list.pop()
# print(num_list)
#
# # sort list by largest to smallest
# num_list.sort(reverse=True)
# print(num_list)
#
# # add 45 to the end of the list
# num_list.append(45)
# print(num_list)

## slicing
#syntax: List[initial: end : index step]

num_list_2 = [10,20,30,40,50,60]

# defaults to 0 - end with no step
# print(num_list_2[::])
# #[::] not giving anything to initial end
# # negative slicing
# print(num_list_2[-6::])
#
# #initial inclusive and exclusive
# print(num_list_2[1:4])
# #start at 1 and end at 4
#
# # create a new list of numbers between 1 - 10
# # output we want is a new list that steps by 2 each time starting at the second position
# num_list_3 = [1,2,3,4,5,6,7,8,9,10]
# print(num_list_3[1::2])
#
# ## Array - can only have a specific type adn has to be the same type, array has different type codes
# import array as arr
# nums = arr.array("i", [1,2,3,4,5,6,7,8,9,10])
# # i = integer
# # accessing the array element
# print("First element:", nums[0])
#
# # casting list into an array
# num_list_4 = [1,2,3,4,5,6,7,8,9,10]
# num_arr = arr.array("i", num_list_4)
#
# #slicing arrays
# print(num_arr[2:5])
#
# # changing elements
# num_arr[0] = 20
# print(num_arr)
#
# # create empty arrays
# numbers = arr.array("i")
# # adding arrays
# numbers = num_arr + nums
# print(numbers)
#
# # delete an item
# del number[2]
# print(numbers)

# create a multiplication table for 5 times table using only lists and list methods (no loops) going to 12

fives = [5,10,15,20,25,30,35,40,45,50,55,60]

print(fives)
print(fives.pop(2))
print(fives)
# fives.remove(25)
# print(fives)
fives.insert(2, 15)
print(fives)
print(fives.pop())
print(fives)
print(fives.pop(4))
print(fives[4])
print(fives.index(40))
print(fives.count(5))

times_five = []
times_five.append(5*0)
times_five.append(5*1)
times_five.append(5*2)
times_five.append(5*3)
times_five.append(5*4)
times_five.append(5*5)
times_five.append(5*6)
times_five.append(5*7)
times_five.append(5*8)
times_five.append(5*9)
times_five.append(5*10)
times_five.append(5*11)
times_five.append(5*12)

print(times_five)
# remove one value


