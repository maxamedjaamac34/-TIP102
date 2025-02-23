# def nanana_batman(x):
#     if x == 0:
#         return " Batman!"
#     elif x > 0:
#         return "Na" + nanana_batman(x-1)
    
# x = 0

# print(nanana_batman(x))


# Standard_Problem_Set_Version1

"""Problem 1: Reverse Sentence
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string."""

def reverse_sentence(sentence):
    _split = sentence.split()

    return " ".join(_split[::-1])


sentence = "tubby little cubby all stuffed with fluff"
#print(reverse_sentence(sentence))


"""Problem 2: Goldilocks Number
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number."""


def goldilocks_approved(nums):

    if len(nums) <= 2:
        return -1
    minimum, maximum = min(nums), max(nums)
    for i in nums:
        if i != minimum and i != maximum:
            return i

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))



"""Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. Return a new list of the elements of hunny_jar_sizes in the order in which they were removed."""

def delete_minimum_elements(hunny_jar_sizes):
    result = []
    while hunny_jar_sizes:
        minimum = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(minimum)
        result.append(minimum)
    return print(result)

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)


"""Problem 4: Sum of Digits
Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits."""

def sum_of_digits(num):
    result = 0
    string = str(num)
    for i in string:
        result +=int(i)
    return print(result)


num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)


"""Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations."""
print("here")
def final_value_after_operations(operations):
    tigger = 1
    for i in operations:
        if i in ["trouncy", "pouncy"]:
            tigger -=1
        elif i in ["bouncy", "flouncy"]:
            tigger +=1
        else:
            continue
    return print(tigger)


operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)


"""Problem 6: Acronym
Given an array of strings words and a string s, implement a function is_acronym() that returns True if s is an acronym of words and returns False otherwise.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "pb" can be formed from ["pooh"", "bear"], but it can't be formed from ["bear", "pooh"]."""

def is_acronym(words, s):
    string = ""
    for i in words:
        string +=i[0] #crm
    return print(s==string)


words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)


"""Problem 7: Good Things Come in Threes
Write a function make_divisible_by_3() that accepts an integer array nums. In one operation, you can add or subtract 1 from any element of nums. Return the minimum number of operations to make all elements of nums divisible by 3."""
#did not complete this one. 
# we were thinking about minimum operations to each number in the list. 
# def make_divisible_by_3(nums):
#     operations = 0
    
#     for i in nums:
#         reminder = i%3
#         if reminder !=0:



# nums = [1, 2, 3, 4] #3
# make_divisible_by_3(nums)

# nums = [3, 6, 9]
# make_divisible_by_3(nums)