import time

# O(2^n) 

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






