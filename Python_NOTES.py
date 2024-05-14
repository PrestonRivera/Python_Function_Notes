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

Input:
# ['Thrundar', 'Morgate', 'Gandolfo', 'Thraine', 'Norwad', 'Gilforn']

Expecting:
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


