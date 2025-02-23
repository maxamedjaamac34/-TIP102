

# Standard_Problem_Set_Version1


"""Problem 3: Catchphrase
Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below."""
def print_catchphrase(character):
    if character =="Pooh": 
        print("Oh bother!")
    elif character =="Tigger":
        print("TTFN: Ta-ta for now!")
    elif character =="Eeyore":
        print("Thanks for noticing me.")
    elif character =="Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
# character = "Pooh"
# print_catchphrase(character)

# character = "Mohamed"
# print_catchphrase(character)


#slicing 
list1 = [1,2,3,4,5]
print(list1[1:4])

"""Problem 4: Return Item
Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.
"""

print('problem4')
def get_item(items, x):
    for i in items:
        if x > len(items):
            return print("None")
        return print(items[x])
    

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 10
get_item(items, x)

#problem 5


"""Winnie the Pooh wants to know how much honey he has. Write a 
function sum_honey() that accepts a list of integers
 hunny_jars and returns the sum of all elements in the list. 
 Do not use the built-in function sum()."""
def sum_honey(hunny_jars):
    counter = 0
    for number in hunny_jars: # [2,3,4,5]
        counter += number
    print(counter)

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)


"""Problem 6: Double Trouble
Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.
"""
def doubled(hunny_jars):
    doubledjars = [i *2 for i in hunny_jars]

    return print(f"doubled jars are {doubledjars}")

hunny_jars = [1, 2, 3,5,6,10]
doubled(hunny_jars)


"""Problem 7: Poohsticks
Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold."""
print("Winnie the Pooh")
def count_less_than(race_times, threshold):
    count = 0
    for i in race_times:
        if i <threshold:
            count += 1
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4 #output: 3
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))




"""Problem 8: Pooh's To Do's
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:
"""
# Pooh's To Dos:
# 1. Task 1
# 2. Task 2
...

def print_todo_list(task):
    for i in range(len(task)):
        print(i +1, task[i])
print("Example Usage")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)




"""Problem 9: Pairs
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise."""

def can_pair(item_quantities):
    for i in item_quantities:
        if i%2 !=0:
            return print(i, False)
    return print(True)

print("Example Usage")

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1,3,2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)



"""Problem 10: Split Haycorns
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity."""

def split_haycorns(quantity):
    divisors = []
    for i in range(1,quantity+1):
        # print(i)
        if quantity % i ==0:
            divisors.append(i)
    return print(divisors)
print("Example Usage")

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)



"""Problem 11: T-I-Double Guh-ER
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it."""

def tiggerfy(s):
    relevant_letters = []
    for i in s.lower():
        if i in "tiger":
            relevant_letters.append(i)
    return print("".join(relevant_letters))

print('Example Usage')

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)



"""Problem 12: Thistle Hunt
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest."""

lst = [1,2,3,4]
for x in range(len(lst)):
    print(lst[x])
def locate_thistles(items):
    result_list  =[]
    for i in range(len(items)):
        if items[i] =="thistle":
            result_list.append(i)
    return print(result_list)

print("Example Usage")

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)


