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

# Using the modulo % operator and the .append() method. 

def get_odd_numbers(num):
    odd_numbers = []
    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers


# Slicing lists syntax example: my_list[ start : stop : step ]

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]
# The above reads as "give me a slice of the scores list from index 1, up to but not including 5, skipping every 2nd value. All of the sections are optional.

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
