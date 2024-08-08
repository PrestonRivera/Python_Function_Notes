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



# WHILE LOOPS


def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1  # Increases current_health by 1
        enemy_distance -= 2  # Decreases enemy_distance by 2
    return current_health  # Returns the final value of current_health


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


# Dictionary comprehensions

# {key_expression: value_expression for item in iterable}



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



# Splitting document into pages using reduce funciton
 
from functools import reduce


def paginator(page_length):
    def paginate(document):
        words = document.split()
        def add_word_to_pages(pages, word):
            if not pages:
                return [word]
            current_page = pages[-1]
            if len(current_page) + len(word) + 1 > page_length:
                pages.append(word)
            else:
                pages[-1] = current_page + " " + word
            return pages
        return reduce(add_word_to_pages, words, [])
    return paginate


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


keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
]


def index_keywords(document, index):
    
    index_copy = index.copy()
    if document in index_copy:
        return index_copy[document], index_copy
    found_keywords = find_keywords(document)
    index_copy[document] = found_keywords
    return found_keywords, index_copy


def find_keywords(document):
    keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
    ]
    found_keywords = [keyword for keyword in keywords if keyword in document]
    return found_keywords



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


'''
NO-OP
A no-op is an operation that does... nothing.

If a function doesn't return anything, it's probably impure. If it doesn't return anything, the only reason for it to exist is to perform a side effect.
'''


# EXAMPLE NO-OP

# This function performs a useless computation because it doesn't return anything or perform a side-effect. It's a no-op.

def square(x):
    x * x


# EXAMPLE SIDE-EFFECT
# This function performs a side effect. It changes the value of the y variable that outside of its scope. It's impure.

y = 5
def add_to_y(x):
    global y
    y += x

add_to_y(3)
# y = 8



def remove_emphasis_from_word(word):
    remove_from_word = word.strip('*')
    return remove_from_word

def remove_emphasis_from_line(line):
    split_line = line.split()
    remove_emp = map(remove_emphasis_from_word, split_line)
    return ' '.join(remove_emp)
    


def remove_emphasis(doc_content):
    doc_lines = doc_content.split("\n")
    remove_emp = map(remove_emphasis_from_line, doc_lines)
    rejoin_doc = "\n".join(remove_emp)
    return rejoin_doc



# MEMOIZATION
'''At its core, memoization is just caching (storing a copy of) the result of a computation so that we don't have to compute it again in the future.'''

# For example, take this simple function:

def add(x, y):
    return x + y

'''
A call to add(5, 7) will always evaluate to 12. So, if you think about it, once we know that add(5, 7) can be replaced with 12,
we can just store the value 12 somewhere in memory so that we don't have to do the addition operation again in the future. Then, if we need to add(5, 7) again, we can just look up the value 12 instead of doing a (potentially expensive) CPU operation.

The slower and more complex the function, the more memoization can help speed things up.

Note: It's pronounced "memOization", not "memORization". This confused me for quite a while in college, I thought my professor just didn't speak goodly...
'''



def word_count_memo(document, memos):
    copied_memos_dict = memos.copy() # copied the memos dictionary
    if document in copied_memos_dict: # here I check to see if the document is already in the dictionary and if so return the word count and the dictionary
        return copied_memos_dict[document], copied_memos_dict # (copied_memos_dict[document]) is accessingand returning the value of the key in the dictionary and copied_memos_dict is returning the dictionary
    
    doc_word_count = word_count(document) # if the doc is not in the dictionary then i call the word count function on it
    copied_memos_dict[document] = doc_word_count # here i add the new doc and word count to the dictionary
    return doc_word_count, copied_memos_dict # here i return word count for the new doc and the updated dictionary


# Don't edit below this line


def word_count(document): # word count function
    count = len(document.split())
    return count


# exaple of creating dict from a list:

students_scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 90)]

students_dict = {}

for student, score in students_scores:
    students_dict[student] = score
print(students_dict)


# Recursion

'''Recursion is a famously tricky concept to grasp, but it's honestly quite simple - don't let it intimidate you! A recursive function is just a function that calls itself!'''

def sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum(nums[1:])

print(sum([1, 2, 3, 4, 5]))
# 15


def print_chars(word, i):
    if i == len(word):
        return
    print(word[i])
    print_chars(word, i + 1)

print_chars("Hello", 0)
# H
# e
# l
# l
# o




def factorial_r(x):
    if x == 0:
        return 1
    return x * factorial_r(x - 1)



## ASSIGNMENT

def zipmap(keys, values):
    # Base case: if either list is empty, return an empty dictionary
    if len(keys) == 0 or len(values) == 0:
        return {}
    
    # Recursive call: get the dictionary for the remaining elements
    smaller_dict = zipmap(keys[1:], values[1:])
    
    # Update dictionary with the first key-value pair
    smaller_dict[keys[0]] = values[0]
    
    # Return the updated dictionary
    return smaller_dict




# Example

def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)




def sum_nested_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested_list(item)  # Add the sum of the nested list to total
        else:
            total += item  # Add the integer to total
    return total  # Return the total after the loop



# RECURSION ON A TREE
# Recursion is often used in "tree-like" structures. For example:

# Nested dictionaries
# File systems
# HTML documents
# JSON objects

# That's because trees can have unknown depth. It's hard to write a series of loops because you don't know how many levels deep the tree goes.


def list_files(current_filetree, current_path=""): # cureent_filetree is a dictionary and current_path="" is a string representing the current path
    file_paths = []
    for node in current_filetree:
        if current_filetree[node] is None:
            file_paths.append(current_path + "/" + node)
        else:
            file_paths.extend(list_files(current_filetree[node], current_path + "/" + node)) 
    return file_paths


'''
STEPS
Create an empty list to store the file paths.

For each "node" in the current dictionary (just use a loop):

If the node's entry is None (meaning it's a final file, not a directory), append the full path for that node to the list.

Otherwise, extend the file list with the results of a recursive list_files call.

The new current_filetree for the recursive call is the one nested under the current node.

The new current_path should be the old one with the new node's name added after a slash. e.g. old_current_path/node_name.

Return the list of file paths.
'''



def count_nested_levels(nested_documents, target_document_id, level=1):
    # Iterate through each key in the dictionary
    for document_id in nested_documents:
        # If the document id matches the target, return the current level
        if document_id == target_document_id:
            return level
        # Recursively search in the nested dictionaries
        found_level = count_nested_levels(nested_documents[document_id], target_document_id, level + 1)
        # If the target document is found in nested levels, return the found level
        if found_level != -1:
            return found_level
    # If the target document is not found in any nested level, return -1
    return -1



def reverse_string(s):
    if s == "":
        return ""  # Base case: reversing an empty string results in an empty string
    # Recursive case: call reverse_string on the rest of the string and add the first character at the end
    return reverse_string(s[1:]) + s[0]



# FUNCTION TRANSFORMATIONS
# "Function transformation" is just a more concise way to describe a specific type of higher order function. 
# It's when a function takes a function (or functions) as input and returns a new function. Let's look at an example:

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# self_math is a higher order function
# input: a function that takes two arguments and returns a value
# output: a new function that takes one argument and returns a value
def self_math(math_func):
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10


# ASSIGNMENT


def get_logger(formatter):
    def inner_func(first, second):
        print(formatter(first, second))
    return inner_func


# Don't edit below this line


def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()


# ASSIGNMENT

def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_func(filename, content):
        # Split the filename and get the last part as the file extension
        file_extension = filename.split(".")[-1]
        # Check if the file extension is in the list of valid formats
        if file_extension in valid_formats:
            return conversion_function(content)
        # Raise an error if the file extension is not valid
        raise ValueError("Invalid file format")
    return inner_func

# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]

# FORMATTER

def formatter(pattern):
    def inner_func(text):
        result = ""
        i = 0
        while i < len(pattern):
            if pattern[i:i+2] == '{}':
                result += text
                i += 2
            else:
                result += pattern[i]
                i += 1
        return result
    return inner_func

# Now we can create new formatters easily:

bold_formatter = formatter("**{}**")
italic_formatter = formatter("*{}*")
bullet_point_formatter = formatter("* {}")

# And use them like this:

print(bold_formatter("Hello"))
# **Hello**
print(italic_formatter("Hello"))
# *Hello*
print(bullet_point_formatter("Hello"))
# * Hello


# CLOSURES
# 90% of the time, when I use function transformations, it's because I want to create a closure. We'll talk about closures in the next chapter!

# A closure is a function that references variables from outside its own function body. The function definition and its environment are bundled together into a single entity.
# Put simply, a closure is just a function that keeps track of some values from the place where it was defined, no matter where it is executed later on.


# The concatter() function returns a function called doc_builder (yay higher-order functions!) that has a reference to an enclosed doc value.

def concatter():
	doc = ""
	def doc_builder(word):
		# "nonlocal" tells Python to use the 'doc'
		# variable from the enclosing scope
		nonlocal doc # Python has a keyword called nonlocal that's required to access variables from an enclosing scope. Most programming languages don't require this keyword, but Python does.
		doc += word + " "
		return doc
	return doc_builder

# save the returned 'doc_builder' function
# to the new function 'harry_potter_aggregator'
harry_potter_aggregator = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Mr. and Mrs. Dursley of number four, Privet Drive

# When concatter() is called, it creates a new "stateful" function that remembers the value of doc it's internal doc variable. 
# Each successive call to harry_potter_aggregator appends to that same doc.


def word_count_aggregator():
    word_count = 0
    def calc_word_count(doc):
        nonlocal word_count
        word_count += len(doc.split())
        return word_count
    return calc_word_count
    
            
aggregator = word_count_aggregator()

print(aggregator("hello world")) # word_count = 2
print(aggregator("this is another test")) # word_count = 6

# The whole point of a closure is that it's stateful. It's a function that "remembers" the values from the enclosing scope even after the enclosing scope has finished executing.

def new_collection(initial_docs):
    closed_list = initial_docs.copy()
    def inner_function(string):
        nonlocal closed_list
        closed_list.append(string)
        return closed_list
    return inner_function


def new_clipboard(initial_clipboard):
    clipboard = initial_clipboard.copy() # Copy original dictionary
    
    def copy_to_clipboard(key, value):
        clipboard[key] = value # Add key value pairs to the copied dictionary
        
    def paste_from_clipboard(key):
        if key in clipboard: # If the key is in dictionary
            return clipboard[key] # Return its value
        return "" # If key not in dictionary return empty string
        
    return copy_to_clipboard, paste_from_clipboard # return the two functions


# selector is the first key and its value should be a dictionary.
# property is the key for the selector's dictionary and value is its value.


def css_styles(initial_styles):
    # Make a copy of the initial styles to avoid modifying the original dictionary
    styles = initial_styles.copy()

    # selector is the first key and its value should be a dictionary.
    # property is the key for the selector's dictionary and value is its value.    
    def add_style(selector, property, value):
        # If the selector is not in the styles dictionary, initialize it with an empty dictionary
        if selector not in styles:
            styles[selector] = {}
        # Add or update the property with the given value in the selector's dictionary
        styles[selector][property] = value
        # Return the updated styles dictionary
        return styles
    
    # Return the nested add_style function
    return add_style


# Spellchecker and ading words

def user_words(initial_words): # intitial_words is a tuple
    init_words_list = list(initial_words) # Convert tuple into a list
    def add_word(word): # Create the add word function
        init_words_list.append(word) # add words to the list
        return tuple(init_words_list) # change list back into a tuple and return it
    return add_word # return the add word funciton

 



def get_filter_cmd(filters):
    # This is the outer function. It takes a dictionary 'filters' as input.
    # 'filters' is expected to contain option strings as keys and the corresponding
    # filtering functions as values.
    
    def filter_cmd(content, options, word_pairs):
        # This is the inner function. It's defined inside get_filter_cmd and
        # will use the 'filters' dictionary passed to the outer function.
        # It takes three parameters:
        # - 'content': the string to be filtered.
        # - 'options': a list of filter option strings.
        # - 'word_pairs': a list of tuples for word replacements/removals, etc.

        if not options:
            # If the 'options' list is empty, raise an exception with the message
            # "missing options".
            raise Exception("missing options")

        for option in options:
            # Loop through each option in the 'options' list.
            if option in filters:
                # If the option is a valid key in the 'filters' dictionary,
                # apply the corresponding filter function to 'content'.
                # The function call 'filters[option](content, word_pairs)' replaces
                # 'content' with the filtered output.
                content = filters[option](content, word_pairs)
            else:
                # If the option is not a valid key in 'filters', raise an exception with
                # the message "invalid option".
                raise Exception("invalid option")

        # After applying all the specified filters, return the modified 'content'.
        return content

    # Return the 'filter_cmd' function when 'get_filter_cmd' is called.
    return filter_cmd

def replace_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[1])
    return content


def remove_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], "")
    return content


def capitalize_sentences(content, word_pairs):
    return ". ".join(map(str.capitalize, content.split(". ")))


def uppercase_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[0].upper())
    return content


filters = {
    "--replace": replace_words,
    "--remove": remove_words,
    "--capitalize": capitalize_sentences,
    "--uppercase": uppercase_words,
}


# CURRYING

# Function currying is a specific kind of function transformation where we translate a single function that accepts multiple arguments into multiple functions that each accept a single argument.


# This is a "normal" 3-argument function:

box_volume(3, 4, 5)

# This is a "curried" series of functions that does the same thing:

box_volume(3)(4)(5)


# Here's another example that includes the implementations:

def sum(a, b):
  return a + b

print(sum(1, 2))
# prints 3


# And the same thing curried:

def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# prints 3

# The sum function only takes a single input, a. It returns a new function that takes a single input, b. 
# This new function when called with a value for b will return the sum of a and b. We'll talk later about why this is useful.


def converted_font_size(font_size):
    def inner_funtion(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("Invalid doc type")
    return inner_funtion


# WHY CURRY?
# It's fairly obvious that:

def sum(a, b):
  return a + b

# is simpler than:

def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

# So why would we ever want to do the more complicated thing? Well, currying is often used to change a function's signature to make it conform to a specific shape. For example:

def colorize(converter, doc):
  # ...
  converter(doc)
  # ...

# The colorize function accepts a function called converter as input, and at some point during its execution, it calls converter with a single argument. 
# That means that it expects converter to accept exactly one argument. So, if I have a conversion function like this:

def markdown_to_html(doc, asterisk_style):
  # ...

# I can't use it with colorize because it wants two arguments. To solve this problem, I can curry markdown_to_html into a function that takes a single argument:

    def markdown_to_html(asterisk_style):
        def asterisk_md_to_html(doc):
        # do stuff with doc and asterisk_style...
            return asterisk_md_to_html

    markdown_to_html_italic = markdown_to_html('italic')
    colorize(markdown_to_html_italic, doc)


# Configure image size using min and max functions. 

def configure_image_size(max_width, max_height):
    def inner_function(min_width=0, min_height=0): # Set default values to zero
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        
        def innermost_function(width, height):
            new_width = min(max(width, min_width), max_width)  # Ensuring width is between min_width and max_width
            new_height = min(max(height, min_height), max_height)  # Ensuring height is between min_height and max_height
            
            return new_width, new_height  # Returning the constrained width and height
        
        return innermost_function  # Returning the innermost function itself
    
    return inner_function  # Returning the intermediate function itself

'''Innermost Call: max(height, min_height)
    This ensures height is at least min_height.

    Outermost Call: min(result, max_height)
    This ensures the result of the max call is at most max_height.
    
For height=1200:

max(1200, 600) results in 1200.
min(1200, 1080) results in 1080.'''


# Remember, currying is when we take a function that accepts multiple arguments:

final_volume = box_volume(3, 4, 5)
print(final_volume)
# 60

# And convert it into a series of functions that each accept a single argument:

final_volume = box_volume(3)(4)(5)
print(final_volume)
# 60

# box_volume(3) returns a new function that accepts a single integer and returns a new function
# box_volume(3)(4) returns another new function that accepts a single integer and returns a new function
# box_volume(3)(4)(5) returns the final result
# Here's another way of calling it, where each function is stored in a variable before being called:

with_length_3 = box_volume(3)
with_len_3_width_4 = with_length_3(4)
final_volume = with_len_3_width_4(5)
print(final_volume)
# 60

# Here are the function definitions:

def box_volume(length):
  def box_volume_with_len(width):
    def box_volume_with_len_width(height):
      return length * width * height
    return box_volume_with_len_width
  return box_volume_with_len




def lines_with_sequence(char): 
    # returns a function with one argument char
    def with_char(length): 
        # returns another function with one argument length
        sequence = char * length 
        # defines sequence with the functions arguments char * length
        def with_length(doc): 
            # returns another function with one argument doc
            split_doc = doc.split("\n") 
            # split the doc into multiple lines
            num_lines = 0 
            # creating a variable that i can add to when needed
            for line in split_doc: 
                # Looping through the split_doc 
                if sequence in line: 
                    # if statement to see if sequence is in line
                    num_lines += 1
                    # if sequence is in line add to the num_lines counter
            return num_lines 
        # return the num_lines value
        return with_length
    # return the function with_length
    return with_char 
# return the function with_char

# test
doc = """
aaaa
aabb
ccddaa
aaacccaa
acaca
"""

num_lines = lines_with_sequence("a")(2)(doc)
print(num_lines)


# same function but using reduce instead of for loop


from functools import reduce

def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length  # Create the sequence to search for by repeating 'char' 'length' times
        def with_length(doc):
            split_doc = doc.split("\n")  # Split the document into lines
            
            # Define the reducer function
            def reducer(count, line):
                if sequence in line:
                    return count + 1  # If the sequence is in the line, increment the count
                return count  # Otherwise, return the count unchanged
                
            # Use 'reduce' to apply the 'reducer' function to each line in 'split_doc', starting with an initial count of 0
            num_lines = reduce(reducer, split_doc, 0)
            
            return num_lines  # Return the final count of lines containing the sequence
        
        return with_length  # Return the inner function that processes the document
    
    return with_char  # Return the function that takes the length

# Example usage:
doc = """aaaa
bbbb
ccdd
aabb"""

num_lines = lines_with_sequence("a")(2)(doc)
print(num_lines) # Expected output: 2

#

def create_markdown_image(alt_text):
    alt_text_md = f"![{alt_text}]"
    def inner_function(url):
        escaped_url = url.replace("(", "%28").replace(")", "%29")
        enclosed_url = f"({escaped_url})"
        combined = alt_text_md + enclosed_url
        def innermost_function(title=None):
            if title:
                enclosed_title = f' "{title}"'
                return combined[:-1] + enclosed_title + ")"
            return combined
        return innermost_function
    return inner_function



### DECERATORS

# decerators are a Python-specific way of modifying functions.

'''Example:'''

def vowel_counter(func_to_decorate):
    vowel_count = 0
    def wrapper(doc):
        nonlocal vowel_count
        vowels = "aeiou"
        for char in doc:
            if char in vowels:
                vowel_count += 1
        print(f"Vowel count: {vowel_count}")
        return func_to_decorate(doc)
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("What")
# Vowel count: 1
# Document: What

process_doc("a wonderful")
# Vowel count: 5
# Document: a wonderful

process_doc("world")
# Vowel count: 6
# Document: world

'''
The @vowel_counter line is "decorating" the process_doc function with the vowel_counter function. vowel_counter is called once when process_doc is defined with the @ syntax,
but the wrapper function that it returns is called every time process_doc is called.
That's why vowel_count is preserved and printed after each time.
'''


# IT'S JUST SYNTACTIC SUGAR
# Decorators are just syntactic sugar for higher-order functions. 
# These two pieces of code are identical:

# WITH DECORATOR
@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("Something wicked this way comes")


# WITHOUT DECORATOR
def process(doc):
    print(f"Document: {doc}")

process_doc = vowel_counter(process)
process_doc("Something wicked this way comes")



# ASSIGNMENT for DECORATORS

def file_type_aggregator(func_to_decorate):
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper


# don't touch above this line

@file_type_aggregator
def process_doc(doc, file_type):
    return (f"Processing doc: '{doc}'. File Type: {file_type}")


from functools import lru_cache # lru_cache memoizes the inputs and outputs of the decorated function in a size-restricted dictionary

@lru_cache()
def is_palindrome(word):
    # Base case
    if len(word) <= 1:
        return True
    
    # Compare the first and last letters
    if word[0] != word[-1]:
        return False
    
    # Recursive call, examining the substring without the first and last letters
    return is_palindrome(word[1:-1]) # creates a substring starting from the second character up to, but not including, the last character.



### ARGS AND KWARGS

# In Python, *args and **kwargs allow a function to accept and deal with a variable number of arguments.

# *args collects positional arguments into a tuple
# **kwargs collects keyword (named) arguments into a dictionary


def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}


# Positional Arguments
# Positional arguments are the ones you're already familiar with, where the order of the arguments matters. Like this:

def sub(a, b):
    return a - b

# a=3, b=2
res = sub(3, 2)
# res = 1

# KEYWORD ARGUMENTS
# Keyword arguments are passed in by name. Order does not matter. Like this:

def sub(a, b):
    return a - b

res = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1

# A NOTE ON ORDERING
# Any positional arguments must come before keyword arguments. 

# This will not work:

sub(b=3, 2)

# The * and ** before args and kwargs in the function definition serve to unpack arguments when the function is called. Let's clarify the roles:

# FUNCTION DEFINITION
# When defining the function, *args and **kwargs tell Python to collect additional positional and keyword arguments into tuples and dictionaries, respectively:

def example_function(*args, **kwargs):
    print(args)
    print(kwargs)

# If you call
example_function(1, 2, 'apple', color='red', size='large')

# Inside the function:
# args = (1, 2, 'apple')
# kwargs = {'color': 'red', 'size': 'large'}



# FUNCTION CALL
# When calling a function:

# * unpacks a sequence (like a list or tuple) into positional arguments.
# ** unpacks a dictionary into keyword arguments.

# Example:

values = (1, 2, 3)
options = {'color': 'blue', 'size': 'small'}

example_function(*values, **options)

# Inside the function:
# args = (1, 2, 3)
# kwargs = {'color': 'blue', 'size': 'small'}


# INSIDE THE FUNCTION
# Once inside the function, args and kwargs are already collected, so you work directly with them as standard variables:

def example_function(*args, **kwargs):
    # args is a tuple
    for arg in args:
        print(arg)
    
    # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# To summarize:

# Function Definition: *args and **kwargs collect incoming arguments.
# Function Call: *values and **options unpack collections into arguments.
# Does this clarify why we don’t use * or ** within the function body?


# EXAMPLE WITHOUT *ARGS AND **KWARGS
# Without *args and **kwargs, you'd have to pack and unpack arguments manually:

def example_without(args, kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

args = (1, 2, 3)
kwargs = {'a': 'apple', 'b': 'banana'}

example_without(args, kwargs)

# Output:
# 1
# 2
# 3
# a: apple
# b: banana





# EXAMPLE WITH *ARGS AND **KWARGS
# With *args and **kwargs, passing arguments becomes much simpler:

def example_with(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_with(1, 2, 3, a='apple', b='banana')

# Output:
# 1
# 2
# 3
# a: apple
# b: banana

# The *args and **kwargs syntax is great for decorators that are intended to work on functions with different signatures.

# The log_call_count function below doesn't care about the number or type of the decorated function's (func_to_decorate) arguments. 
# It just wants to count how many times the function is called. However, it still needs to pass any arguments through to the wrapped function.

def log_call_count(func_to_decorate):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        # The * and ** syntax unpacks the arguments
        # and passes them to the decorated function
        return func_to_decorate(*args, **kwargs)

    return wrapper





def configure_plugin_decorator(func):
    def wrapper(*args):
        dictionary = dict(args)
        global_config = dict(
            map(lambda item: (func.__name__ + "." + item[0], item[1]), dictionary.items())
        )
        result = func(**dictionary)

        return result, global_config
    return wrapper

# Original dictionary
dictionary = {"path": "~/documents", "prefix": "copy_", "extension": ".md"}

# Function name pretending to be inside a function
func_name = "configure_backups"

# Transform each (key, value) to ("func_name.key", value)
transformed_items = map(lambda item: (func_name + "." + item[0], item[1]), dictionary.items())

# Convert the transformed items back to a dictionary
global_config = dict(transformed_items)

# global_config now looks like:
# {
#    "configure_backups.path": "~/documents",
#    "configure_backups.prefix": "copy_",
#    "configure_backups.extension": ".md"
# }












# BASIC SYNTAX
# enumerate(iterable, start=0)

# iterable: The sequence you want to loop over.
# start: The index from which to start (defaults to 0).

# EXAMPLE OF ENUMERATE
# Here’s an example to illustrate:

fruits = ['apple', 'banana', 'cherry']

# Without enumerate
index = 1
for fruit in fruits:
    print(f"{index}. {fruit}")
    index += 1

# With enumerate
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")








# Use the list() function to convert map results to a list
# Use the dict() function to convert map results to a dictionary
# The .items() method can be used on a dictionary to get an iterable of key-value tuple pairs
# The provided convert_md_to_txt function takes a string of Markdown text and returns a string of text with any "heading" symbols removed. For



def markdown_to_text_decorator(func):
    
    def wrapper(*args, **kwargs):
        converted_args = list(map(convert_md_to_txt, args)) 
        converted_kwargs = {k: convert_md_to_txt(v) for k, v in kwargs.items()}
        return func(*converted_args, **converted_kwargs)
    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)


# BREAKDOWN


def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        # Convert positional arguments
        converted_args = list(map(convert_md_to_txt, args))

        # Convert keyword arguments with dictionary comprehension
        converted_kwargs = {k: convert_md_to_txt(v) for k, v in kwargs.items()}

        # Call the original function with converted arguments
        return func(*converted_args, **converted_kwargs)

    return wrapper



# {key_expression: value_expression for item in iterable}

# {k: convert_md_to_txt(v) for k, v in kwargs.items()}


'''
Here's how you can use it:

for

k, v in kwargs.items(): This iterates over each key-value pair in the kwargs dictionary.

convert_md_to_txt(v): This expression converts each value (Markdown text) to plain text using convert_md_to_txt.
'''





# SUM TYPES


'''
As opposed to product types, which can have many (often infinite) combinations, sum types have a fixed number of possible values. For example, 
let's say we need to represent the "colors" a user can choose from:

RED
GREEN
BLUE

We could use a plain-old string to represent these values, but that's annoying because we have to remember all the "valid" values and defensively check for invalid ones all over our codebase.
The Enum module is generally better than a string or an int:
'''

# A "sum" type is the opposite of a "product" type. This Python object is an example of a product type:

# man.studies_finance = True
# man.has_trust_fund = False

# The total number of combinations a man can have is 4, the product of 2 * 2:

# studies_finance	has_trust_fund
#       True	        True
#       True	        False
#       False	        True
#       False	        False


# If we add a third attribute, perhaps a has_blue_eyes boolean, the total number of possibilities multiplies again, to 8!

# studies_finance	has_trust_fund	has_blue_eyes
#        True	        True	        True
#        True	        True	        False
#        True	        False	        True
#        True	        False	        False
#        False	        True	        True
#        False	        True	        False
#        False	        False	        True
#        False	        False	        False


# But let's pretend that we live in a world where there are really only three types of people that our program cares about:

# Dateable
# Undateable
# Maybe dateable
# We can reduce the number of cases our code needs to handle by using a (admittedly fake Pythonic) sum type with only 3 possible types:

class Person:
    def __init__(self, name):
        self.name = name

class Dateable(Person):
    pass

class MaybeDateable(Person):
    pass

class Undateable(Person):
    pass


# SUM_TYPE example
 
class MaybeParsed:
    pass


# don't touch above this line


class Parsed(MaybeParsed):
    def __init__(self, doc_name, text):
        self.doc_name = doc_name
        self.text = text
        same_name_prop = self.doc_name + self.text
        


class ParseError(MaybeParsed):
    def __init__(self, doc_name, err):
        self.doc_name = doc_name
        self.err = err
        same_name_prop = self.doc_name + self.err



# Then we can use the isinstance built-in function to check if a Person is an instance of one of the subclasses. It's a clunky way to represent sum types, but hey, it's Python.

def respond_to_text(guy_at_bar):
    if isinstance(guy_at_bar, Dateable):
        return f"Hey {guy_at_bar.name}, I'd love to go out with you!"
    elif isinstance(guy_at_bar, MaybeDateable):
        return f"Hey {guy_at_bar.name}, I'm busy but let's hang out sometime later."
    elif isinstance(guy_at_bar, Undateable):
        return "Have you tried being rich?"
    else:
        raise ValueError("invalid Person type")


from enum import Enum

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
print(Color.RED)  # this works, prints 'Color.RED'
print(Color.TEAL) # this raises an exception


'''
Now Color is a sum type! At least, as close as we can get in Python.

There are a few benefits:

A "Color" can only be RED, GREEN, or BLUE. If you try to use Color.TEAL, Python raises an exception.
There is a central place to see the "valid" values for a Color.
Each "Color" has a "name" (e.g. Color.RED) and a "value" (e.g. 1). The value is an integer and is used under the hood instead of the name. 
Integers take up less memory than strings, which helps with performance.
'''

from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    if status == CSVExportStatus.PENDING:
        return handle_pending(data)
    elif status == CSVExportStatus.PROCESSING:
        return handle_processing(data)
    elif status == CSVExportStatus.SUCCESS:
        return "Success!", data
    elif status == CSVExportStatus.FAILURE:
        prepared_data = handle_pending(data)[1]
        return "Unknown error, retrying...", handle_processing(prepared_data)[1]
    else:
        raise Exception("Unknown export status")



def handle_pending(data):
    converted_data = list(map(lambda lst: list(map(str, lst)), data))
    return "Pending...", converted_data

def handle_processing(data):
    csv_rows = map(lambda lst: ",".join(lst), data)
    csv_string = "\n".join(csv_rows)
    return "Processing...", csv_string

####


from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document, edit_type, edit):
    match edit_type:
        case EditType.NEWLINE:
            return handle_newline(document, edit)
        case EditType.SUBSTITUTE:
            return handle_substitute(document, edit)
        case EditType.INSERT:
            return handle_insert(document, edit)
        case EditType.DELETE:
            return handle_delete(document, edit)
        case _:
            raise Exception("Unknown edit type")

def handle_newline(document, edit):
    line_number = edit['line_number']
    lines = document.split("\n")
    if line_number >= len(lines):
        raise Exception("Invalid line number")
    lines[line_number] += "\n"
    return "\n".join(lines)


def handle_substitute(document, edit):
    line_number = edit["line_number"]
    start = edit["start"]
    end = edit["end"]
    insert_text = edit["insert_text"]
    lines = document.split("\n")
    
    if line_number >= len(lines):
        raise Exception("Invalid line number")
    if start > len(lines[line_number]):
        raise Exception("Invalid start index")
    if end > len(lines[line_number]) or end < start:
        raise Exception("Invalid end index")

    lines[line_number] = lines[line_number][:start] + insert_text + lines[line_number][end:]
    return "\n".join(lines)


def handle_insert(document, edit):
    insert_text = edit["insert_text"]
    line_number = edit["line_number"]
    start = edit["start"]
    lines = document.split("\n")

    if line_number >= len(lines):
        raise Exception("Invalid line number")
    if start > len(lines[line_number]):
        raise Exception("Invalid start index")

    lines[line_number] = lines[line_number][:start] + insert_text + lines[line_number][start:]
    return "\n".join(lines)


def handle_delete(document, edit):
    line_number = edit["line_number"]
    start = edit["start"]
    end = edit["end"]
    lines = document.split("\n")
    
    if line_number >= len(lines):
        raise Exception("Invalid line number")
    if start > len(lines[line_number]):
        raise exception("Invalid start index")
    if end > len(lines[line_number]) or end < start:
        raise Exception("Invalid end index")

    lines[line_number] = lines[line_number][:start] + lines[line_number][end:]
    return "\n".join(lines)


####

from enum import Enum

Doctype = Enum('Doctype', ['PDF', 'TXT', 'DOCX', 'MD', 'HTML'])


'''
Unfortunately, Python does not support sum types as well as some of the other statically typed languages.

Python does not enforce your types before your code runs. That's why we need this line here to raise an Exception if a color is invalid:
'''

def color_to_hex(color):
    if color == Color.GREEN:
        return '#00FF00'
    elif color == Color.BLUE:
        return '#0000FF'
    elif color == Color.RED:
        return '#FF0000'
    # handle the case where the color is invalid
    raise Exception('Unknown color')


# In a language like Rust we could write the same thing like this:
'''
fn color_to_hex(color: Color) -> String {
    match color {
        Color::Green => "#00FF00".to_string(),
        Color::Blue => "#0000FF".to_string(),
        Color::Red => "#FF0000".to_string(),
    }
}
'''

# Notice how there isn't any case for an unknown value? That's because the Rust code will fail to compile (a step that happens before the code runs at all) if the Color is a different value. 
# This static enforcement is a huge benefit of sum types, and it's a shame we can't get that in Python.


# MATCH

# WORKING WITH ENUMS

'''
Python has a match statement that tends to be a lot cleaner than a series of if/else/elif statements when we're working with 
a fixed set of possible values (like a sum type, or more specifically an enum):
'''

def get_hex(color):
    match color:
        case Color.RED:
            return "#FF0000"
        case Color.GREEN:
            return "#00FF00"
        case Color.BLUE:
            return "#0000FF"

        # default case
        # (invalid Color)    
        case _:
            return "#FFFFFF"

# If you have two values to match, you can use a tuple:

def get_hex(color, shade):
    match (color, shade):
        case (Color.RED, Shade.LIGHT):
            return "#FFAAAA"
        case (Color.RED, Shade.DARK):
            return "#AA0000"
        case (Color.GREEN, Shade.LIGHT):
            return "#AAFFAA"
        case (Color.GREEN, Shade.DARK):
            return "#00AA00"
        case (Color.BLUE, Shade.LIGHT):
            return "#AAAAFF"
        case (Color.BLUE, Shade.DARK):
            return "#0000AA"

        # default case
        # (invalid combination)
        case _:
            return "#FFFFFF"



def hex_to_rgb(hex_color):
    # Check if it's a valid hex color
    if not is_hexadecimal(hex_color) or len(hex_color) != 6:
        raise Exception("not a hex color")

    # Extract the red, green, and blue components
    red_component = hex_color[:2]
    green_component = hex_color[2:4]
    blue_component = hex_color[4:]

    # Convert each component to an integer using base 16
    red = int(red_component, 16)
    green = int(green_component, 16)
    blue = int(blue_component, 16)

    # Return the RGB values
    return red, green, blue

def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except ValueError:
        return False


def deduplicate_lists(lst1, lst2, reverse=False):
    combined_list = lst1 + lst2  # Step 1: Combine the lists
    deduplicate = set(combined_list)  # Step 2: Remove duplicates
    convert_list = list(deduplicate)  # Step 2: Convert set back to list
    return sorted(convert_list, reverse=reverse)  # Step 3: Sort the list

# example usage 
# For ascending order (default)
print(sorted([4, 2, 5, 1, 3]))  # Output: [1, 2, 3, 4, 5]

# For descending order
print(sorted([4, 2, 5, 1, 3], reverse=True))  # Output: [5, 4, 3, 2, 1]

from enum import Enum

class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return content.replace('# ', '<h1>') + '</h1>'
        case (DocFormat.TXT, DocFormat.PDF):
            return (f"[PDF] {content} [PDF]" )
        case (DocFormat.HTML, DocFormat.MD):
            return content.replace('<h1>', '# ').replace('</h1>', '') # Here I am chaining the .replace call together to apply both calls to the same string
            raise Exception("Invalid type")





def sort_dates(dates):
    return sorted(dates, key=format_date)


def format_date(date):
    month, day, year = date.split("-")
    return f"{year:0>4}-{month:0>2}-{day:0>2}"

'''Let's break it down:

0>4:
0 is the fill character. It means if the value is shorter than the specified width, pad it with zeros.
> is the alignment option. It ensures the padding characters (zeros) are added to the left of the number.
4 is the width. It specifies that the resulting string should be at least 4 characters long.'''








# to run the unittest framework, you'll typically use Python's command-line interface.

# You can run your test script with the following command in your terminal or command line:

# python -m unittest test_htmlnode.py


'''
Here is a step-by-step guide:

Ensure you're in the same directory as your test_htmlnode.py file.
Run the above command.
This will execute the test and show you whether it passed or failed.'''







# REGEX FOR A SINGLE WORD

import re

text = "I'm a little teapot, short and stout. Here is my handle, here is my spout."
matches = re.findall(r"teapot", text)
print(matches) # ['teapot']

r"teapot" is a regex pattern.
# The r tells Python to treat the string as a "raw" string, which means we don't have to escape backslashes
# The pattern teapot will match any exact occurrences of the word "teapot" in the input.


# REGEX FOR PHONE NUMBER
text = "My phone number is 555-555-5555 and my friend's number is 555-555-5556"
matches = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(matches) # ['555-555-5555', '555-555-5556']

# \d matches any digit
# {3} means "exactly three of the preceding character"
# - is just a literal - that we want to match


# REGEX FOR TEXT BETWEEN PARENTHESES
text = "I have a (cat) and a (dog)"
matches = re.findall(r"\((.*?)\)", text)
print(matches) # ['cat', 'dog']

# \( and \) are literal parentheses that we want to match
# .*? matches any number of characters (except for line terminators) between the parentheses


# REGEX FOR EMAILS
text = "My email is lane@example.com and my friend's email is hunter@example.com"
matches = re.findall(r"\w+@\w+\.\w+", text)
print(matches) # ['lane@example.com', 'hunter@example.com']

# \w matches any word character (alphanumeric characters and underscores)
# + means "one or more of the preceding character"
# @ is just a literal @ symbol that we want to match
# \. is a literal . that we want to match (The . is a special character in regex, so we escape it with a leading backslash)


#### I love regexr.com for interactive regex testing, it breaks down each part of the pattern and explains what it does.


def toggle_case(line):
    if line.istitle():
        return line.upper() + "!!!"
    if line.isupper():
        return line.capitalize().rstrip("!")
    if len(line) > 0 and line[1:].islower():
        return line.title()
    else:
        return line



print(toggle_case("live long and prosper"))  # Expected: "Live Long And Prosper"
print(toggle_case("...Khan"))                # Expected: "...KHAN!!!"
print(toggle_case("ILLogicaL"))              # Expected: "ILLOGICAL!!!"
print(toggle_case("BEAM ME UP, BOOTS!!!"))   # Expected: "Beam me up, boots"




# UNDERSTANDING HEXADECIMAL COLORS
'''Hexadecimal color codes are a way to represent colors using a base-16 numbering system. They are often used in web development and graphics. Here's a breakdown:

Hexadecimal System: Uses 16 symbols (0-9 and A-F).

0 in hexadecimal represents 0 in decimal.
A in hexadecimal represents 10 in decimal.
F in hexadecimal represents 15 in decimal.
Color Representation:

A hex color code is usually 6 characters long.
Each pair of characters represents the intensity of red, green, and blue, respectively.

EXAMPLE: #FFA07A
Let's take #FFA07A step by step:

Red Component: FF

F = 15 and F = 15
So FF in hexadecimal is 15 * 16 + 15 = 255 in decimal.

Green Component: A0

A = 10 and 0 = 0
So A0 in hexadecimal is 10 * 16 + 0 = 160 in decimal.

Blue Component: 7A

7 = 7 and A = 10
So 7A in hexadecimal is 7 * 16 + 10 = 122 in decimal.'''


def hex_to_rgb(hex_color):
    # Check if it's a valid hex color
    if not is_hexadecimal(hex_color) or len(hex_color) != 6:
        raise Exception("not a hex color")

    # Extract the red, green, and blue components
    red_component = hex_color[:2]
    green_component = hex_color[2:4]
    blue_component = hex_color[4:]

    # Convert each component to an integer using base 16
    red = int(red_component, 16)
    green = int(green_component, 16)
    blue = int(blue_component, 16)

    # Return the RGB values
    return red, green, blue

def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except ValueError:
        return False





# Originals and backups are tuples of document strings
def restore_documents(originals, backups):
    # Create a empty set
    combined_docs = set()

    # Loop through originals
    for doc in originals:
        # If doc is not a random numbers string
        if not doc.isdigit():
            # Add doc to combined_doc set
            combined_docs.add(doc.upper())
    # Loop through backups
    for doc in backups:
        # If doc is not a random number string
        if not doc.isdigit():
            # Add doc to combined_doc set
            combined_docs.add(doc.upper())
    return combined_docs




def find_longest_word(content, longest=""):
    # Check if `content` is empty (base case for recursion)
    if len(content) == 0:
        return longest

    # If `content` is a string
    if isinstance(content, str):
        # Split the string into words
        split_words = content.split()
        # Check if the first word is longer than the current longest word
        if len(split_words[0]) > len(longest):
            longest = split_words[0]
        # Recursively call the function with the remaining words
        return find_longest_word(split_words[1:], longest)

    # If `content` is a list
    if isinstance(content, list):
        # Recursively call the function with the first element of the list
        longest = find_longest_word(content[0], longest)
        # Recursively call the function with the rest of the list
        return find_longest_word(content[1:], longest)

    # Fallback return
    return longest



### ALGORITHMS ###

'''
An "algorithm" is simply a set of instructions to solve a particular problem. People use algorithms all the time, without even realizing it. 
If you've ever organized books on a shelf, packed your luggage for a trip, or followed a cooking recipe, then you've already used an algorithm!
'''

def find_minimum(nums):
    minimum = float("inf")
    if len(nums) == 0:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum


'''
WHAT IS AN ALGORITHM?
As we discussed, an algorithm is a finite sequence of well-defined, computer-implementable instructions. Algorithms are always unambiguous and are used as specifications for real world implementations. Wikipedia Definition

You'll often find algorithms written in what we call pseudocode (pronounced "soo-doe-code"), which is fake code that's meant to be more human readable. This makes it easier to implement the algorithm in whichever programming language you need.
'''

# In short, an algorithm is:

# Defined: there is a specific sequence of steps that performs a task
# Unambiguous: there is a "correct" and "incorrect" interpretation of the steps
# Implementable: it can be performed in code or using hardware


# Finding the sum of a list of numbers without using sum method. 

def sum(nums):
    sum = 0
    if len(nums) == 0:
        return None
    for num in nums:
        sum += num
    return sum



# Finding the average number in  a list of numbers 

def average_followers(nums):
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)


# Finding the median of a list of number.

def median_followers(nums):
    sorted_list = sorted(nums)
    list_len = len(sorted_list)
    index = (list_len - 1) // 2
    if len(sorted_list) == 0:
        return None
    elif (list_len % 2):
        return sorted_list[index]
    else:
        return (sorted_list[index] + sorted_list[index + 1])/ 2.0
    

# Exponents 

# An exponent indicates how many times a number is to be multiplied by itself.

# For example: 53 = 5 * 5 * 5

# Sometimes exponents are also written using the caret symbol (^):

# 5^3 = 53


# We can calculate exponents in Python using the ** operator. (Why not the ^ operator? Blame Fortran.)

square = 2 ** 2
# square = 4

cube = 2 ** 3
# cube = 8


'''
In the social media industry, there is a concept called "spread" - it refers to how much a post spreads due to "reshares" after all of the original author's followers see it. As it turns out, 
social media posts spread at an exponential rate! We've found that the estimated spread of a social post can be calculated using the following formula:

estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )

In the formula above, average_audience_followers refers to an average calculated from each number within the 
audiences_followers argument - which is a list containing the individual follower counts of the author's followers. For example, if audiences_followers = [2, 3, 2, 19], then:

- the author has 4 total followers
- each follower has their own 2, 3, 2, and 19 followers, respectively.

Complete the get_estimated_spread function by implementing the formula above. The only input is audiences_followers, which is a list of the follower counts of all the followers the author has. Return the estimated spread.
'''

def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    
    average_audiences_followers = sum(audiences_followers) / len(audiences_followers)

    if num_followers == 0:
        return None
    else:
        return average_audiences_followers * (num_followers ** 1.2)


# Using geometric sequence formula 

# "fitness" influencers: follower count quadruples each month
# "cosmetic" influencers: follower count triples each month
# All other influencers: follower count doubles each month
# Use a slightly modified geometric sequence formula: total = a1 * r^n

def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == 'fitness':
        r = 4
        return follower_count * (r**num_months)
    elif influencer_type == 'cosmetic':
        r = 3
        return follower_count * (r**num_months)
    else:
        r = 2
        return follower_count * (r**num_months)




## LOGARITHM

'''
A logarithm is the inverse of an exponent.

24 = 16

log216 = 4

"log216" can be read as "log base 2 of 16", and means "the number of times 2 must be multiplied by itself to equal 16".

"log216" can also be written as log2(16)

Some more examples:

log2(2) = 1
log2(4) = 2
log2(8) = 3
log2(16) = 4
log2(32) = 5
log10(100) = 2
log10(1000) = 3
log10(10000) = 4
'''


# LOGS (LOGARITHMS) IN PYTHON
# Just import the math library and use the math.log() function.

import math

print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")
# Logarithm base 2 of 16 is: 4.0

# ASSIGNMENT EXAMPLE

# average_engagement_percentage * log2(num_followers)

import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * (math.log(num_followers, 2))


# Import math module to use the math.factorial function.

import math

def num_possible_orders(num_posts):
    return math.factorial(num_posts)



## EXPONENTIAL DECAY

'''
In physics, exponential decay is a process where a quantity decreases over time at a rate proportional to its current value.

We've found that Instagram influencers tend to lose followers similarly. This means that the more followers you have, the faster you lose them.
'''

# ASSIGNMENT 

# remaining_total = quantity * ( retention_rate ^ time )

def decayed_followers(intl_followers, fraction_lost_daily, days):
    retention_rate = 1 - fraction_lost_daily
    final_value = intl_followers * (retention_rate**days)
    return final_value





import math

def log_scale(data, base):
    new_list = []

    for pos_n in data:
        get_log = math.log(pos_n, base)
        new_list.append(get_log)
    return new_list


#  BIG O NOTATION

'''
There are lots of existing algorithms; some are fast and some are slow. Some use lots of memory. It can be hard to decide which algorithm is the best to solve a particular problem. "Big O" analysis (pronounced "Big Oh", not "Big Zero") is one way to compare algorithms.

Big O is a characterization of algorithms according to their worst-case growth rates
'''


# We write Big-O notation like this:

# O(formula)

'''
Where formula describes how an algorithm's run time or space requirements grow as the input size grows.

O(1) - constant
O(n) - linear
O(n^2) - squared
O(2^n) - exponential
O(n!) - factorial

'''


# EXAMPLE O(N) - Order "N"

def find_max(nums):
    max = float("-inf")
    for num in nums:
        if num > max:
            max = num
    return max


# EXAMPLE O(n^2) - Order "n" squared


def does_name_exist(first_names, last_names, full_name):

    for first_name in first_names:
        for last_name in last_names:
            combined_name = first_name + " " + last_name
            if combined_name == full_name:
                return True
    return False


# EXAMPLE O(NM)

# O(nm) is very similar to O(n^2). The difference is that instead of a single input that we care about, there are 2. 
# If n and m increase at the same rate, then O(nm) is effectively the same as O(n^2). However, if n or m increases faster or slower, then it's useful to track their complexity separately.

# all_handles: a 2-dimensional list, or "list of lists" of strings representing instagram user handles on a per-influencer basis.
# brand_name: a string.

# get_avg_brand_followers returns the average number of handles that contain the brand_name across all the lists. Each list represents the audience of a single influencer.

# EXAMPLE INPUT/OUTPUT

all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmo"


def get_avg_brand_followers(all_handles, brand_name):
    handles_with_brand_name = 0
    
    for lists in all_handles:
        for handle in lists:
            if brand_name in handle:
                handles_with_brand_name += 1
    return handles_with_brand_name / len(all_handles)



'''
In Big O analysis we drop all constants because they don't affect the change in the runtime, just the runtime itself.

O(2 * n) -> O(n)

O(10 * n^2) -> O(n^2)
'''

# ORDER 1
# O(1) means that no matter the size of the input, there is no growth in the runtime of the algorithm. This is also referred to as a "constant time" algorithm.

# In Python, the dictionary data structure offers the ability to look items up by key, which is an operation that is independent of the size of the dictionary. In other words, dictionary lookups are O(1).



# O(1) with dictionary

def find_last_name(names_dict, first_name):
    if first_name in names_dict:
        last_name = names_dict[first_name]
    else:
        last_name = None
    return last_name

# OR

def find_last_name(names_dict, first_name):
    last_name = names_dict.get(first_name, None) # Using the .get method to access a key/value in a dictionary - value = dictionary.get(key) usage with default - value value = dictionary.get(key, default_value)
    return last_name



# BINARY SEARCH ALGORITHM

def binary_search(target, arr):
    n = len(arr)
    low = 0 
    high = n - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False

# BREAKDOWN

'''
Let's break it down step-by-step using the array [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] and target 10.

Initial Setup:

target = 10
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
low = 0
high = len(arr) - 1 = 9
FIRST ITERATION:
Calculate median:

median = (low + high) // 2 = (0 + 9) // 2 = 4
arr[median] = arr[4] = 9
Comparison:

arr[median] < target (i.e., 9 < 10)
So, we update low = median + 1 = 4 + 1 = 5
SECOND ITERATION:
Calculate median:

median = (low + high) // 2 = (5 + 9) // 2 = 7
arr[median] = arr[7] = 15
Comparison:

arr[median] > target (i.e., 15 > 10)
So, we update high = median - 1 = 7 - 1 = 6
THIRD ITERATION:
Calculate median:

median = (low + high) // 2 = (5 + 6) // 2 = 5
arr[median] = arr[5] = 11
Comparison:

arr[median] > target (i.e., 11 > 10)
So, we update high = median - 1 = 5 - 1 = 4
FOURTH ITERATION:
Now, low = 5 and high = 4.
Since low > high, the while loop condition low <= high is False and we exit the loop.
After exiting the loop, it returns False because we didn't find the target in the array.
'''

def count_names(list_of_lists, target_name):
    name_count = 0
    for list in list_of_lists:
        for name in list:
            if name == target_name:
                name_count += 1
    return name_count


# Rmoving duplicates from list

def remove_duplicates(nums):
    uniq_foll = []
    
    for num in nums:
        if num not in uniq_foll:
            uniq_foll.append(num)
    return uniq_foll


# Sorting algorithm


class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

# dont touch above this line

def vanity(influencer):
    inf_vanity = influencer.num_bio_links * 5 + influencer.num_selfies
    return inf_vanity

def vanity_sort(influencers):
    sorted_inf_list = sorted(influencers, key=vanity)
    return sorted_inf_list


# BUBBLE SORT

# Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted.

# Pseudocode for bubble sort:

# Procedure bubble_sort(nums):
    # Set swapping to True
    # Set end to the length of nums
    # While swapping is True:
        # Set swapping to False
        # For i from the 2nd element to end:
            # If the (i-1)th element of nums is greater than the ith element:
                # Swap the (i-1)th element and the ith element of nums
                # Set swapping to True
        # Reduce end by one
    # Return nums
# End Procedure

def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping is True:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums

# MERGE SORT

# Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort.

'''
# DIVIDE AND CONQUER
Merge sort is a divide and conquer algorithm.:

Divide: divide the large problem into smaller problems, and recursively solve the smaller problems
Conquer: Combine the results of the smaller problems to solve the large problem

In merge sort specifically we:

# DIVIDE

Divide the array into two (equal) halves
Recursively sort the two halves
# CONQUER

Merge the two halves to form a sorted array
merge sort gif

# ALGORITHM

The algorithm consists of two separate functions, merge_sort and merge.

merge_sort() divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

The merge() function is used for merging two sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each have a length of 1. 
Those single element lists will be merged into a sorted list of length two, and we can build from there.

# MERGE_SORT() IMPLEMENTATION

Input: A, a list of integers

If the length of A is less than 2, it's already sorted so return it
Split the input array into two halves down the middle
Call merge_sort() twice, once on each half
Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
MERGE() IMPLEMENTATION
Inputs: A, B. Two lists of integers

Create a new "final" list of integers.
Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other). Add those extra items to the final list.
Return the final list.
'''

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    list_a = nums[0:len(nums)//2]
    list_b = nums[len(nums)//2:]
    sorted_a = merge_sort(list_a)
    sorted_b = merge_sort(list_b)
    return merge(sorted_a, sorted_b)


def merge(first, second):
    final_list = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final_list.append(first[i])
            i += 1
        else:
            final_list.append(second[j])
            j += 1
    while i < len(first):
        final_list.append(first[i])
        i += 1
    while j < len(second):
        final_list.append(second[j])
        j += 1
    return final_list

# O(n*log(n)) Explained and why its better then O(n^2)

'''
Number of Operations for O(n*log(n)):

Doubling the size of the input (i.e., doubling n) for an O(n*log(n)) algorithm does not simply double the number of operations. The log(n) part means it grows a bit slower because log(n) increases slowly as n gets larger.

For example:

If n is 1000, log(1000) ≈ 10, so O(n*log(n)) would be about 1000 * 10 = 10,000 operations.
If n doubles to 2000, log(2000) ≈ 11, so O(n*log(n)) would be about 2000 * 11 = 22,000 operations.
So, it's not a simple doubling; the growth is more balanced and efficient due to the logarithmic factor.

Splitting into Smaller Problems:

You're right that splitting the problem into smaller chunks helps handle each chunk faster, and this is the essence of Divide and Conquer algorithms like Merge Sort.

Comparison with O(n^2):

For an O(n^2) algorithm:

If n is 1000, you'd have about 1000^2 = 1,000,000 operations.
If n doubles to 2000, you get 2000^2 = 4,000,000 operations.
This shows a much faster growth in the number of operations compared to O(n*log(n)). That's why O(n*log(n)) is significantly more efficient for large input sizes.
'''

'''
WHY USE MERGE SORT?
Fast: Merge sort is much faster than bubble sort, being O(n*log(n)) instead of O(n^2).

Stable: Merge sort is also a stable sort which means that values with duplicate keys in the original list will be in the same order in the sorted list.

Extra memory: Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires an extra array in memory to merge the sorted subarrays.

Recursive: Merge sort requires many recursive function calls, and function calls can have significant resource overhead.
'''

'''
PSEUDOCODE
For each index in the input list:
Set a j variable to the current index
While j is greater than 0 and the element at index j-1 is greater than the element at index j:
Swap the elements at indices j and j-1
Decrement j by 1
Return the list

TIP
In some languages you need to use a temp variable to swap values, but in python you can do that in a single line:
'''

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums

'''
WHY USE INSERTION SORT?
Simple implementation, easy to write
Fast for very small data sets
Faster than other simple sorting algorithms like Bubble Sort
Adaptive: Faster for partially sorted data sets
Stable: Does not change the relative order of elements with equal keys
In-Place: Only requires a constant amount of memory
Online: Can sort a list as it receives it
'''

'''
WHY IS INSERTION SORT FAST FOR SMALL LISTS?
Some production sorting implementations use insertion sort for very small inputs under a certain threshold (very small, like 10-ish). Insertion sort is better for very small lists than some of the faster algorithms because:

There is no recursion overhead
Tiny memory footprint
It's a stable sort as described above
'''

# QUICK SORT 

'''
Quick sort is an efficient sorting algorithm that's widely used in production sorting implementations. Like merge sort, quick sort is a divide and conquer algorithm.

DIVIDE
Select a pivot element that will preferably end up close to the center of the sorted pack
Move everything onto the "greater than" or "less than" side of the pivot
The pivot is now in its final position
Recursively repeat the operation on both sides of the pivot
CONQUER
The array is sorted after all elements have been through the pivot operation
VISUALS
The quick_sort algorithm is recursive. And it works in the following way:

Select a "pivot" element - We'll arbitrarily choose the last element in the list
Move through all the elements in the list and swap them around until all the numbers less than the pivot are on the left, and the numbers greater than the pivot are on the right
Move the pivot between the two sections where it belongs
recursively repeat for both sections
'''


def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)  # partition and get pivot index
        quick_sort(nums, low, p - 1)  # recursively sort left
        quick_sort(nums, p + 1, high)  # recursively sort right



def partition(nums, low, high):
    pivot = nums[high]  # Step 1: Choose the pivot element
    i = low  # Step 2: Set the initial index
    
    # Step 3: Traverse and compare
    for j in range(low, high):  # j will run from low to high-1
        if nums[j] < pivot:  # Compare current element with pivot
            nums[i], nums[j] = nums[j], nums[i]  # Swap elements
            i += 1  # Increment i
    
    # Step 4: Final swap to place pivot in its correct position
    nums[i], nums[high] = nums[high], nums[i]
    return i  # Step 5: Return the index of the pivot

'''
QUICK SORT BIG O
On average, quicksort has a Big O of O(n*log(n)). In the worst case, and assuming we don't take any steps to protect ourselves, it can break down to O(n^2).

partition() has a single for-loop that ranges from the lowest index to the highest index in the array. By itself, the partition() function is O(n). The overall complexity of quicksort is dependent on how many times partition() is called.

In the worst case, the input is already sorted. An already sorted array results in the pivot being the largest or smallest element in the partition each time. When this is the case, partition() is called a total of n times.

In the best case, the pivot is the middle element of each sublist which results in log(n) calls to partition().
'''

'''
FIXING QUICK SORT BIG O
As we discussed, while the version of quicksort that we implemented is almost always able to perform at speeds of O(n*log(n)), its Big O is still technically O(n^2). We can fix this by altering the algorithm slightly.

There are two approaches:

Shuffle input randomly before sorting. This can trivially be done in O(n) time
Actively find the median of a sample of data from the partition, this can be done in O(1) time.
RANDOM APPROACH
The random approach is easy to code, works practically all of the time, and as such is often used.

The idea is to quickly shuffle the list before sorting it. The likelihood of shuffling into a sorted list is astronomically unlikely, and is also more unlikely the larger the input.

MEDIAN APPROACH
One of the most popular solutions is to use the "median of three" approach. Three elements (for example: the first, middle, and last elements) of each partition are chosen and the median is found between them. That item is then used as the pivot.

This approach has the advantage that it can't break down to O(n^2) time because we are guaranteed to never use the worst item in the partition as the pivot. That said, it can still be slower because a true median isn't used.
'''

# PROS AND CONS OF QUICK SORT

# Pros:

# Very fast in the average case
# In-Place: Saves on memory, doesn't need to do a lot of copying and allocating
# Cons:

# More complex implementation
# Typically unstable: changes the relative order of elements with equal keys

# SELECTION SORT
'''Another sorting algorithm we never covered in-depth is called "selection sort". It's similar to bubble sort in that it works by repeatedly swapping items in a list. However, it's slightly more efficient than bubble sort because it only makes one swap per iteration.

Selection sort pseudocode:

For each index:
Set smallest_idx to the current index
For each index from smallest_idx+1 to the end of the list:
If the number at the inner index is smaller than the number at smallest_idx, set smallest_idx to the inner index
Swap the number at the current index with the number at smallest_idx
'''

def selection_sort(nums):
    for j in range(len(nums)): # Outer loop iterates through each index of the list
        smallest_index = j # Set smallest index to the current index j
        for k in range(j + 1, len(nums)): # Inner loop iterates through j + 1 to end of list
            if nums[k] < nums[smallest_index]: # Compares each value in the inner loop to the current smallest value
                smallest_index = k
        nums[j], nums[smallest_index] = nums[smallest_index], nums[j] # Swaps the smallest found value with the value at index j
    return nums



# POLYNOMIAL VS EXPONENTIAL

# POLYNOMIAL TIME:
# O(1)
# O(n)
# O(n*log(n))
# O(n^2)
# O(n^3)
# O(n^4)
# .....

# EXPONENTIAL TIME

# O(2^n)
# O(3^n)
# ...
# O(n^n)
# ON(n!)

'''
Algorithm's Runtime: This refers to how long it takes for an algorithm to finish its job, usually in terms of the size of the input (n).

Polynomial Time: When we say an algorithm runs in polynomial time, we're saying that the number of steps it takes to complete is no more than a polynomial function of the size of the input n.

n^k: The expression n^k represents a polynomial, where n is the size of the input and k is some constant. For example:

If k=1, we get n^1, which is just n.
If k=2, we get n^2.
If k=3, we get n^3, and so on.
Does Not Grow Faster: This means that as the size of the input (n) increases, the time the algorithm takes to run increases at a rate that can be represented by some polynomial (n^k). It won't be faster than this rate.

EXAMPLES:
n^1 (Linear Time): If an algorithm's runtime is proportional to the input size, it's O(n). This means if you double the input size, the time taken doubles.

n^2 (Quadratic Time): If the runtime is proportional to the square of the input size, it's O(n^2). This means if you double the input size, the time taken grows four times.

VISUAL UNDERSTANDING:
If you plot these functions:

Polynomial functions like n, n^2, n^3 grow, but at a manageable rate.
Exponential functions (e.g., 2^n) grow exceedingly fast, becoming impractical for even slightly large inputs.
Here is a simple comparison to visualize:

For n = 10:
n = 10
n^2 = 100
2^n = 1024
Notice how 2^n skyrockets compared to n and n^2.

POLYNOMIAL TIME = P
Back in the 1970s, some computer scientist researchers wanted to come up with a good, descriptive name for the set of polynomial time algorithms. After much deliberation, they settled on the letter P (naming things is hard).

In general, the main important takeaway is that:

Problems that fall into class P are practical to solve on computers.
Problems that don't fall into P are hard, slow, and impractical.
'''

# REDUCTION TO P

'''
Here are the implementation details to do it in polynomial time:

The input n represents the index of the desired Fibonacci value
Initialize three values. One will hold the current value, one will hold the parent value (1 before), and one will hold the grandparent value (2 before the current). You'll need to hard-code the first two values of the sequence. grandparent=0 and parent=1
Write a loop that iterates n-1 times. (For example, the loop should not repeat when n=2.)
Inside the loop update the current based on the parents, then update the parents to their appropriate values.
Return the current value once the loop completes
'''

def fib(n):
    # Handle the simplest cases directly
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    grandparent = 0  # This is F(0)
    parent = 1       # This is F(1)
    current = 1      # Starting value for the loop
    
    for i in range(2, n + 1):
        current = parent + grandparent  # This is F(i) = F(i-1) + F(i-2)
        grandparent = parent            # Move parent to grandparent
        parent = current                # Update parent to the new current value
    
    return current


# ORDER 2^N - EXPONENTIAL
# O(2^n) is the first Big O class that we've dealt with that falls into the scary exponential category of algorithms.

# Algorithms that grow at an exponential rate become impossible to compute after so few iterations that they are almost worthless in practicality.


def power_set(input_set):
    if len(input_set) == 0:
        return [[]]  # Base case: return list with an empty list

    # Recursive case
    first_element = input_set[0]
    remaining_elements = input_set[1:]

    # Get the power set of the remaining elements
    subsets_without_first = power_set(remaining_elements)

    power_set_list = []

    for subset in subsets_without_first:
        # Subset without the first element
        power_set_list.append(subset)
        # Subset with the first element
        power_set_list.append([first_element] + subset)

    return power_set_list

'''
OBSERVE!
Notice how the power_set() function gets exponentially slower with each iteration. This is because its complexity class is O(2^n)

If we could calculate one subset per millisecond, completing the power_set() of just 25 items would take approximately 9 hours, and that's not accounting for the massive amounts of memory we would need.

40 items would take over 34 years!
'''

import time

def power_set(input_set):

    if len(input_set) == 0:
        return [[]]

    power_set_list = []
    recursive = power_set(input_set[1:])

    for subset in recursive:
        power_set_list.append([input_set[0]] + subset)
        power_set_list.append(subset)
    return power_set_list

input_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

result = power_set(input_set)

print("Power set of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:")
for subset in result:
    print(subset)

print(f"\nTotal subets: {len(result)}")

# Sample input list with 20 items
input_set = list(range(1, 21))  # [1, 2, 3, ..., 20]

# Measure the start time
start_time = time.time()

# Running the power_set function
result = power_set(input_set)

# Measure the end time
end_time = time.time()

# Printing the output (optional, as it's very large)
# print("Power set of [1, 2, ..., 20]:")

# for subset in result:
#     print(subset)

print(f"\nTotal subsets: {len(result)}")
print(f"Time taken: {end_time - start_time} seconds")


### BIG O COMPLEXITY NOTES

# O(1) - constant - *Best* The algorithm always takes the same amount of time, regardless of how much data there is. Example: Looking up an item in a list by index

# O(log n) - logarithmic - *Great* Algorithms that remove a percentage of the total steps with each iteration. Very fast, even with large amounts of data. Example: Binary search

# O(n) - linear - *Good*  100 items, 100 units of work. 200 items, 200 units of work. This is usually the case for a single, non-nested loop. Example: unsorted array search.

# O(n log n) - "linearithmic" - Okay This is slightly worse than linear, but not too bad. Example: mergesort and other "fast" sorting algorithms.

# O(n^2) - quadratic - Slow The amount of work is the square of the input size. 10 inputs, 100 units of work. 100 Inputs, 10,000 units of work. Example: A nested for loop to find all the ordered pairs in a list.

# O(n^3) - cubic - Slower If you have 100 items, this does 100^3 = 1,000,000 units of work. Example: A doubly nested for loop to find all the ordered triples in a list.

# O(2^n) - exponential - Horrible We want to avoid this kind of algorithm at all costs. Adding one to the input doubles the amount of steps. Example: Brute-force guessing results of a sequence of n coin flips.

# O(n!) - Factorial - Even More Horrible The algorithm becomes so slow so fast, that is practically unusable. Example: Generating all the permutations of a list

# EXAMPLES

# O(1) - Constant Time
# The time or space taken by the function doesn't change relative to the input size.

def get_first_element(array):
    return array[0]

# O(log n) - Logarithmic Time
# The time grows logarithmically as the input size increases.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return None

# O(n) - Linear Time
# The time grows linearly with the size of the input.

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# O(n log n) - Linearithmic Time
# Commonly seen in efficient sorting algorithms.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# O(n^2) - Quadratic Time
# The time grows quadratically with the input size.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# O(2^n) - Exponential Time
# This time complexity grows exponentially with each additional element. Here's an example using a recursive function to generate all subsets of a set:

def find_subsets(s):
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(s)):
            backtrack(i + 1, path + [s[i]])

    result = []
    backtrack(0, [])
    return result

# Example of usage
set_elements = [1, 2, 3]
print(find_subsets(set_elements))

# O(n!) - Factorial Time
# This time complexity grows factorially with the input size. One common example is to generate all permutations of a list:

def generate_permutations(arr):
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]

    result = []
    backtrack(0)
    return result

# Example of usage
array = [1, 2, 3]
print(generate_permutations(array))

# O(n^3) - Cubic Time
# This time complexity grows cubically with the input size. An example could be three nested loops, like matrix multiplication:

def matrix_multiplication(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
                
    return result

# Example of usage
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print(matrix_multiplication(A, B))

# O(2n)

#   halvedSections returns a list of lists. For example,
#	    the input "12" would result in
#	    [
#		    [0 1 2 3 4 5 6 7 8 9 10 11 12]
#			[0 1 2 3 4 5 6]
#			[0 1 2 3]
#			[0 1]
#		]
def halved_sections(n):
    rows = []
    i = n
    while i > 0:
        col = []
        for j in range(i+1):
            col.append(j)
        rows.append(col)
        i //= 2
    return rows

# Which has a specific time complexity of:

# T(n) = O(n + n/2 + n/4 + … 1)

# Hint: This is a tricky one. You need to take into account the shrinking size of each successive list.




# EXPONENTIAL GROWTH SEQUENCE 

def exponential_growth(n, factor, days):
    growth_sequence = [n]

    for _ in range(days):
        growth = growth_sequence[-1] * factor
        growth_sequence.append(growth)
    return growth_sequence

'''
Suppose n = 10, factor = 2, and days = 4.
Your list starts with [10].
On the first loop iteration, growth_sequence[-1] is 10, and 10 * 2 = 20, so the list becomes [10, 20].
Next iteration, growth_sequence[-1] is 20, and 20 * 2 = 40, so the list becomes [10, 20, 40].
This continues until you've looped days times.
'''

# TRAVEL TIME LEFT

def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1


    while time_left >= time_in_country:
        time_left -= time_in_country  # Subtract time spent in the current country from time_left
        time_in_country *= factor     # Increase the time required for the next country
        count += 1                    # Increment the count of countries visited
    return count

# Non-Deterministic Polynomial Time
'''NP (which stands for nondeterministic polynomial time) is the set of problems whose solutions can be verified in polynomial time, but not necessarily solved in polynomial time.

For a more precise definition of NP, take a look here.

P is in NP
Because all problems that can be solved in polynomial time can also be verified in polynomial time, all the problems in P are also in NP

P in NP

The Oracle
A good way of thinking about problems in NP is to imagine that we have a magic oracle that gives us potential solutions to problems. Here would be our process for finding if a problem is in NP:

Present the problem to the magic oracle
The magic oracle gives us a potential solution
We verify in polynomial time that the solution is correct
If we can do the verification in polynomial time, the problem is in NP, otherwise, it isn't.'''

# TRAVELING SALESMAN PROBLEM

# Probelm solved in NP(Non polynomial time) (O(n!)) Factorial

def tsp(cities, paths, dist):
    posible_paths = permutations(cities)
    
    for path in posible_paths:
        total_distance = 0  # Initialize for each path
        
        for i in range(len(path) - 1):
            from_city = path[i]
            to_city = path[i + 1]
            total_distance += paths[from_city][to_city]  # Accumulate the distance
        
        # After summing the path distance, check if it's less than dist
        if total_distance < dist:
            return True
    
    # If no path found within the distance, return False
    return False

# Dont touch below this line

def permutations(arr):
    res = []  # Initialize the result list to store permutations
    res = helper(res, arr, len(arr))  # Call the helper function
    return res  # Return the final result


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()  # Make a copy of arr
        res.append(tmp)  # Append the copy to res
    else:
        for i in range(n):
            # Recursive call to generate permutations for n-1 elements
            res = helper(res, arr, n - 1)

            # Swap logic for generating permutations
            if n % 2 == 1:  # If n is odd
                arr[n - 1], arr[i] = arr[i], arr[n - 1]  # Swap the last element with the i-th element
            else:  # If n is even
                arr[0], arr[n - 1] = arr[n - 1], arr[0]  # Swap the first element with the last element
    return res

# Probem verified in P(Polynomial time) - O(n)

def verify_tsp(paths, dist, actual_path):

    verify_distance = 0
    # Calculate the distance for travelling through the path
    for i in range(len(actual_path) - 1):
        path_a = actual_path[i]
        path_b = actual_path[i + 1]
        verify_distance += paths[path_a][path_b]
    # Add the distance from the last city back to the starting city
    verify_distance += paths[actual_path[-1]][actual_path[0]]
    # Compare the computed distance to the provided distance
    if  verify_distance < dist:
        return True
    return False

# NP-Complete / reducer
'''Some, but not all problems in NP are also considered to be NP-complete.

A problem in NP is also NP-complete if every other problem in NP can be reduced into it in polynomial time.

How is a problem "reduced"?
We won't go in deep on the subject of reductions in this course, but we can cover the basics.

Any problem, let's call it Problem A, can be reduced to a different problem, Problem B, if there is an algorithm (called a reducer) that changes an algorithm that solves Problem B into an algorithm that solves Problem A.

Algorithm to solve B -> reducer -> Algorithm to solve A

We say that "Problem A is reducible to problem B" if the reducer from the above can be run in polynomial time.

What Does That Mean With NP-Complete?
If we have an algorithm that solves an NP-complete problem, it has been proven that we can quickly reduce that algorithm into a new algorithm to solve any other problem in NP.'''




# Password guesses given a pasaword length

def get_num_guesses(length):
    guesses = 0
    
    for i in range(1, length + 1):
        guesses += 26 ** i
    return guesses
        
'''Does P Equal NP?
SUSPECT P != NP
We don't know if P = NP.

We have been unable to prove that P = NP because we can't find any polynomial-time solutions to NP-complete problems. Additionally, we have been unable to prove that P != NP. We suspect P != NP just because it has been so difficult to prove that P = NP.

That said, it's actually more complicated to prove the negative case. To prove the positive case, that P = NP, we simply need to solve an NP-complete problem like TSP in polynomial time. 
In order to prove the negative case, that P != NP, we would need to exhaustively prove that there's no possible way to solve TSP in polynomial time. That's a lot trickier.'''


# NP-HARD

# All NP-complete problems are NP-hard, but not all NP-hard problems are NP-complete. The determining factor between NP-complete and NP-hard is that not all NP-hard problems are in NP.

# math.sqrt(x)
# Return the square root of x.
# PRoblem is NP

import math

def prime_factors(n):
    prime_factor_list = []
    
    # Handle factor of 2
    while n % 2 == 0:
        prime_factor_list.append(2)
        n = n // 2 # same thing as shorthand n //= 2
    
    # Handle odd factors up to square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factor_list.append(i)
            n = n // i # same thing as shorthand n //= i
    
    # If n is still a prime number and greater than 2, append it to the list
    if n > 2:
        prime_factor_list.append(n)
    
    return prime_factor_list

# n /= 2 performs floating-point division and assigns the resulting floating-point number back to n. This means if n was an integer, after this operation, n would become a float.

# n //= 2, on the other hand, performs integer (or floor) division and keeps n as an integer. This means it discards any decimal portion and keeps only the whole number part.





def find_subset_sum(nums, target, index):
    # Step 1: If target is 0, we've found a subset
    if target == 0:
        return True
    
    # Step 2: If index is below 0 and target is not 0, no subset found
    if index < 0 and target != 0:
        return False
    
    # Step 3: If current number is more than target, skip it
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    
    # Step 4: Try excluding and including the current number
    return find_subset_sum(nums, target, index - 1) or find_subset_sum(nums, target - nums[index], index - 1)



### DATA STRUCTURES ###


def count_potions(inventory):
    count = 0

    for item in inventory:
        if item == "Healing potion":
            count += 1
    return count


# WHAT IS A DATA STRUCTURE

'''More formally, a data structure is a data organization, management, and storage format that enables efficient access and modification. More precisely, a data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.'''

'''
In other words, a data structure:

Stores data
Organizes data in such a way that we can read and modify it quickly
Implements algorithmic functions that expose the ability to read and modify the data
Examples of data structures you are likely already familiar with:'''

# Array (AKA list or slice) - several elements stored in a specific order
myList = ['cat', 'dog', 'mouse']

# Record (AKA dictionary or map) - Unordered* elements stored by key/value pair
myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# LIST INDEXING

def last_item(inventory):
    if len(inventory) < 1: # If list is empty return none
        return None
    return inventory[-1] # return the last item in the list


# or 

def last_item(inventory):
    if len(inventory) > 0:
        return inventory[len(inventory) - 1]
    return None


## STACKS

# What is a stack?
'''A stack is an abstract data type that serves as a collection of elements. Our stack will have several operations:

stack.push(item) -> places a new item on top of the stack
stack.pop() -> removes the top item from the stack and returns it
stack.peek() -> returns the top item from the stack without modifying the stack
stack.size() -> returns the number of items in the stack'''


class Stack:
    def __init__(self):
        self.arrows = []

    def push(self, arrow): # adds item to the end of the list
        self.arrows.append(arrow)

    def pop(self): # removes the last item from the list
        if len(self.arrows) == 0:
            return None
        return self.arrows.pop()    

    def peek(self): # shows the last item in the list without modifying the list
        if len(self.arrows) == 0:
            return None
        return self.arrows[-1] # Or self.arrows[len(self.arrows) - 1]

    def size(self): # returns the length of the list
        return len(self.arrows)
    

###


def function_one():
	# function_one is pushed onto the callstack
	function_two()
	function_two()
	# function_one is popped off of the callstack

def function_two():
	# function_two is pushed onto the callstack
	function_three()
	function_three()
	# function_two is popped off of the callstack

def function_three():
	# function_three is pushed onto the callstack
	print("function three")
	# function_three is popped off of the callstack

function_one()
    
'''
For simplicity's sake, let's just focus on the runtime's call frames to understand why a stack is used. A call frame is just an area of memory that is set aside by the language to keep track of a function call in progress.
Call frames are born when a function is called, and they die when a function returns.

In other words:

Calling a function pushes a call frame onto the runtime stack
Returning from a function pops the top frame off the stack.'''

'''
Let's do a runtime stack simulation so we can better visualize how it works.

I've provided a call() function that takes a function as input and executes it with some additional logging. Instead of calling each function in the normal way you can use the call function. For example:

call(my_function)

instead of:

my_function()

The call function will push and pop the name of the function on and off of our own Stack implementation, and will print the state of the stack at each step.'''

def attack_action():
    call(shoot_arrow)
    call(calc_new_health)


def shoot_arrow():
    call(calc_damage)


def calc_damage():
    call(apply_damage)


# don't touch below this line


def calc_new_health():
    pass


def apply_damage():
    pass


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


stack = Stack()


def call(func):
    stack.push(func.__name__)
    print("Pushing " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=================================")
    func()
    stack.pop()
    print("Popping " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=================================")


call(attack_action)

###

'''
Balanced Parentheses

((()))
(())()
(())
()()
()
Copy icon
Unbalanced Parentheses

(()))
())
)
(
'''


def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == "(":
            stack.push(char)
        elif char == ")":  # Use `elif` here
            if stack.pop() is None:  # Check if the stack is empty when popping
                return False
    return stack.peek() is None  # Final check outside the loop
            


# don't modify below this line


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]
    


###

# Overiding parent class push method in child class 

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


# don't modify above this line


class PotionStack(Stack):
    def push(self, potion):
        if self.peek() != potion:
            return super().push(potion)
        

###

# QUEUE

'''A queue is an abstract data type that serves as an ordered collection of elements. A simple queue typically has several operations:'''

# queue.push(item) -> adds an item to the tail of the queue
# queue.pop() -> removes and returns an item from the head of the queue
# queue.peek() -> returns an item from the head of the queue
# queue.size() -> returns the number of items in the queue

'''
The order in which elements come off a queue gives rise to its alternative name, FIFO (first in, first out)

Think of a line to get tickets. The first person to get in line will be the first person to receive a ticket and get out of line.

-> [tail, item, item, item, head] ->'''

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(-1)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)



 # If we were dealing with a dictionary 

# Initializing the Dictionary Queue

# Dictionary-Based Initialization:

class DictQueue:
    def __init__(self):
        self.items = {}
        self.next_key = 0  # Track the next key to use for insertion

# Here, we use items as a dictionary and next_key to track the insertion order since dictionaries do not maintain an explicit order.

# Dictionary-Based Push:

def push(self, item):
    self.items[self.next_key] = item
    self.next_key += 1

# In the dictionary version, we add the item with an integer key (next_key) that increases with each push to maintain order.

# Dictionary-Based Pop:

def pop(self):
    if len(self.items) == 0:
        return None
    last_key = max(self.items.keys())  # The key with the highest number, representing the last inserted
    temp = self.items[last_key]
    del self.items[last_key]
    return temp

# In the dictionary version, we find the last key using max, retrieve the item, and then delete it.

# Dictionary-Based Peek:

def peek(self):
    if len(self.items) == 0:
        return None
    last_key = max(self.items.keys())
    return self.items[last_key]



# Linked Lists (LL)

# A linked list is a linear data structure where elements are not stored next to each other in memory. The elements in a linked list are linked using pointers.

# Linked lists can be contrasted with the native List (aka Array) in Python. Items in a normal list are stored next to each other in memory, and to get an item from a List we need to use the numbered index:

# item = myList[1]

# In a linked list, there are no indexes. We need to walk each node of the list because the only way to get the location of the second item in a linked list is to look at the pointer of the first item.

'''
head node -> node -> node -> node -> tail node

The direction of flow above might feel opposite to what you're used to with a Queue, but it's really the same. Above I'm using arrows to show which nodes are pointing to which other nodes. In a future lesson when we implement a Queue using a LinkedList, we'll add elements to the tail and remove elements from the head. When we use arrows to denote the flow of data through the queue, it will still be:

tail node -> node -> node -> node -> head node
'''
    

# EXAMPLE USAGE

# Create nodes
node1 = Node("Node 1")
node2 = Node("Node 2")
node3 = Node("Node 3")

# Link nodes
node1.next = node2
node2.next = node3

# Create a linked list and set its head
linked_list = LinkedList()
linked_list.head = node1

# Let's iterate over our linked list
for node in linked_list:
    print(node.val)

# Output should be:
# Node 1
# Node 2
# Node 3



# ADDED add_to_tail method to class LinkedList
# ADDED add_to_head method to class LinkedList


class LinkedList:

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        node.next = self.head
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val



# Changed LinkedList class to LLQueue class and removed add_to_head functionality because Queues don't allow inserting into the wrong end.

class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        else:
            current_head = self.head
            self.head = current_head.next
            if self.head is None:
                self.tail = None
            return current_head
        
    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
    

### Matchmaking queue

def matchmake(queue, player):
    if player[-1] == "join":
        queue.push(player[0])
    if player[-1] == "leave":
        queue.search_and_remove(player[0])
    if queue.size() >= 4:
        player1 = queue.pop()
        player2 = queue.pop()
        return f"{player1} matched {player2}!"
    if queue.size() < 4:
        return "No match found"

        

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"
    



### What is a tree

'''A tree is a widely used data structure that simulates a hierarchical tree structure, with a root value and subtrees of children with a parent node, represented as a set of linked nodes.'''

'''
A tree is a collection of nodes starting at a root or head node, similar to how our Linked List was a collection of nodes starting with a head (root). The big difference between a LL and a tree is that a tree's nodes can have multiple children instead of just one.

A generic tree structure has the following rules:

Each node has a value and a list of "children"
Children can only have a single "parent"
Duplicate values are allowed, multiple nodes can have the same value
Linked List
node -> node -> node
Copy icon
Tree
            > node
      > node
            > node
> node            
            > node
      > node
            > node
'''


### Binary trees 

# Trees aren't particularly useful data structures unless they're ordered in some way. One of the most common types of ordered tree is a Binary Search Tree or BST. 
# In addition to the properties we've already talked about, a BST has some additional constraints:


'''Binary search tree or BST'''

# Instead of a list of children, each node has at most 2 children, a right and a left child
# The left child's value must be less than its parent's value
# The right child's value must be greater than its parents
# No two nodes in the BST can have the same value

'''Some of the simpler algorithms in regard to a BST are the get_min and get_max methods. The get_min function should loop through all the left child nodes and return the value of the last one. The get_max function should do the same for the right children.'''


class BSTNode:


    def get_min(self):
        if self.left == None:
            min = self.val
        if self.left != None:
            min = self.left.get_min()
        return min
        

    def get_max(self):
        if self.right == None:
            max = self.val
        if self.right != None:
            max = self.right.get_max()
        return max 


    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    

    def insert(self, val):
        # If the current node is empty, assign the value here
        if self.val is None:
            self.val = val

        # If the current node's value matches the inserted value, do nothing (no duplicates)
        elif self.val == val:
            pass

         # If the inserted value is less than the current node's value
        elif val < self.val:

            # If there's no left child, create a new node there
            if self.left is None:
                self.left = BSTNode(val)

            # Otherwise, recursively attempt to insert on the left child
            else:
                 self.left.insert(val)

        # If the inserted value is greater than the current node's value
        else:

            # If there's no right child, create a new node there
            if self.right is None:
                self.right = BSTNode(val)

            # Otherwise, recursively attempt to insert on the right child
            else:
                self.right.insert(val)


    def delete(self, val):
        # If the node is empty, return None. This handles cases where you try to delete from an empty tree.
        if self.val == None:
            return None
        # If the value to be deleted is less than the current node's value, recursively delete it from the left subtree.
        if val < self.val:
            #  Check if the left child exists before making the recursive call.
            if self.left:
                self.left = self.left.delete(val)
            return self
        # Similarly, if the value is greater than the current node's value, recursively delete it from the right subtree.
        if val > self.val:
            # Check if the right child exists before making the recursive call.
            if self.right:
                self.right = self.right.delete(val)
            return self
        #  If the value matches the current node's value, we have found the node to be deleted.
        # Handle three scenarios:
        if val == self.val:
            # If there's no right child, just return the left child. 
            # This effectively deletes the current node and replaces it with the left subtree.
            if self.right is None:
                return self.left
            # Similarly, if there's no left child, return the right child.
            if self.left is None:
                return self.right
            # Handles node with two children
            if self.left and self.right:
                #  We're going to find the in-order successor, starting from the right child.
                right_child = self.right
                #Traverse to the leftmost child in the right subtree, which is the in-order successor.
                while right_child.left:
                    right_child = right_child.left
                # Replace the current node's value with the successor’s value.
                self.val = right_child.val
                #  Recursively delete the successor, which is now a duplicate, from the right subtree.
                self.right = self.right.delete(right_child.val)
                # Finally, return the current node to link back properly to its parent in the BST.
                return self
            
   # Implement the recursive preorder method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values we have visited so far.
    def preorder(self, visited):
        visited.append(self.val)

        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited
    
    # Implement the recursive postorder method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values we have visited so far.
    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited
    
    # Implement the recursive inorder method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values visited so far.
    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        if self.val is not None:
            visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited

    # Implement the exists method. It should take a value as input and return True if the value exists in the tree, and False if it doesn't.
    def exists(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left:
                return self.left.exists(val)
        if val > self.val:
            if self.right:
                return self.right.exists(val)
        return False
   

   