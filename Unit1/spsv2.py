
# Standard_Problem_Set_Version2

"""Problem 1: Batman
Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".
"""
def batman():
	return print(f"I am vengeance. I am the night. I am Batman!")
print("Example Usage:")

batman()


"""Problem 2: Mad Libs
Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".
"""
def madlib(verb):
	return print(f"I have one power. I never {verb}. - Batman")
print("Example Usage")

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)


'''Problem 3: Trilogy
Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."'''

def trilogy(year):

    if year ==2005:
        print("Batman Begins")
    elif year ==2008:
        print("The Dark Knight")
    elif year ==2012:
        print("The Dark Knight Rises")

    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")
	
print("Example Usage:")
year = 2008
trilogy(year)

year = 1998
trilogy(year)



"""Problem 4: Last
Implement a function get_last() that accepts a list of items items and returns the last item in the list. If the list is empty, return None."""

def get_last(items):
        
    if len(items) ==0:
        return print("None")
    return print(items[-1])
print(("Example Usage"))

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)


"""Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words."""

def concatenate(words):
    # words_combined = ""
    # for i in words:
    #     words_combined = "".join(words)
    #return print(words_combined)
    return print("".join(words))

print("Example Usage")

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)


"""Problem 6: Squared
Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list."""

def squared(numbers):
    squared_list = [x **2 for x in numbers]
    return print(squared_list)
print("Example Usage")

numbers = [1, 2, 3]
squared(numbers)


"""Problem 7: NaNaNa Batman!
Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.
"""
def nanana_batman(x):
    combine_na =[]
    for i in range(x):
        combine_na.append("na")
    return print(f"{''.join(combine_na)} batman!")
print("Example Usage")

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)


"""Problem 8: Find the Villain
Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd."""

def find_villain(crowd, villain):
    hiding_place = []
    for i in range(len(crowd)):
        if crowd[i] ==villain:
            hiding_place.append(i)
    return print(hiding_place)
        
print("Example Usage")

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)


"""Problem 9: Odd
Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums."""

def get_odds(nums):
    odds = []
    for i in nums:
        if i %2 ==1:
            odds.append(i)
    return print(odds)
            
print("Example Usage")

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)


"""Problem 10: Up and Down
Write a function up_and_down() that accepts a list of integers lst as a parameter. The function should return the number of odd numbers minus the number of even numbers in the list.
"""
def up_and_down(lst):
    odd_count = 0
    even_count = 0
    for i in lst:
        if i %2 ==0:
            even_count +=1
        else:
            odd_count +=1
    return print(odd_count -even_count)
print("Example Usage")

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)


"""Problem 11: Running Sum
Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman has stopped each month in Gotham City. The function should modify the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). You must modify the list in place; you may not create any new lists as part of your solution.
"""
def running_sum(superhero_stats):
    for i in range(1, len(superhero_stats)):
        superhero_stats[i] += superhero_stats[i-1]
    return print(superhero_stats)

print("Example Usage")

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)


"""Problem 12: Shuffle
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].
"""
def shuffle(cards):
   
    shuffled_list = []
    first_half_length = len(cards)//2

    for i in range(first_half_length):
        shuffled_list.append(cards[i])
        shuffled_list.append(cards[i+first_half_length])
    print(shuffled_list)

print("Example Usage")

# lst = [1,2,3,4,5,6,7,8,9,10]
# shuffled_list = []
# first_half_length = len(lst)//2

# for i in range(first_half_length): #0,1,2,3,4
#     shuffled_list.append(lst[i])
#     shuffled_list.append(lst[i+first_half_length])
# print(shuffled_list)



cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)