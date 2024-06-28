#Practice Notes
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area



sword_length = 1.0
spear_length = 2.0

# don't touch above this line
sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)


# don't touch below this line
print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")



# "In place" operators function some examples -=, +=, **, *= 
def get_hurt(current_health, damage):
    current_health -= damage
    return current_health


#Built in "int" function converts binary string to an integer.
#Binary base is 2 
def body_parts(num_heads, num_arms, num_fingers):
    num_heads = int(num_heads, 2)
    num_arms = int(num_arms, 2)
    num_fingers = int(num_fingers, 2)
    return num_heads, num_arms, num_fingers

#Comparison Operators 
 # " " are not needed just added for readability 
"<"
">"
"<="
">="
"=="
"!="

#If statements
def print_status(player_health):
    if player_health <= 0:
        print("dead")

        
    if player_health >= 0:
        print("status check complete")

# IF ELSE STATEMENT EXAMPLE
def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"
    
# EXAMPLE 2 
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
         return "You are not the highest scoring player!"

# EXAMPLE 3
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
        

# Boolean Logic (Logical operators "and" "or" with "if" "elif" "else")
def does_attack_hit(attack_roll, armor_class):
    if attack_roll != 1 and attack_roll >= armor_class or attack_roll == 20:
        return True
    else:
        return False
    
def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False
    if player_power > enemy_defense:
        advantage = True
    elif player_power < enemy_defense:
        disadvantage = True
    else:
        evenly_matched = True
    return advantage, disadvantage, evenly_matched


#Complete the has_enough_gas function. Do some Pythonic math with the miles_one_way and miles_per_gallon variables to determine how many gallons are needed for Tyler to get to work AND make it back home after he gets off work. 
#Assign the result to a gallons_needed variable. Return True if there are at least enough gallons in the tank based on the gallons_needed variable, and False otherwise.
def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
    gallons_needed = True
    if miles_one_way * 2 / miles_per_gallon <= gallons_in_car:
        return gallons_needed
    else:
        return False
    
# "FOR LOOP" Prints numbers 0-99
def print_numbers():
    for i in range(0, 100):
        print (i)


# Finding the sum of numbers in a for loop starting with 1. 
# Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:
# number_sum(5) -> 1+2+3+4+5 -> 15
def number_sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

# Prints counting down from 20-1 (start -end)
def count_down(start, end):
    for i in range(start, end, -1):
        print(i)

# sum of numbers 0+1+2+3+4+5
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, +2):
        total += i
    return total


# Find the factorial of a number. factorial is 4! = 4 * 3 * 2 * 1 = 24

def factorial(num):

    f = 1 
 
    for i in range(1, num + 1):
        f *= i
    return f
        

# Calculates Square of the numbers in the for loop
def calculate_squares(start, end):
    for i in range(start, end):
        print(f"{i} squared = {i ** 2}")


# Modulo "%" is used to find the remainder. DEF is finding prime numbers
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# List Function 

def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]

def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")


# Lists can include Strings, numbers(Intergers, Floats), Boolean and can be included in same lists. 
# Each item in the list has an index that refers to its spot
# Example 

names = ["Bob", "James", "Katy"]

# Index 0: Bob
# Index 1: James
# Index 2: Katy

# The length of a List can be calculated using the len() function.

fruits = ["apple", "banana", "pear"]
length = len(fruits)
# Prints: 3


# Accesing items in the list

def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]

# To change items in the list you can do so by giving an index.
# Example

def smelt_ore():
    inventory = ["Healing Potion", "Iron Ore", "Bread", "Shortsword"]
    print(f"Inventory: {inventory}") # Will print inventory 
    inventory[1] = "Iron Bar" # Applies changes to inventory by calliing index
    return inventory


# Adding items to my list using .append() method

cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

# Removing items from the list are done using .pop()

vegetables = ["broccoli", "cabbage", "kale", "tomato"];
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'

# Complete function so that it returns the length of the inventory list minus 1.

def get_last_index(inventory):
    length = len(inventory)
    return length - 1


# Remember that we can iterate over all the elements in a list using a loop. For example, the following code will print each item in the sports list.

for i in range(0, len(sports)):
    print(sports[i])

# Our players need a way to see how many copies of a specific item they have within their inventory!
# Let's finish the get_item_counts function. Within the loop, check if the items are a Potion, Bread, or Shortsword, then add up how many there are of each by incrementing the potion_count, bread_count and shortsword_count variables respectively.

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1


    return potion_count, bread_count, shortsword_count


# In my opinion, Python has the most elegant syntax for iterating directly over the items in a list without worrying about index numbers. If you don't need the index number you can use the following syntax:
# NO INDEX SYNTAX
# Use when you dont need the index(position in numbers) you just need the value.

trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple


# Example of "no index" "no range" syntax


def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for items in items:
        if items == "Leather Scraps":
            return True   

    # don't touch below this line

    return found


# Float functions finding the max value

def find_max(nums):
    max_so_far = float("-inf")
    for i in range(0, len(nums)):
        if nums[i] > max_so_far:
            max_so_far = nums[i]
    return max_so_far

# Float function finding the lowest number in list.
def find_min(nums):
    min = float("inf")

    for i in range(len(nums)):
        if nums[i] <= min:
            min = nums[i]
    return min

# Using the modulo % operator and the .append() method. 

def get_odd_numbers(num):
    odd_numbers = []
    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers


# Slicing lists syntax example: my_list[ start : stop : step ]

scores = [50, 70, 30, 20, 90, 10, 50] 
print(scores[1:5:2])
# Prints [70, 20]
# The above reads as "give me a slice of the scores list from index 1, up to but not including 5, skipping every 2nd value. All of the sections are optional.

# Splits the list of players into two seperate teams using slice with step values

def split_players_into_teams(players):
    even_team = players[0::2]
    odd_team = players[1::2]
    return even_team, odd_team

# You can also omit various sections ("start", "stop", or "step"). For example, numbers[:3] means "get all items from the start up to (but not including) index 3". numbers[3:] means "get all items from index 3 to the end".

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

# Negative indices count from the end of the list. For example, numbers[-1] gives the last item in the list, numbers[-2] gives the second last item, and so on.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:] # Gives [7, 8, 9]

# Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:
# First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
# Next, return a slice of the champions list that starts at the beginning of the list and ends with the third champion from the end (inclusive).
# Last, return a slice of the champions list that only includes the champions in even numbered indexes.

def get_champion_slices(champions):
    return champions[2:], champions[:-2], champions[::2]

# Input:
# ['Thrundar', 'Morgate', 'Gandolfo', 'Thraine', 'Norwad', 'Gilforn']

# Expecting:
# (['Gandolfo', 'Thraine', 'Norwad', 'Gilforn'], ['Thrundar', 'Morgate', 'Gandolfo', 'Thraine'], ['Thrundar', 'Gandolfo', 'Norwad'])


# Concatenating two lists (smushing them together) is easy in Python, just use the + operator.

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    fav_list = favorite_weapons + favorite_armor + favorite_items
    return fav_list

# Checking whether a value exists in a list is also really easy in Python, just use the in keyword.

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]


    if weapon in top_weapons:
        return True
    else:
        return False
    

# Python has a built-in keyword del that deletes items from objects. In the case of a list, you can delete specific indexes or entire slices.


    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []

# Delete the last two strongholds from the list
# Return the new trimmed-down list

def trim_strongholds(strongholds):
    del strongholds[0] # Delete the first stronghold from the list
    del strongholds[-2] # Delete the last two strongholds from the list * Delete Furthest from end first to on delete the original end list items *
    del strongholds[-1] # Delete the last two strongholds from the list
    return(strongholds)


# Tuples are collections of data that are ordered and unchangeable. You can think of a tuple as a List with a fixed size. Tuples are created with round brackets:

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True

# Tuples are often used to store very small groups (like 2 or 3 items) of data. For example, you might use a tuple to store a dog's name and age.

dog = ("Fido", 4)

# There is a special case for creating single-item tuples. You must include a comma so Python knows it's a tuple and not regular parentheses.

dog = ("Fido",)

# Because Tuples hold their data, multiple tuples can be stored within a list. Similar to storing other data in lists, each tuple within the list is separated by a comma.
# When accessing tuples the first index relates to which tuple you want to access, the second relates to the values within that tuple.

my_tuples = [("this is the first tuple in the list", 45, True),("this is the second tuple in the list", 21, False)]
print(my_tuples[0][0]) # this is the first tuple in the list
print(my_tuples[0][1]) # 45
print(my_tuples[1][0]) # this is the second tuple in the list
print(my_tuples[1][2]) # False


# Let's add another function to our inventory system. Write a function that returns the first element from a list. If the list is empty then return the string ERROR instead.

def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
    return items[0]

 
 # Reverse Lists using slicing

def reverse_array(items):
    return items[-1::-1]



# A list of the same messages but with all instances of the word dang removed.
# A list containing the number of dang words that were removed from the message at that particular index.

def filter_messages(messages):
    filtered_messages = [] # Created empy list i can add to later on.
    dang_count = []  # Created empy list i can add to later on.
    
    for messages in messages:
        words = messages.split() # Splits the words in the string into seperate strings.
        non_bad_words = []  # Empty list i can add to later.
        counter = 0  # Counter for the word dang. 
        
        for words in words:
            if words == "dang":  # Goes through strings and detects the word "dang"
                counter += 1  # Adds to the counter for every word "dang"
            else:
                non_bad_words.append(words)  # Adds the clean words to the non_bad_words List

        clean_message = " ".join(non_bad_words)  # Joins the seperate strings of non bad words into one string
        filtered_messages.append(clean_message)  # Adds the clean words message to the final filtered_message list
        dang_count.append(counter)  # adds the count of bad words to the dang_count list 
    
    return filtered_messages, dang_count  # Finally it returns the lists. 


# The .split() method is called on a string. If you don't pass it any arguments, it will just split the words in the string on the whitespace.

message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]


# The .join() method is called on a delimiter (what goes between all the words in the list), and takes a list of strings as input.

list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"



# Finding how many odd numbers and even numbers exist in a given list. 

def get_odds_and_evens(numbers):
    num_evens = 0
    num_odds = 0


    for i in range(0, len(numbers)):
        if numbers[i] % 2 != 0:
            num_odds += 1
        else:
            num_evens += 1
    return num_odds, num_evens



def get_test_score(answer_sheet, student_answers):
    total_questions = len(answer_sheet)
    correct_answers = 0

    for answer, student_answer in zip(answer_sheet, student_answers):  # zip()Combinds two seperate iterables into one 
        if answer == student_answer:
            correct_answers += 1

    percentage = (correct_answers / total_questions) * 100.0
    return percentage


def get_test_score(answer_sheet, student_answers):
    total_questions = len(answer_sheet)
    correct_answers = 0
    name = student_answers.pop(0)

    for correct_answer, student_answer in zip(answer_sheet, student_answers):
        if correct_answer == student_answer:
            correct_answers += 1

    percentage = (correct_answers / total_questions) * 100 

    return name, percentage


# How to double letters in a string 

def double_string(string):
    new_sentence = ""
    
    for letter in string:
        new_sentence += letter * 2
    return new_sentence

            
# Dictionaries in Python are used to store data values in key -> value pairs. Dictionaries are a great way to store groups of information.
# use curly braces
# add key-value pairs

car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}


def get_character_record(name, server, level, rank):
    record = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": name + "#" + server # concantenates "name" with a number (#) with a server 
    }

    return record


def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }


# accessing the value in a dictionary by calling the key in square brackets [ ]

car = {
    'make': 'tesla',
    'model': '3'
}
print(car['make'])
# Prints: tesla


names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_list = name.split()

    # here we update the dictionary
    names_dict[name_list[0]] = name_list[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}


# If you try to set the value of a key that already exists, you'll end up just updating the value of that key.
# In this example, "denver" overwrote "bronson" as the value for the key "jack".

full_names = ["jack bronson", "james mcarty", "jack denver"]

names_dict = {}
for full_name in full_names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    names = full_name.split()
    first_name = names[0]
    last_name = names[1]
    names_dict[first_name] = last_name

print(names_dict)
# {
#   'jack': 'denver',
#   'james': 'mcarty'
# }

# You can delete existing keys using the del keyword.

names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['joe']

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}

# Notice that if you try to delete a key that doesn't exist, you'll get an error.

names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['unknown']
# ERROR HERE, key doesn't exist

# If you're unsure whether or not a key exists in a dictionary, use the in keyword.

cars = {
    'ford': 'f150',
    'tesla': '3'
}

print('ford' in cars)
# Prints: True

print('gmc' in cars)
# Prints: False

# Checking for existence in a created dict. 

def count_enemies(enemy_names):

    enemy_name_dict = {}

    for enemy_name in enemy_names:
        if enemy_name in enemy_name_dict:
          enemy_name_dict[enemy_name] += 1
        else:
            enemy_name_dict[enemy_name] = 1
    return enemy_name_dict


# Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

def area_sum(rectangles):
    sum = 0
    for rectangle in rectangles:
        sum += rectangle["height"] * rectangle["width"]
    return sum



# iterating over a dictionary in python

def get_most_common_enemy(enemies_dict): # CHAT

    max_so_far = float("-inf")
    most_common_enemy = None

    for enemy, count in enemies_dict.items():
        if count > max_so_far:
            max_so_far = count
            most_common_enemy = enemy
    return most_common_enemy

# ORRRRR

def get_most_common_enemy(enemies_dict):

    max_so_far = float("-inf")
    most_common_enemy = None

    for enemy_name in enemies_dict:
        count = enemies_dict[enemy_name]
        if count > max_so_far:
            max_so_far = count
            most_common_enemy = enemy_name
    return most_common_enemy

# Dictionaries in python version 3.6 and older were unordered. 3.7 and newwer are ordered and can i can iterate over dictionaries in the same order every time. 

# Challenge showing how to access nested information in a dictionary.
{
    "type": {
        "student": {
            "name": "Allan",
            "courses": {
                "math_1050": {
                    "current_grade": "B",
                },
                "English_1010": {
                    "current_grade": "A-",
                },
            },
        }
    }
}

# Solution 

def get_english_grade(student):
    return student["type"]["student"]["courses"]["English_1010"]["current_grade"]


# Total score challenge

def merge(dict1, dict2): # k = key
    merged_dict = {} 
    for k in dict1:
        merged_dict[k] = dict1[k]
    for k in dict2:
        merged_dict[k] = dict2[k]
    return merged_dict

def total_score(score_dict):
    total = 0
    for k in score_dict:
        total += score_dict[k]
    return total

'''
items_purchased: A list of the names of items purchased on this shopping trip. This is a list of strings.
grocery_list: A list of the names of items Emma wanted to purchase. This is also a list of strings.

OUTPUTS
The function should return 3 values in this order:

unpurchased_items: A list of all the item names in grocery_list that weren't found in items_purchased in order.
receipt: A dictionary containing all the items Emma purchased, even stuff not on her list. The keys are the item names and the values are their respective prices from the item_prices dictionary.
total: The total cost of all the items that were purchased.
'''

def calculate_total(items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }


    unpurchased_items = []
    receipt = {}
    total = 0

    for item in grocery_list:
        if item not in items_purchased:
            unpurchased_items.append(item)

    for item in items_purchased:
        price = item_prices[item]
        receipt[item] = price
        total += price

    return unpurchased_items, receipt, total



# Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set

fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

# add values

fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

# Note: No error will be raised if you add an item already in the set.

# Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.

fruits = set()
fruits.add('pear')
print(fruits)
# Prints: {'pear'}

# ITERATE OVER VALUES IN A SET (ORDER IS NOT GUARANTEED)

fruits = {'apple', 'banana', 'grape'}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple


    def remove_duplicates(spells):

    learned_spells = set(spells) # I add the spells to a set. Removing any duplicates by adding to a set. 
    com_spells = [] # created an empty list to add to later.
    
    for spells in learned_spells: # iterate over spells in the set.
        com_spells.append(spells) # add spells to the com_spells list with removed duplicates. 
    return com_spells

# How to remove values from a set. my_set.remove("item")

fruits = {'apple', 'banana', 'grape'}
fruits.remove('apple')
print(fruits)
# Prints: {'banana', 'grape'}


# Complete the count_vowels function. It should take a string and return a count of the number of vowels within the given string, and a set of its unique vowels.


def count_vowels(text):
    l_case_vowels = ["a", "e", "i", "o", "u"]
    u_case_vowels = ["A", "E", "I", "O", "U"]

    unique_vowels = set()
    vowel_count = 0
    
    for word in text:
        for letter in word:
            if letter in l_case_vowels or letter in u_case_vowels:
                vowel_count += 1
                unique_vowels.add(letter)
    return vowel_count, unique_vowels



# Converting lists into sets and back into lists. 

# You can convert a List to a Set using the set() function.
# You can convert a Set to a List using the list() function.
# You can subtract the elements in one Set from another Set using the - operator.

def find_missing_ids(first_ids, second_ids): # currently lists
    
    first_ids_set = set(first_ids)
    second_ids_set = set(second_ids)
    new_ids = first_ids_set - second_ids_set 
    final_list = list(new_ids)

    return final_list

# Even if your code has the right syntax, however, it may still cause an error when an attempt is made to execute it.
# Errors detected during execution are called "exceptions" and can be handled gracefully by your code. 
# You can even raise your own exceptions when bad things happen in your code.

# Python uses a try-except pattern for handling errors.

try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"

'''
The try block is executed until an exception is raised or it completes, whichever happens first. In this case, a "divide by zero" error is raised because division by zero is impossible. 
The except block is only executed if an exception is raised in the try block. It then exposes the exception as data (e in our case) so that the program can handle the exception gracefully without crashing.
'''

try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
except Exception as e:
        print(e)

        
    


# Don't edit below this line


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")



# Syntax for rasing an exception:

# raise Exception("something bad happened")

# Example in function 

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


# For now, what is important to understand is that there are different types of exceptions and that we can differentiate between them in our code.

try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)

# 0 division
# index error


# That's looking much better! You've addressed the previous issue by ensuring that get_player_record(player_id)'s result is returned if it succeeds, and you're correctly handling exceptions. 
# Your use of return in each block means your function will return either the player record, "index is too high" if there's an IndexError, or the exception itself for any other kind of exception.
# This matches the task's requirements closely. Well done on making those adjustments!

def handle_get_player_record(player_id):
    try:
        return get_player_record(player_id)
    
    except IndexError:
        return ("index is too high")
    except Exception as e:
        return (e)
    


# This program will crash with an uncaught exception 

try:
    raise Exception('zero division')
except ZeroDivisionError as e:
    print("zero")

# This will print "other"

 try:
    raise Exception('zero division')
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")

# If the customer doesn't have enough money raise an exception with the text "not enough money". Don't handle the exception. 
# Otherwise, return the amount of money the customer has leftover after completing the purchase.

def purchase(price, money_available):
    if money_available >= price:
        change = money_available - price
    elif money_available < price:
        raise Exception("not enough money")
    return change


# Completing the function above to process an entire list of purchase orders.



def make_purchases(purchase_orders):
    leftovers = []
    for purchase_order in purchase_orders:
        try:
            price = purchase_order["price"]  # Defining the varicbale to the key "price"
            money_available = purchase_order["money_available"]  # Defining the variable to the value "money available"
            leftover = purchase(price, money_available)  # Using the purchase function to process the order. 
            leftovers.append(leftover)  # Adding the leftover money to my empty list 
        except Exception as e:  
            print(f"Purchase exception: {e}")
    return leftovers
            

# Don't edit below this line


def main():
    print("Making purchases...")
    leftovers = make_purchases(
        [
            {"price": 10.00, "money_available": 125.00},
            {"price": 5.00, "money_available": 2.00},
            {"price": 20.01, "money_available": 5.20},
            {"price": 1.04, "money_available": 254.00},
            {"price": 40.20, "money_available": 6.00},
            {"price": 16.00, "money_available": 235.01},
            {"price": 10.70, "money_available": 10.70},
            {"price": 12.00, "money_available": 2.30},
        ]
    )
    print("Purchases complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")


def purchase(price, money_available):
    if money_available < price:
        raise Exception(f"{money_available:.2f} is not enough for {price:.2f}")
    return money_available - price


main()

# You can check the type of a variable using type() function. if type(variable) == int:
# Complete the remove_nonints() function that takes a list and returns a new list with all the non-integer types removed.

def remove_nonints(nums):
    
    removed_non_integers = []

    for ints in nums:
        if type(ints) == int:
            removed_non_integers.append(ints)
    return removed_non_integers


# FIZZBUZZ function. Complete the fizzbuzz function that loops over all the numbers from start to end (excluding the end value) and prints them. 
# If the number is a multiple of 3, instead of printing the number, print "fizz". If the number is a multiple of 5, instead print "buzz". 
# If it is a multiple of 3 and 5 then instead print "fizzbuzz".

def fizzbuzz(start, end):
    for i in range(start, end):
        if i % 15 == 0: 
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)

# DONT TOUCH BELOW == TEST CASES

def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()


# List division. Write a function called divide_list() that takes a list and a number as input. The function returns a new list that contains all the elements of the original list except they have been divided by the second input.
# Example divide_list([6, 8, 10], 2)
# returns values[3.0, 4.0, 5.0]

def divide_list(nums, divisor):
    new_list = []
    value = 0
    
    for num in nums:
        value = num / divisor
        new_list.append(value)
    return new_list


# Tim Peters "The Zen of Python"
'''
Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than right now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!
'''


LESSON 2:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]

# Create a new function called get_soldier_dps that takes a soldier and returns its DPS using the same logic as the lines above. Then, replace the two lines above with calls to get_soldier_dps.

def get_soldier_dps(soldier):
    DPS = soldier["damage"] * soldier["attacks_per_second"]
    return DPS



def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)

    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"



# CLASSES:

# """A class is a special type of value in an object-oriented programming language like Python. It's similar to a dictionary in that it usually stores other types inside itself.
# Just like a string, integer or float, a class is a type, but instead of being a built-in type, your classes are custom types that you define.
# An object is just an instance of a class type. For example:

# Defines a new class called "Soldier"
class Soldier:
    health = 5
    armor = 3
    damage = 2


health = 50
# health is an instance of an integer type
aragorn = Soldier()
# aragorn is an instance of the Soldier type (class)


class Archer:
    health = 40
    arrows = 10

# Create several instances of the Archer class
legolas = Archer()
bard = Archer()

# Print class properties
print(legolas.health) # 40
print(bard.arrows) # 10


## EXAMPLE 2 with a METHOD

class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"

class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3" 



# Add a fortify() method to your wall class. It should double the current armor property.

class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2


# Add a .get_cost() method to your wall class. What do you think it should return? The cost of a wall is the product of its height and armor:
# DEV SOLUT
class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        return self.armor * self.height


    # don't touch below this line


    def fortify(self):
        self.armor *= 2

# MY SOLUTE

class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        cost = self.armor * self.height
        return cost

    # don't touch below this line

    def fortify(self):
        self.armor *= 2


class Soldier:
    name = "Legolas"
    armor = 2
    num_weapons = 2

# It's more practical to use a constructor. In Python, if you name a method __init__, that's the constructor and it is called when a new object is created.
# So, with a constructor, the code would look like this: __init__ aka : 

class Soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2

# Now we can make the starting armor and number of weapons configurable with some parameters!

class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier("Legolas", 5, 10)
print(soldier.name)
# prints "Legolas"
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"

'''A constructor is a special method in a class that gets called automatically when a new object (or instance) of the class is created.

Its main job is to initialize the object's attributes and set up any necessary initial states.
In Python, this constructor method is always named __init__. Heres what it does:

Initializes Attributes: It sets the initial values for the object's attributes.
Gets Called Automatically: When you create a new instance of a class, Python automatically calls the __init__ method without you having to explicitly call it.'''

class WizardBear:
    def __init__(self, name, spells, power_level):
        self.name = name
        self.spells = spells
        self.power_level = power_level

    def cast_spell(self):
        return f"{self.name} casts {self.spells} with power level {self.power_level}!"
    
'''Here’s what happens:

Define the Class: WizardBear is a class with a constructor method __init__.
The __init__ Method: It takes name, spells, and power_level as arguments and sets these as attributes of the instance.
Create an Instance: When you create a WizardBear like this:
merlin = WizardBear("Merlin", "fireball", 99)
Python automatically calls:
merlin.__init__("Merlin", "fireball", 99)
so self.name becomes "Merlin", self.spells becomes "fireball", and self.power_level becomes 99.'''


# MULTIPLE OBJECTS

'''An object is an "instance" of a class. Let's look at what that means.

In object-oriented programming, an instance is a concrete occurrence of any object... "Instance" is synonymous with "object" as they are each a particular value... "Instance" emphasizes the distinct identity of the object. The creation of an instance is called instantiation.

So for our wall class, I can create three different "instances" of the class. Or, in other words, I can create three separate objects.'''

wall_maria = Wall(1, 2, 3)
wall_rose = Wall(4, 5, 6)
wall_sina = Wall(9, 8, 7)

# In the example above, the variables are instances of the Wall type.

class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier("Legolas", 5, 1)
print(soldier_one.name)
# "Legolas"
print(soldier_one.get_speed())
# 4





def main():
    Brawler_Aragorn = Brawler(4, 4, "Aragorn")
    Brawler_Gimli = Brawler(2, 7, "Gimli")
    Brawler_Legolas = Brawler(7, 7, "Legolas")
    Brawler_Frodo = Brawler(3, 2, "Frodo")
    fight(Brawler_Aragorn, Brawler_Gimli)
    fight(Brawler_Legolas, Brawler_Frodo)
    


# don't touch below this line


class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name


def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")


main()



'''Complete the get_shot method. It doesn't take any parameters.

If the current archer has health left, remove one health from the current archer. Then, if the archer's health is 0, raise the exception: {} is dead where {} is the archer's name.

SHOOT METHOD
Finish the shoot method. It takes an Archer instance as the target input.

If the shooter has no arrows left, raise the exception {} can't shoot where {} is the shooter's name.
Otherwise, remove an arrow from the shooter and print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the targeted archer. Next, call the target's get_shot() method.'''

class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def get_shot(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
             raise Exception(f"{self.name} is dead")
            

    def shoot(self, target):
        if self.num_arrows == 0:
            raise Exception(f"{self.name} can't shoot")
        elif self.num_arrows > 0:
            print(f"{self.name} shoots {target.name}")
            self.num_arrows -= 1
            target.get_shot()


 # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")





# INSTANCE VARIABLES
# Instance variables vary from object to object and are declared in the constructor.

class Wall:
    def __init__(self):
        self.height = 10

south_wall = Wall()
south_wall.height = 20 # only updates this instance of a wall
print(south_wall.height)
# prints "20"

north_wall = Wall()
print(north_wall.height)
# prints "10"


# CLASS VARIABLES
# Class variables remain the same between instances of the same class and are declared at the top level of a class definition.

class Wall:
    height = 10

south_wall = Wall()
print(south_wall.height)
# prints "10"

Wall.height = 20 # updates all instances of a Wall

print(south_wall.height)
# prints "20"
# In other languages these types of variables are often called static variables.

# Generally speaking, stay away from class variables. Just like global variables, class variables are usually a bad idea because they make it hard to keep track of which parts of your program are making updates. 
# However, it is important to understand how they work because you may see them out in the wild.




class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for lib_book in self.books:
            if book.title == lib_book.title and book.author == lib_book.author: # Comparing the title nd author to current books in self.book lsit
                self.books.remove(lib_book)

    def search_books(self, search_string):
        matching_books = [] # create an empty list for matching books

        for lib_book in self.books: # loop through each book in the library
            # Checking if the search string is in the title or author, case insensitive
            if (
                search_string.lower() in lib_book.title.lower()
                or search_string.lower() in lib_book.author.lower()
            ):
                matching_books.append(lib_book) # Adding the matching book to the list
        return matching_books # return the list of matching books. 
    




class Employee:
    company_name = "Age of Dragons, Inc."
    total_employees = 0 # Class variable

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1

    def get_name(self):
        return self.first_name + " " + self.last_name
    
# ENCAPSULATION: 

'''Encapsulation is the practice of hiding complexity inside a "black box" so that it's easier to focus on the problem at hand.

encapsulation

The most basic example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.'''

# Encapsulation is about organization, not security.

# Encapsulation is like folders in an unlocked filing cabinet. They don't stop someone from peeking inside, but they do keep everything tidy and easy to find.

# By default, all properties and methods in a class are public. That means that you can access them with the . operator:

wall.height = 10
print(wall.height)
# 10


# Private data members are how we encapsulate logic and data within a class. To make a property or method private, you just need to prefix it with two underscores.

class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30



class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name # Public
        self.__stamina = stamina # private
        self.__intelligence = intelligence # Private
        self.health = self.__stamina * 100  # health: 100x the value of "stamina". Public accessing private properties
        self.mana = self.__intelligence * 10 # mana: 10x the value of "intelligence". Public accessing private properties


# Add the following methods to the Wizard class.

'''
GET_FIREBALLED()
This method operates on the instance of the class. It takes no inputs and returns no values explicitly, but it should remove 500 health from the wizard.

DRINK_MANA_POTION()
This method operates on the instance of the class. It takes no inputs and returns no values explicitly, but it should add 100 mana to the wizard's reserves.'''


fireball_damage = 500
potion_mana = 100


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def get_fireballed(self):
        self.health -= fireball_damage

    def drink_mana_potion(self):
        self.mana += potion_mana


'''
Python is a dynamic language, and that makes it difficult for the interpreter to enforce some of the safeguards that languages like Go do.
That's why encapsulation in Python is achieved mostly by convention rather than by force.
Prefixing methods and properties with a double underscore is a strong suggestion to the users of your class that they shouldn't be touching that stuff.
If a developer wants to break convention, there are ways to get around the double underscore rule.'''


class Wall:
    def __init__(self, height):
        # the double underscore make this a private property
        # but it's not strictly enforced, there are hacks to get around it
        self.__height = height

    def get_height(self):
        return self.__height
    

'''
Complete the cast_fireball and __is_alive methods.

CAST_FIREBALL
If there isn't enough mana to cast a fireball (see fireball_cost at the top of the file), raise an Exception with the message ____ cannot cast fireball, where ____ is the wizard's name.

If the wizard has enough mana, reduce their mana by the fireball_cost and call get_fireballed on the target wizard.

__IS_ALIVE
This method should return True if the wizard's health is greater than 0, and False otherwise.'''



fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        if self.mana >= fireball_cost:
            self.mana -= fireball_cost
            target.get_fireballed()
            

    def __is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_fireballed(self):
        self.health -= fireball_damage

    def drink_mana_potion(self):
        self.mana += potion_mana


# don't touch below this line


def main():
    merlin = Wizard("Merlin", 15, 10)
    morgana = Wizard("Morgana", 17, 5)
    print_wizard_stats(merlin)
    print_wizard_stats(morgana)

    while merlin._Wizard__is_alive() and morgana._Wizard__is_alive():
        test_cast(merlin, morgana)
        test_cast(morgana, merlin)

    print(" -- Done! --")


def test_cast(caster, target):
    print(f"  >  {caster.name} casts fireball at {target.name}")
    try:
        caster.cast_fireball(target)
    except Exception as e:
        print(f"    >  !!!{e}!!!")
        test_drink_potion(caster)
    print_wizard_stats(caster)
    print_wizard_stats(target)


def test_drink_potion(caster):
    print(f"  >  {caster.name} drinks mana potion")
    caster.drink_mana_potion()


def print_wizard_stats(wizard):
    print(f"{wizard.name}: health={wizard.health}, mana={wizard.mana}")


main()



'''Great! Your deposit and withdraw methods are now simplified, getting rid of unnecessary else blocks.

Let's summarize what I have achieved:

Constructor (__init__ method): Initializes private variables for the account number and balance.
Public Getters (get_account_number and get_balance): Return the account number and balance respectively.
Deposit Method (deposit): Adds the given amount to the balance after verifying it's positive, otherwise raises an error.
Withdraw Method (withdraw): Deducts the given amount from the balance after verifying it's positive and that there are sufficient funds, otherwise raises an error.
'''



class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"Cannot deposit zero or negative funds")
        self.__balance += amount
        
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"Cannot withdraw zero or negative funds")
        if self.__balance < amount:
            raise ValueError(f"Insufficient funds")
        self.__balance -= amount


'''
Here are a few reasons why we use ValueError:

Clarity: ValueError indicates exactly what type of error occurred—an issue with the value provided. This is clearer than a generic exception.

Granularity: In a larger codebase, catching specific exceptions allows you to handle different error conditions in distinct ways. 
This is particularly true if you'd like to distinguish between different types of errors that might occur.

Standard Practice: Using built-in exceptions such as ValueError follows Python's standard practices, making your code more consistent and understandable to others.

EXAMPLE FOR DIFFERENCE:
Let's say you have a function like this:

def do_something(value):
    if value < 0:
        raise ValueError("Negative values not allowed")
    if not isinstance(value, int):
        raise TypeError("Value must be an integer")
    # perform some operation

If you use generic Exception instead:

def do_something(value):
    if value < 0:
        raise Exception("Negative values not allowed")
    if not isinstance(value, int):
        raise Exception("Value must be an integer")
    # perform some operation

When you try to handle exceptions:

try:
    do_something(value)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)

In the first example, you can specifically catch ValueError or TypeError and handle them accordingly, but in the second example, every error is caught by Exception, removing the granularity.
'''




class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        if score >= 80 and score <= 89:
            return "B"
        if score >= 70 and score <= 79:
            return "C"
        if score >= 60 and score <= 69:
            return "D"
        if score < 60:
            return "F"

    def add_course(self, course_name, score):
        letter_grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = letter_grade
        

    def get_courses(self):
        return self.__courses
    

'''
INSTANCE VARIABLE VS REGULAR (LOCAL) VARIABLE:
Instance Variable:

An instance variable is tied to an instance (an object) of a class. This means each instance of the class can have its own copy of the instance variable.
In Python, instance variables are defined using self. followed by the variable name (e.g., self.name).
These variables are accessible throughout the instance and can hold data particular to that object.
Regular (Local) Variable:

A regular or local variable is defined within a method or function and only accessible within that method or function.
It is temporary and only exists during the execution of that method. It doesn't use self.
For example:'''

class Example:
    def __init__(self, name):
        self.instance_variable = name  # Instance variable

    def change_name(self, new_name):
        local_variable = new_name  # Local variable
        self.instance_variable = local_variable  # Using the local variable to update an instance variable

# Create an instance of the class
ex = Example("Alice")
print(ex.instance_variable)  # Output: Alice
ex.change_name("Bob")
print(ex.instance_variable)  # Output: Bob

'''INSTANCE METHOD VS REGULAR FUNCTION:
An instance method is a function that is defined in a class and is meant to operate on instances of that class. It always takes at least one parameter, usually self, which refers to the instance calling the method.

USAGE OF SELF.CALCULATE_LETTER_GRADE(SCORE):
In your add_course method, calculate_letter_grade is defined as a method of the Student class. This means it is an instance method and must be called with self to indicate it is being called on the current instance of the class.

Here's an example to illustrate:'''

class Example:
    def greeting(self):
        return "Hello, " + self.name  # Instance method using an instance variable

    def set_name(self, name):
        self.name = name  # Setting an instance variable

# Create an instance
ex = Example()
ex.set_name("Alice")  # Using instance method to set name
print(ex.greeting())  # Using instance method to get a greeting - Output: Hello, Alice



'''
INSTANCE METHODS
An instance method is a function defined in a class that operates on an instance of that class. To call an instance method, you need to access it through an instance of the class. Here are the common patterns:

Calling an Instance Method on Another Object:

If you have an instance of a class (like your target in the get_fireballed example), you call the method directly on that instance.
target.get_fireballed()
Copy icon
This means get_fireballed is a method defined in the class of the target object.

Calling an Instance Method within Another Method:

When calling a method from within another method of the same class, you use self to refer to the current instance.
letter_grade = self.calculate_letter_grade(score)
Copy icon
Here, self.calculate_letter_grade(score) means you are calling the calculate_letter_grade method on the current instance (self) of the Student class.

EXAMPLE TO ILLUSTRATE BOTH CASES:'''

class Target:
    def get_fireballed(self):
        return "Ouch! I've been fireballed!"


class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        # Calling a method within the same class using self
        letter_grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = letter_grade

    def get_courses(self):
        return self.__courses


# Creating an instance of Target
target = Target()
# Calling an instance method on the target instance
print(target.get_fireballed())  # Output: Ouch! I've been fireballed!

# Creating an instance of Student
student = Student("Zatanna")
# Adding a course and calling an instance method within another method
student.add_course("Maths", 85)
print(student.get_courses())    # Output: {'Maths': 'B


'''
ABSTRACTION
Abstraction helps us handle complexity by hiding unnecessary details. Sounds like encapsulation, right? They're so similar that it's almost not worth worrying about the difference...almost.

ABSTRACTION VS ENCAPSULATION
Abstraction is about creating a simple interface for complex behavior. It focuses on what's exposed.
Encapsulation is about hiding internal state. It focuses on tucking implementation details away so no one depends on them.
Abstraction is more about reducing complexity, encapsulation is more about maintaining the integrity of system internals.
'''


class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed
        

    def get_position(self):
        return self.__pos_x, self.__pos_y
    

    '''
    move_right: Adds the human's speed to its x position.
move_left: Subtracts the human's speed from its x position.
move_up: Adds the human's speed to its y position.
move_down: Subtracts the human's speed from its y position.
get_position: Returns the current position as a tuple of x and y.
Now, let's make sure everything looks correct.

In move_right, self.__pos_x is increased by self.__speed.
In move_left, self.__pos_x is decreased by self.__speed.
In move_up, self.__pos_y is increased by self.__speed.
In move_down, self.__pos_y is decreased by self.__speed.
In get_position, a tuple of self.__pos_x and self.__pos_y is returned.
Would you like to test this now and see what results you get? If there's anything else you'd like to verify or discuss, let me know!'''


'''
The __raise_if_cannot_sprint and __use_sprint_stamina are private methods that are only intended to be used within the class. In your case, you'll use them to build the other four sprinting methods.

__RAISE_IF_CANNOT_SPRINT
This method should raise the exception: not enough stamina to sprint if the human is out of stamina.

__USE_SPRINT_STAMINA
Remove one stamina from the human.

THE REMAINING METHODS
Raise an error if there isn't enough stamina to sprint (use __raise_if_cannot_sprint()).
Use the stamina needed to sprint (use __use_sprint_stamina())
Move twice in the direction of the sprint.
'''


class Human:
    def sprint_right(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_right()
        self.move_right()

    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_left()
        self.move_left()

    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_up()
        self.move_up()

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_down()
        self.move_down()

    def __raise_if_cannot_sprint(self):
        if self.__stamina == 0:
            raise Exception(f"not enough stamina to sprint")

    def __use_sprint_stamina(self):
        if self.__stamina > 0:
            self.__stamina -= 1

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina



'''
Complete the Calculator class.

CONSTRUCTOR
Create a private instance variable called result initialized to 0.

MATH
The following methods should perform their respective mathematic computations. The "left-hand side" of each operation should be the current value of the result variable. The "right-hand side" of each operation will be the value passed in.

add(self, a)
subtract(self, a)
multiply(self, a)
divide(self, a): If the user attempts to divide by 0, raise a ValueError with "Cannot divide by zero" as the argument
modulo(self, a): If the user attempts to divide by 0, raise a ValueError with "Cannot divide by zero" as the argument
power(self, a):
square_root(self)
HELPER METHODS
clear(self): reset the result variable to 0
get_result(self): return the current value stored in the calculator's private result variable.
'''


class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a
        return self.__result

    def subtract(self, a):
        self.__result -= a
        return self.__result

    def multiply(self, a):
        self.__result *= a
        return self.__result

    def divide(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result /= a
        return self.__result

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result %= a
        return self.__result

    def power(self, a):
        self.__result **= a
        return self.__result

    def square_root(self):
        self.__result **= 0.5
        return self.__result

    def clear(self):
        self.__result = 0
        return self.__result

    def get_result(self):
        return self.__result
    




import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    
    def __init__(self):  
        self.__cards = [] # Create an empty list
        self.create_deck() # Fill the empty list by calling this method in my constructor. 
        

    def create_deck(self):
        for suit in self.SUITS: # for suit in self.SUITS: loops through each suit.
            for rank in self.RANKS: # for rank in self.RANKS: loops through each rank within the current suit.
                self.__cards.append((rank, suit)) # self.__cards.append((rank, suit)) creates a tuple for each card and adds it to the deck.
                

    def shuffle_deck(self):
        random.shuffle(self.__cards) # Shuffles the deck

    def deal_card(self):
        if len(self.__cards) > 0: # checks to see if there are cards to deal in the deck
            return self.__cards.pop() # Deals from the deck
        else:
            return None # If no cards returns None

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
    


'''
INHERITANCE
We've made it to the holy grail of object-oriented programming: inheritance. Non-OOP languages like Go and Rust allow for encapsulation and abstraction features as nearly every language does. Inheritance, on the other hand, tends to be unique to class-based languages like Python, Java, and Ruby.

WHAT IS INHERITANCE?
Inheritance allows one class, the "child" class, to inherit the properties and methods of another class, the "parent" class.

This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.

SYNTAX
Here Cow is a "child" class that inherits from the "parent" class Animal:
'''
#class Animal:
    # parent "Animal" class

#class Cow(Animal):
    # child class "Cow" inherits "Animal"

# The Cow class can reuse the Animal class's constructor with the super() method:

class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to
        # give the cow some legs
        super().__init__(4)

'''In Age of Dragons, all the archers are humans, but not all humans are necessarily archers. All humans have a name, but only archers have a __num_arrows property.

Complete the Archer class. It should inherit the Human class. In its constructor it should call its parent's constructor, then also set its unique __num_arrows property.'''

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        self.name = name
        self.__num_arrows = num_arrows
        super().__init__(name)

    def get_num_arrows(self):
        return self.__num_arrows



'''
Encapsulation is a core principle in object-oriented programming. By keeping data private, we can control how it's accessed and modified. Here’s why it’s often important to make certain attributes private:

Control Access: By controlling access to important attributes, you can ensure they are only modified in specific ways. For example, you might have a method to validate the data before setting an attribute.

Prevent Inadvertent Changes: If attributes are public, they might be changed from outside the class, potentially leading to unexpected behavior or bugs. For instance, someone might set num_arrows to a negative number if it's not encapsulated properly.

Maintain Invariants: Invariants are conditions that should always hold true for your object. By encapsulating attributes, you can enforce these conditions. For example, you might want to ensure num_arrows is always a non-negative number.

Flexibility to Change: Encapsulation allows you to change the internal implementation without affecting external code that uses your class. If num_arrows is private, you can modify how it's calculated or stored without breaking code that relies on your class.

Let's say we have the following private attribute:'''

class Archer:
    def __init__(self, name, num_arrows):
        self.__num_arrows = num_arrows

# Now, if you want to change the way num_arrows is set or validated, you can do so safely within the class without worrying that some external code will break:

class Archer:
    def __init__(self, name, num_arrows):
        self.__num_arrows = 0
        self.set_num_arrows(num_arrows)
    
    def set_num_arrows(self, num_arrows):
        if num_arrows < 0:
            raise ValueError("Number of arrows cannot be negative")
        self.__num_arrows = num_arrows




'''WHEN SHOULD I USE INHERITANCE?
Inheritance is a powerful tool, but it is a really bad idea to try to overuse it. Inheritance should only be used when all instances of a child class are also instances of the parent class.

When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance is probably not the best answer. Better to simply share some functions, or maybe make a new parent class that both classes can inherit from.

All cats are animals but not all animals are cats:'''


class Animals:
    # Animals class

    class Plants:
    # Plants class

        class Cats(Animals):
            # Cats (child class) inherits methods from the Animals (Parent class). 
            class Animals(Plants):
                '''# Wouldnt make sense cause they dont have anything in common.'''



''''Animals' and 'plants' might inherit from a new class called Organisms'''


'''INHERITANCE HIERARCHY
There is no limit to how deeply we can nest an inheritance tree. For example, a Cat can inherit from an Animal that inherits from LivingThing. That said, be careful! New programmers often get carried away.

You should never think to yourself:

"Well most wizards are elves... so I'll just have wizard inherit from elf"

A good child class is a strict subset of its parent class.'''





class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name) # Calls the parent constructor
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows 

    def use_arrows(self, num):
        if self.__num_arrows < num: 
            raise Exception("not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows) # Call to parent constructor

    def triple_shot(self, target):
        self.use_arrows(3) # use 3 arrows
        target_name = target.get_name() # Gets target name
        return f"{target_name} was shot by 3 crossbow bolts" # Returns formatted message
    




# Example of inheritance in code:

class RealEstate:
    def __init__(self, location):
        self.__location = location


class Residential(RealEstate):
    def __init__(self, location, bedrooms):
        super().__init__(location)
        self.__bedrooms = bedrooms


class House(Residential):
    def __init__(self, location, bedrooms, yard_size):
        super().__init__(location, bedrooms)
        self.__yard_size = yard_size


'''
INHERITANCE
Inheritance can be thought of as a way for one class (child class) to get properties and behaviors (methods) from another class (parent class).
This lets us reuse code, making our programs more organized and easier to manage.'''
EXAMPLE BREAKDOWN
Let's recap the given example with RealEstate, Residential, and House.

# RealEstate:

class RealEstate:
    def __init__(self, location):
        self.__location = location
'''This is our parent class.
It has one property: location.'''

# Residential:

class Residential(RealEstate):
    def __init__(self, location, bedrooms):
        super().__init__(location)
        self.__bedrooms = bedrooms

'''This is a child class that inherits from RealEstate.
It has a new property: bedrooms.
It uses super().__init__(location) to call the constructor of the parent class (RealEstate) to initialize the location property.'''

# House:

class House(Residential):
    def __init__(self, location, bedrooms, yard_size):
        super().__init__(location, bedrooms)
        self.__yard_size = yard_size

'''This is another child class, but it inherits from Residential.
It has a new property: yard_size.
It uses super().__init__(location, bedrooms) to call the constructor of the parent class (Residential) to initialize the location and bedrooms properties.'''


# A parent class can have multiple children.


class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0: 
            raise Exception(f"not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10) 

class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name,health)
        self.__mana = mana

    def cast(self, target):
        if self.__mana < 25:
            raise Exception(f"not enough mana")
        self.__mana -= 25
        target.take_damage(25)




'''You'll often find that it's more likely that an inheritance tree is wide than deep. In other words, instead of a deep tree like:

wide vs deep inheritance

WHY ARE INHERITANCE TREES OFTEN WIDE INSTEAD OF DEEP?
As we talked about earlier, in good software a child class is a strict subset of its parent class. In a deep tree, that means the children need to be perfect members of all the parent class "types". 
That simply doesn't happen very often in the real world. It's much more likely that you'll have a base class that simply has many sibling classes that are slightly different variations of the base.'''



class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if (self.pos_x >= x_1 
            and self.pos_x <= x_2 
            and self.pos_y >= y_1 
            and self.pos_y <= y_2
            ):
            return True
        else:
            return False
       

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_units = []
        for unit in units:
            if unit.in_area(
                x - self.__fire_range, y - self.__fire_range,
                x + self.__fire_range, y + self.__fire_range
            ):
                hit_units.append(unit)
        return hit_units
    
# Create a list hit_units to collect the units hit by the fire breath.
# Loop through each unit in units.
# Check if the unit is in the fire area by using in_area method.
# Append it to hit_units if it is inside the fire area.
# Finally, return the list hit_units.


# To get a new copy of a list, use the copy() method. If you don't, your new variable will just be a reference to the original list.
nums = [4, 3, 2, 1]
nums_copy = nums.copy()
# nums_copy is [4, 3, 2, 1]

# DELETE FROM A LIST
nums = [4, 3, 2, 1]
del nums[1]
# nums is [4, 2, 1]



def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    # don't touch above this line
    dragons_copy = dragons.copy() 
    for dragon in dragons_copy:
        describe(dragon)
    for i in range(len(dragons)):
        dragon = dragons[i]
        other_dragons = dragons.copy()
        del other_dragons[i]
        dragon.breathe_fire(x=3, y=3, units=other_dragons)
    
    


# don't touch below this line


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("====================================")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()



class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        area = self.__length * self.__width
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        return perimeter

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)




class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        trip_cost = (distance / self.efficiency) * food_price 
        return trip_cost

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        base_cost = super().get_trip_cost(distance, food_price)
        return base_cost + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        volume = self.bed_area * 2
        return volume


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume



'''While inheritance is the most unique trait of object-oriented languages, polymorphism is probably the most powerful. Polymorphism is the ability of a variable, function or object to take on multiple forms.

"poly"="many"
"morph"="form".
For example, classes in the same hierarchical tree may have methods with the same name but different behaviors.

SHAPES
Let's look at a simple example.'''

class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        else:
            return self.__x2
            
    def get_right_x(self):
        if self.__x2 > self.__x1:
            return self.__x2
        else:
            return self.__x1

    def get_top_y(self):
        if self.__y2 > self.__y1:
            return self.__y2
        else:
            return self.__y1
        

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        else:
            return self.__y2

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
    


'''
Get the edges of both rectangles: Use the helper methods to find the left, right, top, and bottom edges of both self and rect.

Check the conditions:

A's left side (self_left) is on or to the left of B's right side (rect_right)
A's right side (self_right) is on or to the right of B's left side (rect_left)
A's top side (self_top) is on or above B's bottom side (rect_bottom)
A's bottom side (self_bottom) is on or below B's top side (rect_top)
'''

class Rectangle:
    def overlaps(self, rect):
        self_left = self.get_left_x()
        self_right = self.get_right_x()
        self_top = self.get_top_y()
        self_bottom = self.get_bottom_y()

        rect_left = rect.get_left_x()
        rect_right = rect.get_right_x()
        rect_top = rect.get_top_y()
        rect_bottom = rect.get_bottom_y()
        
        overlap = (
            self_left <= rect_right and
            self_right >= rect_left and
            self_top >= rect_bottom and
            self_bottom <= rect_top
        )

        return overlap

        
    
         

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
    

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return(
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        half_width = self.width / 2
        half_height = self.height / 2
        left_x = self.pos_x - half_width
        right_x = self.pos_x + half_width
        bottom_y = self.pos_y - half_height
        top_y = self.pos_y + half_height
        self.__hit_box = Rectangle(left_x, bottom_y, right_x, top_y)

    def in_area(self, x1, y1, x2, y2):
        area_rectangle = Rectangle(x1, y1, x2, y2)
        return self.__hit_box.overlaps(area_rectangle)


# Don't touch below this line


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
    


'''
Take a look at the Greek roots of the word "polymorphism".

"poly" means "many".
"morph" means "to change" or "form".
Polymorphism in programming is the ability to present the same interface (function or method signatures) for many different underlying forms (data types).

A classic example is a Shape class that Rectangle, Circle, and Triangle can inherit from. With polymorphism, each of these classes will have different underlying data. 
The circle needs its center point coordinates and radius. The rectangle needs two coordinates for the top left and bottom right corners. The triangle needs coordinates for the corners.

By making each class responsible for its data and its code, you can achieve polymorphism. In the shapes example, each class would have its own draw_shape() method. 
This allows the code that uses the different shapes to be simple and easy, and more importantly, it can treat shapes as the same even though they are different. 
It hides the complexities of the difference behind a clean abstraction.
'''


shapes = [Circle(5, 5, 10), Rectangle(1, 3, 5, 6)]
for shape in shapes:
    print(shape.draw_shape())


'''
This is in contrast to the functional way of doing things where you would have had separate functions that have different function signatures, 
like draw_rectangle(x1, y1, x2, y2) and draw_circle(x, y, radius).
'''

'''
A function signature (or method signature) includes the name, inputs, and outputs of a function or method. For example, hit_by_fire in the Human and Archer classes have identical signatures.
'''

class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self):
        self.health -= 10
        return self.health
    
'''
Both methods have the same name, take 0 inputs, and return integers. If any of those things were different, they would have different function signatures.
'''

# Example of different signatures

class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self, dmg):
        self.health -= dmg
        return self.health
    

'''
The Archer class's hit_by_fire method takes an input, dmg, which is used to calculate the new health. This is a different signature than the Human class's hit_by_fire method, which takes no inputs. 
Calling two methods with the same signature should look the same to the caller.
'''


# same inputs (none)
# same name
# same outputs (a single integer)
health = sam.hit_by_fire()
health = archer.hit_by_fire()


'''
WHEN OVERRIDING METHODS, USE THE SAME FUNCTION SIGNATURE
If you change the function signature of a parent class when overriding a method, it could be a disaster. 
The whole point of overriding a method is so that the caller of your code doesn't have to worry about what different things are going on inside the methods of different object types.
'''

'''
The main benifit of Polymorphism is to hide the differences between subtypes from users of your code.
'''

# Operator overloading

'''Another kind of built-in polymorphism in Python is the ability to override how an operator works. For example, the + operator works for built-in types like integers and strings.'''

print(3 + 4)
# prints "7"

print("three " + "four")
# prints "three four"


class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == other.sword_type == "bronze":
            return Sword("iron")
        elif self.sword_type == other.sword_type == "iron":
            return Sword("steel")
        else:
            raise Exception("can not craft")
        

'''As we discussed in the last assignment, operator overloading is the practice of defining custom behavior for standard Python operators. 
Here's a list of how the operators translate into method names.'''

# Operation	             Operator	        Method
# Addition	                +	             add
# Subtraction	            -	             sub
# Multiplication            *	             mul
# Power	                    **	             pow
# Division	                /	             truediv
# Floor Division	        //	             floordiv
# Remainder (modulo)	    %	             mod
# Bitwise Left Shift	    <<	             lshift
# Bitwise Right Shift	    >>	             rshift
# Bitwise AND	            &	             and
# Bitwise OR	            |	             or
# Bitwise XOR	            ^	             xor
# Bitwise NOT	            ~	             invert


# OVERLOADING BUILT-IN METHODS
'''Last but not least, let's take a look at some of the built-in methods we can overload in Python. 
While there isn't a default behavior for the arithmetic operators like we just saw, there is a default behavior for printing a class.'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
print(p1)
# prints "<Point object at 0xa0acf8>"


'''That's not super useful! Let's teach instances of our Point object to print themselves. The __str__ method (short for "string") lets us do just that. 
It takes no inputs but returns a string that will be printed to the console when someone passes an instance of the class to Python's print() function.
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

p1 = Point(4, 5)
print(p1)
# prints "(4,5)"

class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return(f"I am {self.name}, the {self.color} dragon")
    

# RANKING THE CARDS
# Exactly! By converting the ranks and suits to numerical values based on their positions in the RANKS and SUITS lists, we can easily compare them.

import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    # The equality operator needs to return True if both the rank and suit of two cards are the same:
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    # The less-than operator needs to compare ranks first. If they are the same, it needs to compare suits:
    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    # The greater-than operator follows the same logic, but checks if one card is greater than the other:
    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"



import random


class CardGame:
    def __init__(self):
        self.deck = DeckOfCards()
        self.deck.shuffle_deck()
        
    def play(self):
        print("Nothing to play...")


class War(CardGame):
    def __init__(self):
        super().__init__()
        self.player1_hand = []
        self.player2_hand = []
        
        
    def play(self):
        self.player1_hand = self.__deal_hand()
        self.player2_hand = self.__deal_hand()
        self.__battle()

    def __deal_hand(self):
        hand = []
        for _ in range(5):
            hand.append(self.deck.deal_card())
        return hand

    # don't touch below this line

    def __battle(self):
        player1_pile = []
        player2_pile = []
        player1_score = 0
        player2_score = 0
        ties = 0
        while len(self.player1_hand) > 0 or len(self.player2_hand) > 0:
            if len(self.player1_hand) == 0:
                random.shuffle(player1_pile)
                self.player1_hand = player1_pile.copy()
                player1_pile.clear()
            if len(self.player2_hand) == 0:
                random.shuffle(player2_pile)
                self.player2_hand = player2_pile.copy()
                player2_pile.clear()
            card1 = self.player1_hand.pop()
            card2 = self.player2_hand.pop()
            print(f"{card1} vs {card2}")
            if card1 > card2:
                player1_pile.append(card1)
                player1_pile.append(card2)
                player1_score += 1
                print(f"Player 1 wins with {card1}")
            elif card2 > card1:
                player2_pile.append(card1)
                player2_pile.append(card2)
                player2_score += 1
                print(f"Player 2 wins with {card2}")
            else:
                ties += 1
                print("Tie! Both players draw a card and play again")
        print("------------------------------------------")
        print("Game over!")
        print("------------------------------------------")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")
        print(f"Ties: {ties}")
        print("==========================================")


SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def index_of(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return None


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __cmp(self, other):
        self_suit_i = index_of(SUITS, self.suit)
        other_suit_i = index_of(SUITS, other.suit)
        self_rank_i = index_of(RANKS, self.rank)
        other_rank_i = index_of(RANKS, other.rank)
        if self_rank_i > other_rank_i:
            return "gt"
        if self_rank_i < other_rank_i:
            return "lt"
        if self_suit_i > other_suit_i:
            return "gt"
        if self_suit_i < other_suit_i:
            return "lt"
        return "eq"

    def __eq__(self, other):
        return self.__cmp(other) == "eq"

    def __gt__(self, other):
        return self.__cmp(other) == "gt"

    def __lt__(self, other):
        return self.__cmp(other) == "lt"

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class DeckOfCards:
    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.__cards.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop(0)


def test(seed):
    random.seed(seed)
    war = War()
    war.play()


def main():
    test(1)
    test(2)


main()

'''
WHAT IS FUNCTIONAL PROGRAMMING?
Functional programming is a style (or "paradigm" if you're pretentious) of programming where we compose functions instead of mutating state (updating the value of variables).

Functional programming is more about declaring what you want to happen, rather than how you want it to happen.
Imperative (or procedural) programming declares both the what and the how.
'''


# Example of imperative code:

car = create_car()
car.add_gas(10)
car.clean_windows()


# Example of functional code:

# return clean_windows(add_gas(create_car()))


'''The important distinction is that in the functional example, we never change the value of the car variable, 
we just compose functions that return new values, with the outermost function, clean_windows in this case, returning the final result.
'''

'''
DOC2DOC
In this course, we're working on "Doc2Doc", a command line tool for converting documents from one format to another. If you're familiar with Pandoc, the idea is similar.
'''

def stylize_title(document):
    return (add_border(center_title(document)))


# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)


'''
FUNCTIONAL VS OOP
Functional programming and object-oriented programming are styles for writing code. One isn't inherently superior to the other, 
but to be a well-rounded developer you should understand both well and use ideas from each when appropriate.

You'll encounter developers who love functional programming and others who love object-oriented programming. However, contrary to popular opinion,
 FP and OOP are not always at odds with one another. They aren't opposites. Of the four pillars of OOP, inheritance is the only one that doesn't fit with functional programming.

Inheritance isn't seen in functional code due to the mutable classes that come along with it. Encapsulation, polymorphism and abstraction are still used all the time in functional programming.

When working in a language that supports ideas from both FP and OOP (like Python, JavaScript, or Go) 
the best developers are the ones who can use the best ideas from both paradigms effectively and appropriately.
'''




def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    new_tuple = documents + (new_doc,)
    return new_tuple


# Existing documents tuple
documents = ("0. This is the first document", "1. This is the second document")

# New document to add
new_document = "This is the third document"

# Add the new document with the prefix
updated_documents = add_prefix(new_document, documents)

print(updated_documents)



'''
Immutable data is easier to think about and work with. When 10 different functions have access to the same variable, and you're debugging a problem with that variable, 
you have to consider the possibility that any of those functions could have changed the value.

When a variable is immutable, you can be sure that it hasn't changed since it was created. It's a helluva lot easier to work with.

Generally speaking, immutability means fewer bugs and more maintainable code.

TUPLES VS LISTS
Tuples and lists are both ordered collections of values, but tuples are immutable and lists are mutable.

You can append to a list, but you can not append to a tuple. You can create a new copy of a tuple using values from an existing tuple, but you can't change the existing tuple.
'''


# LISTS ARE MUTABLE
ages = [16, 21, 30]
# 'ages' is being changed in place
ages.append(80)
# [16, 21, 30, 80]

# TUPLES ARE IMMUTABLE
ages = (16, 21, 30)
more_ages = (80,) # note the comma! It's required for a single-element tuple
# 'all_ages' is a brand new tuple
all_ages = ages + more_ages
# (16, 21, 30, 80)



# IMPERATIVE STYLING
'''Unlike functional programming (and CSS), a lot of code is imperative. We write out the exact step-by-step implementation details.
 This Python script draws a red button on a screen using the Tkinter library:
'''

from tkinter import * # first, import the library
master = Tk() # create a window
master.geometry("200x100") # set the window size
button = Button(master, text="Submit", fg="red").pack() # create a button
master.mainloop() # start the event loop



# DECLARATIVE STYLING
# The following CSS changes all button elements to have red text:

button {
    color: red;
}

# It does not execute line-by-line like an imperative language. Instead, it simply declares the desired style, and it's up to a web browser to figure out how to apply and display it.


avg = Σx/N

# To put this calculation in plain English:

# Σ is just the Greek letter Sigma, and it represents "the sum of a collection".
# x is the collection of numbers we're averaging.
# N is the number of elements in the collection.
# avg is equal to the sum of all the numbers in collection "x" divided by the number of elements in collection "x".

# So, the equation really just says that avg is the average of all the numbers in collection "x". 


# This math equation is a declarative way of writing "calculate the average of a list of numbers". Here's some imperative Python code that does the same thing

def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)


# However, with functional programming, we would write code that's a bit more declarative:

# Here we're not keeping track of state (the total variable in the first example is "stateful"). We're simply composing functions together to get the result we want.

def get_average(nums):
    return sum(nums) / len(nums)


def get_median_font_size(font_sizes):
    sorted_list = sorted(font_sizes)
    list_length = len(sorted_list)
    
    if list_length == 0:
        return None
    median_index = (list_length - 1) // 2

    if list_length % 2 == 0:
        return min(sorted_list[median_index], sorted_list[median_index] + 1)
    else:
        return sorted_list[median_index]

'''
EXPLANATION:

- Line with sorted(font_sizes): This sorts the list and stores it in sorted_list.
- Line with len(sorted_list): This gets the length of the sorted list.
- Line with if list_length == 0:: This checks if the list is empty and returns None if so.
- Line with median_index = (list_length - 1) // 2:: This finds the index of the middle element.
- Line with if list_length % 2 == 0:: This checks if the list length is even.
- If true, it compares the two middle elements and returns the smaller one.
- Line with else:: This handles the case where the list length is odd and returns the single middle element.
'''


'''
- .replace(old, new) can be used to replace all instances of a character in a string.
- .upper() capitalizes an entire string, .capitalize() capitalizes the first letter.
- .strip() removes whitespace from the beginning and end of a string, .lstrip() and .rstrip() remove whitespace from the left and right respectively.
'''

# original/bugged
def format_line(line):
    return f"{line.rstrip().capitalize().replace(',', '')}...."

# corrected/ debugged
def format_line(line):
    return f"{line.strip().upper().replace('.', '')}..."



# In Python, functions are just values, like strings, integers, or objects. For example, we can assign an existing function to a variable:



def add(x, y):
    return x + y

# assign the function to a new variable
# called "addition". It behaves the same
# as the original "add" function
addition = add
print(addition(2, 5))
# 7


# Assignment 
def file_to_prompt(file, to_string):
    new_string = to_string(file)
    return (f"```\n{new_string}\n```")

'''TESTING IT'''

# Sample file dictionary
sample_file = {
    "filename": "sample.txt",
    "content": "This is a test content.",
    "author_first_name": "Alice",
    "author_last_name": "Wonderland",
}

# Sample to_string function
def to_string(file):
    return (
        f"File: {file['filename']}\n"
        f"Author: {file['author_first_name']} {file['author_last_name']}\n"
        f"Content: {file['content']}"
    )

# Call your file_to_prompt function
result = file_to_prompt(sample_file, to_string)

# Print the result
print(result)





'''
ANONYMOUS FUNCTIONS
Anonymous functions have no name, and in Python, they're called lambda functions after lambda calculus. Here's a lambda function that takes a single argument x and returns the result of x + 1:
'''

lambda x: x + 1

'''
Notice that the expression x + 1 is returned automatically, no need for a return statement. And because functions are just values, we can assign the function to a variable named add_one:
'''

add_one = lambda x: x + 1
print(add_one(2))
# 3


'''
Lambda functions might look scary, but they're still just functions. Because they simply return the result of an expression, they're often used for small, simple evaluations.
 Here's an example that uses a lambda to get a value from a dictionary after modifying the key:
'''

get_age = lambda name: {
    'lane_age': 29,
    'hunter_age': 69,
    'allan_age': 17
}.get(name + '_age', 'not found')
print(get_age('lane'))
# 29


# ASSIGNMENT 

def filename_getter(name_extension_tuples):
    # Step 1: Create an empty dictionary
    map_dict = {}
    
    # Step 2: Loop through each tuple in the input list
    for doc_type, extensions in name_extension_tuples:
        # Step 3: Loop through each extension in the list of extensions
        for ext in extensions:
            # Step 4: Add the extension to the dictionary with the document type as the value
            map_dict[ext] = doc_type
    
    # Return the lambda function
    return lambda ext: map_dict.get(ext, "Unknown")


'''
A programming language "supports first-class functions" when functions are treated like any other variable. 
That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables.

First-class function: A function that is treated like any other value
Higher-order function: A function that accepts another function as an argument or returns a function
Python supports first-class and higher-order functions.
'''

# FIRST-CLASS EXAMPLE
def square(x):
    return x * x

# Assign function to a variable
f = square

print(f(5))
# 25


# HIGHER-ORDER EXAMPLE
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]

'''
"Map", "filter", and "reduce" are three commonly used higher-order functions in functional programming.

In Python, the built-in map function takes a function and an iterable (in this case a list) as inputs. 
It applies the function to each element in the iterable and returns a new iterable with all the results.
'''

# With map, we can operate on lists without using loops and nasty stateful variables. For example:

def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]

# The list type constructor, list() converts the map object back into a standard list.

# "map" higher order function 

def change_bullet_style(document):
    doc_lines = document.split("\n")
    new_bullet = map(convert_line, doc_lines)
    rejoined_doc = "\n".join(new_bullet)
    return rejoined_doc
    


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

'''
 .split() and .join() to split the document into a list of lines, and then join the lines back together. This should preserve the original line breaks.
'''

# my_document is a string with newlines
# Example
lines_list = my_document.split("\n")

rejoined_doc = "\n".join(lines_list)



def remove_invalid_lines(document):
    new_list = document.split("\n")
    valid_lines = list(filter(lambda x: not x.startswith("-"), new_list))
    return "\n".join(valid_lines)



'''
The built-in functools.reduce() function takes a function and a list of values, and applies the function to each value in the list, accumulating a single result as it goes
'''

# import functools from the standard library
import functools

def add(sum_so_far, x):
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers = [1, 2, 3, 4]
sum = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10


import functools


def join(doc_so_far, sentence):
    return (doc_so_far + ". " + sentence)

def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    firs_n_sentence = sentences[:n]
    com_sentence = functools.reduce(join, firs_n_sentence)
    return com_sentence + "."



# Take a look at this imperative code that calculates the factorial of a number:

def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Here's the same factorial function using reduce:

import functools

def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))


# INTERSECT

# The .intersection() method calculates the intersection of two sets.
# The intersection of two sets is a new set that contains all of the elements that are in both original sets

# For example:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
print(c)
# {3, 4}


def get_common_formats(formats1, formats2):
    formats1_set = set(formats1) # Converts a ist to a set
    formats2_set = set(formats2)
    return formats1_set.intersection(formats2_set) # Using the .intersection method which can only be used on sets.



# ZIP

# The zip function takes two iterables (in this case lists), and returns a new iterable where each element is a tuple containing one element from each of the original iterables.

a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]



valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    zipped = list(zip(doc_names, doc_formats))
    filter_tuples = list(filter(lambda x: x[1] in valid_formats, zipped)) # x[1] is accessing the second element in my zipped tuple and compairing it to valid_formats
    return filter_tuples


# PURE FUNCTIONS

# A pure function has two properties:

# It always returns the same value given the same arguments.
# Its evaluation has no side effects

# EXAMPLE

def findMax(nums):
    max_val = float('-inf')
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val



# EXAMPLE OF AN IMPURE FUNCTION (impure becasue it has variabes outside of the function that get called to and can be mutated)

# instead of returning a value
# this function modifies a global variable
global_max = float('-inf')

def findMax(nums):
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num

# PURE FUNCTION


def convert_file_format(filename, target_format):
    valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
    valid_conversions = {
    "docx": ["pdf", "txt", "md"],
    "pdf": ["docx", "txt", "md"],
    "txt": ["docx", "pdf", "md"],
    "pptx": ["ppt", "pdf"],
    "ppt": ["pptx", "pdf"],
    "md": ["docx", "pdf", "txt"],
    }
    current_format = filename.split(".")[-1]
    if (
        current_format in valid_extensions
        and target_format in valid_conversions[current_format]
    ):
        return filename.replace(current_format, target_format)
    return None


'''
REFERENCE VS. VALUE
When you pass a value into a function as an argument, one of two things can happen:

It's passed by reference: The function has access to the original value and can change it
It's passed by value: The function only has access to a copy. Changes to the copy within the function don't affect the original
There is a bit more nuance, but this explanation mostly works.

These types are passed by reference:

Lists
Dictionaries
Sets
These types are passed by value:

Integers
Floats
Strings
Booleans
Tuples
Most collection types are passed by reference (except for tuples) and most primitive types are passed by value.
'''

# EXAMPLE OF PASS BY REFERENCE (MUTABLE)

def modify_list(inner_lst):
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because lst is a reference to the original

outer_lst = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]


# EXAMPLE OF PASS BY VALUE (IMMUTABLE)

def attempt_to_modify(inner_num):
    inner_num += 1
    # the original "outer_num" is not updated
    # because num is a copy of the original

outer_num = 1
attempt_to_modify(outer_num)
# outer_num = 1



# Creating a new dictionary using .copy() to not modify the original
# CORRECT
def add_format(default_formats, new_format):
    updated_dict = default_formats.copy()
    updated_dict[new_format] = True
    return updated_dict


def remove_format(default_formats, old_format):
    updated_dict = default_formats.copy()
    updated_dict[old_format] = False
    return updated_dict

# THIS IS INCORRECT AND MODIFYS THE ORIGINAL DICTIONARY:
def add_format(default_formats, new_format):
    default_formats[new_format] = True
    return default_formats


def remove_format(default_formats, old_format):
    default_formats[old_format] = False
    return default_formats


'''
The term "i/o" stands for input/output. In the context of writing programs, i/o refers to anything in our code that interacts with the "outside world". 
"Outside world" just means anything that's not stored in our application's memory (like variables).

EXAMPLES OF I/O
Reading from or writing to a file on the hard drive
Accessing the internet
Reading from or writing to a database
Even simply printing to the console is considered i/o!
All i/o is a form of "side effect".
'''


def convert_case(text, target_format):
    if not text or not target_format:
        raise ValueError(f"No text or target format provided")

    if target_format == "uppercase":
        return (text.upper())
    if target_format == "lowercase":
        return (text.lower())
    if target_format == "titlecase":
        return (text.title())
    raise ValueError(f"Unsupported format: {target_format}")



'''
In functional programming, i/o is viewed as dirty but necessary. We know we can't eliminate i/o from our code, so we just contain it as much as possible. 
There should be a clear place in your project that does nasty i/o stuff, and the rest of your code can be pure.

For example, a Python program might:

Read a file from the hard drive as the program starts
Run a bunch of pure functions to analyze the data
Write the results of the analysis to a file on the hard drive at the end
'''






















