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


