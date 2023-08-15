# kaggle tutorials
# The ZEN of Python: Readability counts. Explicit is better than implicit!

# Functions

# def least_diff(a,b,c):
#       """Return the smallest diff bet any 2 numb
#       present in the function arguments
#       (1, 5, -5)
#       4
#       """
#
#       diff1 = abs(a -b)
#       diff2 = abs(b - c)
#       diff3 = abs(c - a)
#       return min(diff1, diff2, diff3)
#
# print(least_diff(20, 15, 7))
#
# help(least_diff)
#
# #functions applied to Functions
#
# def mult_five(x):
#       return x*5
#
# def call(fn, arg):
#       """Call fn on arg"""
#       return fn(arg)
#
# def squared_call(fn, arg):
#       """Call fn on the result of calling fn on arg"""
#       return fn(fn(arg))
#
# print(
#       call(mult_five,1),
#       squared_call(mult_five,1),
#       sep = '\n'
# )

# def mod_5(x):
#     return x % 5
#
#
# numbers = [5, 12, 27]
#
# print(
#       f'The biggest number in the list is: {max(numbers)}', '\n'
#       f'The biggest module in the list is: {max(numbers, key=mod_5)}')
#
#
# def round_to_two_decimals(x):
#     """"Return x rounded to 2 decimals places
#     3.1415 -> 3.14
#     """
#     return round(x, 2)
#     pass
#
#
# print(round_to_two_decimals(5.2264))
# help(round)


# def to_smash(total_candies, friends=3):
#     """Return the number of leftover candies by value of friends
#         to_smash(22)
#          1"""
#     return total_candies % friends
#
#
# print(to_smash(91, 3))

# Booleans and Conditionals

#
# def can_run_for_president(age):
#     """Can you run for president in the US based on age?"""
#     return age >= 35
#
#
# print(f'Can I run for president?')
# print(can_run_for_president(int(input(f'Insert your age: ')))

# def is_odd(x):
#     return x % 2 == 0
#
#
# print(is_odd(5))

# num = "0123456789-1-2-3-4-5-6-7-8-9"
# x = input(f'Please write a number: ')
# for i in x:
#     if i not in num:
#         print(f'Please, write a number!!')
#         exit()
#     else:
#         x = int(x)
#
#         """This for is used to see if the value given by user is
#         a number or not. And if it is it changes it from str to int,
#         so it can be then compared to 0"""
#
# if x == 0:
#     print(f'The value is 0')
# elif x > 0:
#     print(f'The value {x} is positive')
# elif x < 0:
#     print(f'The value {x} is negative')
# else:
#     print(f'Please write a number: ')
#
# if x <= 0:


# def sign(x):
#     if x > 0:
#         return 1
#     elif x < 0:
#         return -1
#     else:
#         return 0
#
#
# print(sign(0))


# def to_smash(total_candies):
#     """Return the number of leftover candies that must be smashed after distributing
#     the given number of candies evenly between 3 friends.
#     to_smash(91)
#     1
#     """
#     # if total_candies == 1:
#     #     print(f'Splitting {total_candies} candy')
#     # else:
#     #     print("Splitting", total_candies, "candies")
#     # return total_candies % 3
#
#     print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
#
#
# to_smash(91)
# to_smash(1)
#
#
# def concise_is_negative(number):
#     return number < 0
#
#
# print(concise_is_negative(-1))
#
#
# def wants_all_toppings(ketchup, mustard, onion):
#     """Return whether the customer wants "the works" (all 3 toppings)
#     """
#     return ketchup and mustard and onion
#
#
# def exactly_one_topping(ketchup, mustard, onion):
#     """Return whether the customer wants exactly one of the three available toppings
#     on their hot dog.
#     """
#     return (ketchup + mustard + onion) == 1

# LISTS

# primes = [2, 3, 5, 7]
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#
# list_of_lists = [[1, 2, 3], [1, 2, 3]]
#
# print(planets[0], planets[3], planets[:3], planets[:], sep=' ', end='\n')

# def losing_team_captain(teams):
#     """Given a list of teams, where each team is a list of names,
#      return the 2nd player (captain) from the last listed team.
#     The last item in a list L can be selected with L[-1].
#     The first item in the first sublist would be selected as L[0][0]"""
#
#     return teams[-1][1]


# def purple_shell(racers):
#     """Given a list of racers, set the first place racer (at the front of the list) to last
#         place and vice versa."""
#     racers[0], racers[-1] = racers[-1], racers[0]
#     return racers
#
#
# racers = ["Mario", "Bowser", "Luigi"]
# print(purple_shell(racers))
# print(len(racers))
#
# a = [1, 2, 3]
# b = [1, [2, 3]]
# c = []
# d = [1, 2, 3][1:]
#
# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d), d)
#
# party_attendees = ['Adela', 'Ana', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
#
#
# def fashionably_late(arrivals, name):
#     """Given an ordered list of arrivals to the party and a name,
#      return whether the guest with that name was fashionably late.
#     """
#     if arrivals > (len(party_attendees) / 2) and arrivals < len(party_attendees):
#         return f'{name} is fashionably late'
#     else:
#         pass
#
#
# print(fashionably_late(7, 'Adela'))

# for i in party_attendees:
#     print(i)
# print(len(party_attendees))
# len = len(party_attendees)
# print(type(len))
#
# food = ['pizza', 'hamburger', 'beef']
# for i in food:
#     print(i)

# Loops and List Comprehensions

# for loops
#
# # itteration - list
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for planet in planets:
#     print(planet, end=' ')  # prints all in the same line
# print(end='\n')
#
# # itteration - tuple
# multiplicands = (2, 2, 2, 3, 3, 5)
# for mult in multiplicands:
#     print(mult, end=' ')
# print(end='\n')
#
# # itteration string
# s = 'steganograpHy: the practicE of conceaLing a file, mess, img, video within another fiLe, mess, img, video. WORLD'
# for char in s:
#     if char.isupper():
#         print(char, end='\n')
#
# for i in range(5):
#     print("Doing important work. i =", i)
#
# # while loops
#
# i = 0
# while i <= 10:
#     print(i, end=' ')
#     i += 1  # increase the value if i by 1
# print(end='\n')
#
# # List comprehensions
#
# square = [n**2 for n in range(10)]
# print(square, end='\n')
#
# nums = [-1, 2, -5]
#
#
# def count_negatives(nums):
#     return len([num for num in nums if num < 0])
#
#
# print(count_negatives(nums))


def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False


print(has_lucky_number([7, 5, 7, 6]))


def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])


print(has_lucky_number([7, 5, 7, 6]))
help(any)


def elementwise_greater_than(num, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise.

    elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [ele > thresh for ele in num]


print(elementwise_greater_than([1, 2, 3, 4], 2))


def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    #  Iterate over all indices of the list, except the last one
    # for i in range(len(meals)-1):
    #     if meals[i] == meals[i+1]:
    #         return True
    # return False

    return [meals[i] == meals[i+1] for i in range(len(meals)-1)]


print(menu_is_boring([1, 1, 3, 5, 5, 6]))

# Strings and Dictionaries

a = ''
b = "it's ok"
c = 'it\'s ok'
d = """hey"""
e = '\n'
print(len(a), len(b), len(c), len(d), len(e))
print(bool(a))


def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
     """
    return len(zip_code) == 5 and zip_code.isdigit()


print(is_valid_zip(f'45876'))



#
# def word_search(doc_list, keyword):
#     """
#     Takes a list of documents (each document is a string) and a keyword.
#     Returns list of the index values into the original list for all documents
#     containing the keyword.
#
#     Example:
#     doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
#     word_search(doc_list, 'casino')
#     [0]
#     """
#     # list to hold the indices of matching documents
#     indices = []
#     # Iterate through the indices (i) and elements (doc) of documents
#     for i, doc in enumerate(doc_list):
#         tokens = doc.split()
#         normalized = [token.rstrip('.,').lower() for token in tokens]
#         if keyword.lower() is normalized:
#             indices.append(i)
#     return indices
#
#
# print(word_search("The Learn Python Challenge Casino. Casinoville", 'casino'))
#
#
# def multi_word_search(documents, keywords):
#     """
#     Takes list of documents (each document is a string) and a list of keywords.
#     Returns a dictionary where each key is a keyword, and the value is a list of indices
#     (from doc_list) of the documents containing that keyword
#
#     doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
#     keywords = ['casino', 'they']
#     multi_word_search(doc_list, keywords)
#     {'casino': [0, 1], 'they': [1]}"""
#     keyword_to_indices = {}
#     for keyword in keywords:
#         keyword_to_indices[keyword] = word_search(documents, keyword)
#     return keyword_to_indices
#
#
# print(multi_word_search("The Learn Python Challenge Casino. Casinoville", 'casino'))

# Working with External Libraries

# Imports

# import math
#
# # Three tools for understanding strange objects
#
# #1: type() (what is this thing?)
# print(type(math))
#
# # 2: dir() (what can I do with it?)
# print(dir(math))
#
# # 3: help() (tell me more)
#
# print(help(math))
#
# print(math.pi)
# print(math.log(32, 2))
