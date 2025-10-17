# dugga part 1
# define variable
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

# list of numbers to which the absolute value is bigger than or equal to 10 can be added so they can be summed
abs_bigger_10 = []

# for loop to check absolute value of each number in the list
for i in numbers:
    if abs(i) >= 10:
        # append the number to the new list if abs is bigger than or equal to 10
        abs_bigger_10.append(i)
print(sum(abs_bigger_10))

# same for loop structure with an empty list to which the cubes of negative numbers will be added
negative = []

# only difference is the condition in the if statement and the operation performed on the number before appending it to the new list
for i in numbers:
    if i <= 0:
        negative.append(i ** 3)
print(negative)

# new empty list to keep track of absolute values already seen
duplicate = []
# for loop to check for duplicates based on absolute values
for i in numbers:
    if abs(i) in duplicate:
        # if a duplicate is found, print message and break the loop so we stop at the first duplicate
        print (f"Repeat found of value", i)
        break
    elif abs(i) not in duplicate:
        # if no duplicate is found, print message and append the absolute value to the list so we can keep track of the values that have already been seen
        print("No repeats found (yet)")
        duplicate.append(abs(i))
