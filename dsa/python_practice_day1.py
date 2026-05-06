# ============================================================
# PYTHON PRACTICE FILE - DAY 1
# Goal: Read the comment, say it out loud, then type the code
# Practice speaking + typing + understanding at the same time
# ============================================================


# ============================================================
# SECTION 1: BUILT-IN DATA TYPES
# ============================================================

# int() converts a value into an integer (whole number)
int(5)

# int() can also convert a string of digits into an integer
int("42")

# int() can convert a float to integer by removing the decimal part
int(3.9)

# float() converts a value into a floating point number (decimal number)
float(5)

# float() converts a string into a float
float("3.14")

# str() converts a value into a string (text)
str(100)

# str() converts a float into a string
str(3.14)

# bool() converts a value into a boolean (True or False)
bool(1)

# bool() of zero is False
bool(0)

# bool() of a non-empty string is True
bool("hello")

# bool() of an empty string is False
bool("")

# list() creates an empty list
list()

# list() converts a string into a list of characters
list("hello")

# tuple() creates an empty tuple
tuple()

# tuple() converts a list into a tuple
tuple([1, 2, 3])

# dict() creates an empty dictionary
dict()

# set() creates an empty set
set()

# set() removes duplicate values from a list
set([1, 2, 2, 3, 3, 3])

# type() tells us the data type of any value
type(5)

# type() on a string
type("hello")

# type() on a float
type(3.14)

# type() on a list
type([1, 2, 3])

# type() on a dictionary
type({"key": "value"})


# ============================================================
# SECTION 2: VARIABLES AND ASSIGNMENT
# ============================================================

# We assign an integer value to a variable called age
age = 25

# We assign a string value to a variable called name
name = "Ravi"

# We assign a float value to a variable called height
height = 5.9

# We assign a boolean value to a variable called is_student
is_student = True

# We assign a None value - meaning no value / empty
result = None

# We can assign multiple variables in one line using multiple assignment
x, y, z = 1, 2, 3

# We can assign the same value to multiple variables at once
a = b = c = 0

# We can swap two variables in one line - this is very Pythonic
x, y = y, x

# We print the value of the variable age using print()
print(age)

# We print the variable name
print(name)

# We print multiple variables separated by a comma
print(name, age)

# We use an f-string to embed variables inside a string for clean output
print(f"My name is {name} and I am {age} years old")

# We check the type of the variable age
print(type(age))

# We check the type of the variable name
print(type(name))


# ============================================================
# SECTION 3: ARITHMETIC OPERATORS
# ============================================================

# Addition operator adds two numbers together
print(10 + 5)

# Subtraction operator subtracts the second number from the first
print(10 - 5)

# Multiplication operator multiplies two numbers
print(10 * 5)

# Division operator divides and always returns a float
print(10 / 3)

# Floor division operator divides and returns only the whole number part
print(10 // 3)

# Modulus operator returns the remainder after division
print(10 % 3)

# Exponentiation operator raises a number to a power
print(2 ** 10)

# We store arithmetic results in variables
sum_result = 10 + 5
diff_result = 10 - 5
product_result = 10 * 5

# We print the results stored in variables
print(sum_result)
print(diff_result)
print(product_result)

# We use augmented assignment to add to an existing variable
count = 0
count += 1
print(count)

# We use augmented assignment to subtract from an existing variable
count -= 1
print(count)

# We use augmented assignment to multiply a variable
count = 5
count *= 2
print(count)

# We use augmented assignment to divide a variable
count /= 2
print(count)


# ============================================================
# SECTION 4: COMPARISON OPERATORS
# ============================================================

# Equal to operator checks if two values are the same
print(5 == 5)

# Equal to returns False when values are different
print(5 == 6)

# Not equal to operator checks if two values are different
print(5 != 6)

# Greater than operator checks if the left side is bigger
print(10 > 5)

# Less than operator checks if the left side is smaller
print(3 < 7)

# Greater than or equal to operator
print(5 >= 5)

# Less than or equal to operator
print(4 <= 5)

# We store comparison results in variables - they return True or False
is_equal = (10 == 10)
is_greater = (10 > 5)
print(is_equal)
print(is_greater)


# ============================================================
# SECTION 5: LOGICAL OPERATORS
# ============================================================

# and operator returns True only if BOTH conditions are True
print(True and True)

# and operator returns False if any one condition is False
print(True and False)

# or operator returns True if at least ONE condition is True
print(True or False)

# or operator returns False only if BOTH conditions are False
print(False or False)

# not operator reverses the boolean value
print(not True)

# not operator on False gives True
print(not False)

# We combine comparison and logical operators together
age = 20
is_adult = age >= 18
has_id = True
can_enter = is_adult and has_id
print(can_enter)

# We check if age is between 18 and 60 using chained comparison - very Pythonic
print(18 <= age <= 60)


# ============================================================
# SECTION 6: STRINGS IN DEPTH
# ============================================================

# We create a string variable
greeting = "Hello, World!"

# len() gives us the total number of characters in the string
print(len(greeting))

# We access a single character using its index - index starts at 0
print(greeting[0])

# We access the last character using negative index -1
print(greeting[-1])

# We slice a string to get a portion of it - start index is inclusive, end is exclusive
print(greeting[0:5])

# We slice from beginning to index 5
print(greeting[:5])

# We slice from index 7 to the end
print(greeting[7:])

# upper() method converts the entire string to uppercase
print(greeting.upper())

# lower() method converts the entire string to lowercase
print(greeting.lower())

# strip() method removes leading and trailing whitespace
messy = "   hello   "
print(messy.strip())

# replace() method replaces one substring with another
print(greeting.replace("World", "Python"))

# split() method splits a string into a list using a separator
sentence = "I love Python programming"
words = sentence.split(" ")
print(words)

# join() method joins a list of strings into one string with a separator
joined = "-".join(words)
print(joined)

# in keyword checks if a substring exists inside a string
print("Python" in sentence)

# startswith() checks if string begins with a given prefix
print(greeting.startswith("Hello"))

# endswith() checks if string ends with a given suffix
print(greeting.endswith("!"))

# count() counts how many times a substring appears
print("banana".count("a"))

# find() returns the index of the first occurrence of a substring
print(greeting.find("World"))

# find() returns -1 if the substring is not found
print(greeting.find("xyz"))

# We format strings using f-strings - the modern and preferred way
city = "Hyderabad"
population = 10000000
print(f"{city} has a population of {population}")

# String repetition using the * operator
print("ha" * 3)

# String concatenation using the + operator
first = "Hello"
second = " World"
combined = first + second
print(combined)

# We check if a string is all digits using isdigit()
print("1234".isdigit())

# We check if a string is all alphabets using isalpha()
print("hello".isalpha())

# We check if a string is all lowercase using islower()
print("hello".islower())

# We check if a string is all uppercase using isupper()
print("HELLO".isupper())


# ============================================================
# SECTION 7: LISTS
# ============================================================

# We create a list with square brackets - lists are ordered and mutable
fruits = ["apple", "banana", "cherry"]

# We print the entire list
print(fruits)

# We access the first element using index 0
print(fruits[0])

# We access the last element using index -1
print(fruits[-1])

# len() gives us the number of elements in the list
print(len(fruits))

# append() adds a single element to the END of the list
fruits.append("mango")
print(fruits)

# insert() adds an element at a specific index position
fruits.insert(1, "grape")
print(fruits)

# remove() removes the first occurrence of a specific value
fruits.remove("banana")
print(fruits)

# pop() removes and returns the element at a given index - default is last element
removed = fruits.pop()
print(removed)
print(fruits)

# pop() with an index removes element at that position
fruits.pop(0)
print(fruits)

# We can slice a list just like a string
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

# We can reverse a list using reverse() method - it modifies in place
numbers.reverse()
print(numbers)

# We can sort a list using sort() method - modifies in place
numbers.sort()
print(numbers)

# sorted() returns a new sorted list without modifying the original
original = [3, 1, 4, 1, 5, 9]
new_sorted = sorted(original)
print(new_sorted)
print(original)

# We check if an element exists in a list using the in keyword
print("apple" in fruits)

# index() returns the index of the first occurrence of a value
colors = ["red", "green", "blue"]
print(colors.index("green"))

# count() counts how many times a value appears in the list
nums = [1, 2, 2, 3, 3, 3]
print(nums.count(3))

# extend() adds all elements of another list to the end
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# We concatenate two lists using the + operator
combined_list = [1, 2, 3] + [4, 5, 6]
print(combined_list)

# We repeat a list using the * operator
repeated = [0] * 5
print(repeated)

# clear() removes all elements from the list
temp = [1, 2, 3]
temp.clear()
print(temp)

# We create a list of numbers using range() and list()
number_list = list(range(1, 11))
print(number_list)

# We create a list of even numbers using range() with a step of 2
evens = list(range(0, 20, 2))
print(evens)

# min() returns the smallest value in the list
print(min(number_list))

# max() returns the largest value in the list
print(max(number_list))

# sum() returns the total of all values in the list
print(sum(number_list))


# ============================================================
# SECTION 8: TUPLES
# ============================================================

# We create a tuple with parentheses - tuples are ordered but IMMUTABLE
coordinates = (10, 20)

# We print the tuple
print(coordinates)

# We access elements by index just like a list
print(coordinates[0])
print(coordinates[1])

# len() works on tuples too
print(len(coordinates))

# We unpack a tuple into separate variables
x, y = coordinates
print(x)
print(y)

# Tuples can hold mixed data types
person = ("Ravi", 25, "Hyderabad")
name, age, city = person
print(name)
print(age)
print(city)

# We check if an element exists in a tuple using in
print(25 in person)

# count() works on tuples
t = (1, 2, 2, 3)
print(t.count(2))

# index() works on tuples
print(t.index(3))

# A single element tuple needs a trailing comma to be recognized as a tuple
single = (42,)
print(type(single))

# Without the comma it is just an integer in parentheses
not_a_tuple = (42)
print(type(not_a_tuple))

# We convert a tuple to a list when we need to modify it
coords_list = list(coordinates)
coords_list.append(30)
print(coords_list)

# We convert it back to a tuple
coords_tuple = tuple(coords_list)
print(coords_tuple)


# ============================================================
# SECTION 9: DICTIONARIES
# ============================================================

# We create a dictionary with curly braces - key value pairs
student = {
    "name": "Ravi",
    "age": 22,
    "city": "Hyderabad",
    "gpa": 8.5
}

# We print the entire dictionary
print(student)

# We access a value using its key inside square brackets
print(student["name"])

# We access another value using its key
print(student["age"])

# get() is safer - it returns None instead of an error if key doesn't exist
print(student.get("email"))

# get() allows us to provide a default value if key is not found
print(student.get("email", "Not provided"))

# We add a new key-value pair to the dictionary
student["email"] = "ravi@example.com"
print(student)

# We update an existing key's value
student["age"] = 23
print(student["age"])

# We delete a key-value pair using del
del student["gpa"]
print(student)

# pop() removes and returns the value for a given key
removed_city = student.pop("city")
print(removed_city)
print(student)

# keys() returns all the keys in the dictionary
print(student.keys())

# values() returns all the values in the dictionary
print(student.values())

# items() returns all key-value pairs as tuples
print(student.items())

# We check if a key exists in a dictionary using in
print("name" in student)

# len() returns the number of key-value pairs
print(len(student))

# update() merges another dictionary into this one
student.update({"phone": "9876543210", "course": "Python"})
print(student)

# We create a dictionary using dict() constructor
config = dict(host="localhost", port=8080, debug=True)
print(config)

# We iterate over dictionary keys
for key in student:
    print(key)

# We iterate over key-value pairs using items()
for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# SECTION 10: SETS
# ============================================================

# We create a set with curly braces - sets store UNIQUE values only
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)

# Duplicate values are automatically removed in a set
with_duplicates = {1, 2, 2, 3, 3, 3}
print(with_duplicates)

# add() adds a single element to the set
unique_numbers.add(6)
print(unique_numbers)

# remove() removes an element - raises error if not found
unique_numbers.remove(6)
print(unique_numbers)

# discard() removes an element - does NOT raise error if not found
unique_numbers.discard(99)
print(unique_numbers)

# We check membership using the in keyword
print(3 in unique_numbers)

# len() returns the number of elements in a set
print(len(unique_numbers))

# union() combines two sets - all elements from both
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))

# intersection() returns only elements that are in BOTH sets
print(set_a.intersection(set_b))

# difference() returns elements in set_a that are NOT in set_b
print(set_a.difference(set_b))

# We convert a list to a set to remove duplicates
duplicate_list = [1, 1, 2, 2, 3, 3]
clean_set = set(duplicate_list)
print(clean_set)

# We convert it back to a list
clean_list = list(clean_set)
print(clean_list)


# ============================================================
# SECTION 11: CONDITIONAL STATEMENTS
# ============================================================

# if statement runs a block of code only when the condition is True
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement runs one block if True, another if False
score = 45
if score >= 50:
    print("Pass")
else:
    print("Fail")

# if-elif-else checks multiple conditions in sequence
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

# Nested if statement - an if inside another if
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome Admin")
    else:
        print("Welcome User")
else:
    print("Please log in")

# Ternary operator - shorthand if-else in a single line
temperature = 35
weather = "Hot" if temperature > 30 else "Cool"
print(weather)

# We combine conditions using and, or, not
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# We check if a value is None
value = None
if value is None:
    print("No value found")

# We check if a list is empty - empty list is falsy in Python
items = []
if not items:
    print("The list is empty")

# We check if a string is not empty
text = "hello"
if text:
    print("String has content")


# ============================================================
# SECTION 12: FOR LOOPS
# ============================================================

# for loop iterates over each item in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for loop with range() - range(5) gives 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# for loop with range(start, stop) - goes from start to stop-1
for i in range(1, 6):
    print(i)

# for loop with range(start, stop, step) - step controls the increment
for i in range(0, 10, 2):
    print(i)

# for loop iterating over a string character by character
for char in "Python":
    print(char)

# for loop iterating over a dictionary's keys
student = {"name": "Ravi", "age": 22}
for key in student:
    print(key)

# for loop iterating over key-value pairs using items()
for key, value in student.items():
    print(f"{key} = {value}")

# for loop with enumerate() - gives index and value together
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# for loop with enumerate() starting index from 1
for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")

# We use break to stop a loop early
for i in range(10):
    if i == 5:
        break
    print(i)

# We use continue to skip an iteration and move to the next one
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# We use a for loop to calculate the sum of a list
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(total)

# for loop with zip() - iterates over two lists at the same time
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# for loop with else - the else block runs when the loop finishes without break
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

# Nested for loop - a loop inside a loop
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")


# ============================================================
# SECTION 13: WHILE LOOPS
# ============================================================

# while loop keeps running as long as the condition is True
count = 0
while count < 5:
    print(count)
    count += 1

# while loop for a countdown
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

# while loop with break - exit the loop when a condition is met
number = 0
while True:
    print(number)
    number += 1
    if number == 5:
        break

# while loop with continue - skip even numbers
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# while loop to find the first number divisible by both 3 and 7
num = 1
while True:
    if num % 3 == 0 and num % 7 == 0:
        print(f"Found: {num}")
        break
    num += 1

# while loop with else - runs when condition becomes False naturally
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("While loop finished")


# ============================================================
# SECTION 14: LIST COMPREHENSIONS
# ============================================================

# List comprehension creates a new list using a compact one-line syntax
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# List comprehension with a condition - filter only even numbers
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# List comprehension to convert strings to uppercase
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)

# List comprehension to get the length of each word
lengths = [len(fruit) for fruit in fruits]
print(lengths)

# List comprehension with an if-else inside
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(labels)

# Nested list comprehension to create a multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)

# Dictionary comprehension creates a dictionary in one line
square_dict = {x: x ** 2 for x in range(1, 6)}
print(square_dict)

# Set comprehension creates a set in one line
unique_lengths = {len(fruit) for fruit in fruits}
print(unique_lengths)


# ============================================================
# SECTION 15: FUNCTIONS
# ============================================================

# We define a function using the def keyword
def greet():
    print("Hello, World!")

# We call the function by its name followed by parentheses
greet()

# We define a function that takes a parameter
def greet_person(name):
    print(f"Hello, {name}!")

# We call the function by passing an argument
greet_person("Ravi")

# We define a function that takes two parameters
def add(a, b):
    return a + b

# The return statement sends a value back to the caller
result = add(5, 3)
print(result)

# We define a function with a default parameter value
def power(base, exponent=2):
    return base ** exponent

# Calling with both arguments
print(power(3, 3))

# Calling with only the first argument - exponent defaults to 2
print(power(4))

# We use keyword arguments to pass arguments by name
print(power(exponent=3, base=2))

# We define a function that returns multiple values as a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([5, 2, 8, 1, 9])
print(low, high)

# We use *args to accept any number of positional arguments
def total(*args):
    return sum(args)

print(total(1, 2, 3))
print(total(10, 20, 30, 40))

# We use **kwargs to accept any number of keyword arguments
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Ravi", age=22, city="Hyderabad")

# We define a function with both *args and **kwargs
def mixed(*args, **kwargs):
    print(args)
    print(kwargs)

mixed(1, 2, 3, name="Ravi", city="Hyderabad")

# We define a recursive function - a function that calls itself
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))

# We define a recursive function to calculate Fibonacci numbers
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# A lambda function is a small anonymous one-line function
square = lambda x: x ** 2
print(square(5))

# Lambda with two parameters
multiply = lambda x, y: x * y
print(multiply(3, 4))

# We use lambda with sorted() to sort by a specific key
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people)

# We use lambda with map() to apply a function to every element
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# We use lambda with filter() to keep elements that pass a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# A docstring describes what a function does - placed right after def line
def calculate_area(length, width):
    """
    This function calculates the area of a rectangle.
    It takes length and width as parameters.
    It returns the product of length and width.
    """
    return length * width

print(calculate_area(5, 3))

# We can read a function's docstring using __doc__
print(calculate_area.__doc__)


# ============================================================
# SECTION 16: SCOPE - LOCAL AND GLOBAL VARIABLES
# ============================================================

# A global variable is defined outside all functions
global_var = "I am global"

# A local variable is defined inside a function
def show_scope():
    local_var = "I am local"
    print(local_var)
    print(global_var)

show_scope()

# We use the global keyword to modify a global variable inside a function
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)

# Variables defined inside functions are not accessible outside
def create_local():
    inside_var = "only inside"
    print(inside_var)

create_local()


# ============================================================
# SECTION 17: ERROR HANDLING WITH TRY AND EXCEPT
# ============================================================

# try-except block handles errors gracefully without crashing the program
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# We handle different types of errors with multiple except blocks
try:
    number = int("hello")
except ValueError:
    print("Invalid value - cannot convert to integer")

# try-except-else - else block runs only if NO error occurred
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print(f"Result is: {result}")

# try-except-finally - finally block ALWAYS runs regardless of error
try:
    x = int("5")
    print(x)
except ValueError:
    print("Error occurred")
finally:
    print("This always runs - good for cleanup")

# We catch any exception using the generic Exception class
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except Exception as e:
    print(f"An error occurred: {e}")

# We raise our own custom exception using raise
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-5)
except ValueError as e:
    print(e)


# ============================================================
# SECTION 18: FILE HANDLING
# ============================================================

# We open a file for writing using open() with mode 'w'
# The 'w' mode creates the file if it doesn't exist, or overwrites it
with open("sample.txt", "w") as file:
    file.write("Hello, this is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# We open a file for reading using open() with mode 'r'
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# We read a file line by line using readlines()
with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# We open a file in append mode 'a' to add content without overwriting
with open("sample.txt", "a") as file:
    file.write("This is line 4 - appended\n")

# We verify the appended content
with open("sample.txt", "r") as file:
    print(file.read())

# The with statement automatically closes the file - no need to call file.close()

# We write multiple lines at once using writelines()
lines_to_write = ["Line A\n", "Line B\n", "Line C\n"]
with open("multiline.txt", "w") as file:
    file.writelines(lines_to_write)

with open("multiline.txt", "r") as file:
    print(file.read())


# ============================================================
# SECTION 19: CLASSES AND OBJECT ORIENTED PROGRAMMING
# ============================================================

# We define a class using the class keyword - a class is a blueprint
class Dog:
    # __init__ is the constructor - it runs automatically when we create an object
    def __init__(self, name, breed, age):
        # self refers to the current object - instance attributes
        self.name = name
        self.breed = breed
        self.age = age

    # A method is a function that belongs to the class
    def bark(self):
        print(f"{self.name} says: Woof!")

    # A method that uses the object's attributes
    def describe(self):
        print(f"{self.name} is a {self.breed}, aged {self.age} years")

# We create an object (instance) of the Dog class
dog1 = Dog("Tommy", "Labrador", 3)
dog2 = Dog("Buddy", "German Shepherd", 5)

# We call the methods on the objects
dog1.bark()
dog2.bark()
dog1.describe()
dog2.describe()

# We access attributes directly
print(dog1.name)
print(dog2.age)

# We modify attributes directly
dog1.age = 4
print(dog1.age)


# ============================================================
# SECTION 20: INHERITANCE
# ============================================================

# We define a parent class (base class)
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

    def describe(self):
        print(f"I am {self.name}")

# We define a child class that inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # super() calls the parent class's __init__
        super().__init__(name, "Meow")
        self.color = color

    # We override the describe method
    def describe(self):
        print(f"I am {self.name} and I am {self.color}")

# We define another child class
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Moo")

    def give_milk(self):
        print(f"{self.name} is giving milk")

# We create objects of child classes
cat = Cat("Whiskers", "orange")
cow = Cow("Bessie")

# Child class inherits the speak() method from Animal
cat.speak()
cow.speak()

# Cat uses its overridden describe() method
cat.describe()

# Cow uses the parent's describe() method
cow.describe()

# Cow has its own unique method
cow.give_milk()

# isinstance() checks if an object is an instance of a class
print(isinstance(cat, Cat))
print(isinstance(cat, Animal))
print(isinstance(cow, Cat))


# ============================================================
# SECTION 21: SPECIAL / DUNDER METHODS
# ============================================================

# __str__ defines how the object looks when printed
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    # __repr__ defines the developer-friendly representation
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    # __len__ allows us to use len() on our objects
    def __len__(self):
        return len(self.name)

    # __eq__ defines how two objects are compared with ==
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person("Ravi", 22)
p2 = Person("Ravi", 22)
p3 = Person("Alice", 25)

# __str__ is called by print()
print(p1)

# __len__ is called by len()
print(len(p1))

# __eq__ is called by ==
print(p1 == p2)
print(p1 == p3)


# ============================================================
# SECTION 22: MODULES AND IMPORTS
# ============================================================

# We import the math module to use mathematical functions
import math

# math.sqrt() calculates the square root
print(math.sqrt(16))

# math.pi gives us the value of pi
print(math.pi)

# math.ceil() rounds up to the nearest integer
print(math.ceil(4.2))

# math.floor() rounds down to the nearest integer
print(math.floor(4.8))

# math.pow() raises a number to a power - returns a float
print(math.pow(2, 10))

# math.factorial() calculates the factorial of a number
print(math.factorial(5))

# math.log() calculates the natural logarithm
print(math.log(math.e))

# We import only specific functions from a module using from-import
from math import sqrt, pi

print(sqrt(25))
print(pi)

# We import a module with an alias using as
import math as m
print(m.sqrt(9))

# We import the random module for generating random numbers
import random

# random.random() returns a random float between 0 and 1
print(random.random())

# random.randint() returns a random integer between two values (inclusive)
print(random.randint(1, 100))

# random.choice() picks a random element from a list
colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors))

# random.shuffle() shuffles a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# random.sample() picks multiple unique random elements from a list
sample = random.sample(colors, 2)
print(sample)

# We import the datetime module to work with dates and times
import datetime

# datetime.datetime.now() gives the current date and time
now = datetime.datetime.now()
print(now)

# We access individual parts of the datetime object
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)

# datetime.date.today() gives just today's date
today = datetime.date.today()
print(today)

# We import the os module to interact with the operating system
import os

# os.getcwd() returns the current working directory
print(os.getcwd())

# os.listdir() lists files and folders in a directory
print(os.listdir("."))

# We import the sys module for system-related operations
import sys

# sys.version gives the Python version being used
print(sys.version)


# ============================================================
# SECTION 23: ITERATORS AND GENERATORS
# ============================================================

# An iterator is an object we can loop through one item at a time
# iter() creates an iterator from a list
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# next() gets the next item from the iterator
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# A generator function uses yield instead of return
# yield pauses the function and saves its state
def count_up(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

# We use the generator in a for loop
for num in count_up(1, 5):
    print(num)

# Generators are memory efficient - they produce values one at a time
def squares_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

# We convert the generator to a list
print(list(squares_generator(5)))

# Generator expression - like list comprehension but with parentheses
gen_expr = (x ** 2 for x in range(1, 6))
print(next(gen_expr))
print(next(gen_expr))
print(list(gen_expr))


# ============================================================
# SECTION 24: DECORATORS
# ============================================================

# A decorator is a function that wraps another function to add behavior
# We define a simple decorator
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

# We apply the decorator using the @ symbol - this is called syntactic sugar
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# A decorator that works with functions that take arguments
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"Result: {result}")

# A decorator that measures execution time
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "Done"

slow_function()


# ============================================================
# SECTION 25: COMMON BUILT-IN FUNCTIONS RECAP
# ============================================================

# print() outputs values to the console
print("Hello")

# input() reads user input as a string - commented to avoid blocking
# name = input("Enter your name: ")

# len() returns the length of a sequence
print(len("Python"))
print(len([1, 2, 3, 4, 5]))

# range() generates a sequence of numbers
print(list(range(10)))

# type() returns the data type of an object
print(type(42))

# int(), float(), str(), bool() convert between data types
print(int("5"))
print(float("3.14"))
print(str(100))
print(bool(0))

# abs() returns the absolute value of a number
print(abs(-42))

# round() rounds a number to a given number of decimal places
print(round(3.14159, 2))

# max() returns the maximum value from a sequence or arguments
print(max(3, 7, 2, 9, 1))
print(max([5, 10, 3]))

# min() returns the minimum value from a sequence or arguments
print(min(3, 7, 2, 9, 1))
print(min([5, 10, 3]))

# sum() returns the sum of all elements in an iterable
print(sum([1, 2, 3, 4, 5]))

# sorted() returns a new sorted list from any iterable
print(sorted([3, 1, 4, 1, 5, 9]))

# reversed() returns a reversed iterator - we convert to list to see it
print(list(reversed([1, 2, 3, 4, 5])))

# enumerate() gives index and value together
for i, v in enumerate(["a", "b", "c"]):
    print(i, v)

# zip() pairs up elements from multiple iterables
for pair in zip([1, 2, 3], ["a", "b", "c"]):
    print(pair)

# map() applies a function to every item in an iterable
print(list(map(str, [1, 2, 3, 4, 5])))

# filter() keeps only items for which the function returns True
print(list(filter(lambda x: x > 3, [1, 2, 3, 4, 5])))

# any() returns True if at least one element is truthy
print(any([0, 0, 1, 0]))

# all() returns True only if all elements are truthy
print(all([1, 2, 3, 4]))
print(all([1, 0, 3, 4]))

# id() returns the unique memory address of an object
x = 42
print(id(x))

# hash() returns the hash value of an object - used in sets and dicts
print(hash("hello"))

# dir() returns a list of attributes and methods of an object
print(dir([]))

# help() shows documentation - commented to avoid long output
# help(str)

# isinstance() checks if an object is an instance of a class
print(isinstance(5, int))
print(isinstance("hello", str))
print(isinstance(3.14, (int, float)))

# issubclass() checks if a class is a subclass of another
print(issubclass(bool, int))


# ============================================================
# SECTION 26: STRING FORMATTING METHODS
# ============================================================

# Old style formatting using % operator
name = "Ravi"
age = 22
print("My name is %s and I am %d years old" % (name, age))

# format() method - flexible and powerful
print("My name is {} and I am {} years old".format(name, age))

# format() with positional arguments
print("First: {0}, Second: {1}, First again: {0}".format("A", "B"))

# format() with keyword arguments
print("Name: {n}, Age: {a}".format(n=name, a=age))

# f-strings - modern, fast, and readable - preferred in Python 3.6+
print(f"My name is {name} and I am {age} years old")

# f-string with expressions inside
print(f"5 + 3 = {5 + 3}")

# f-string with formatting - 2 decimal places
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")

# f-string for aligning text - right align in a field of width 10
print(f"{'hello':>10}")

# f-string for aligning text - left align in a field of width 10
print(f"{'hello':<10}|")

# f-string for centering text in a field of width 10
print(f"{'hello':^10}|")

# f-string with fill character
print(f"{'hello':*^20}")


# ============================================================
# SECTION 27: USEFUL PATTERNS FOR INTERVIEWS
# ============================================================

# Pattern 1: Counting occurrences in a list using a dictionary
def count_occurrences(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(count_occurrences(words))

# Pattern 2: Finding duplicates in a list
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))

# Pattern 3: Reversing a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

# Pattern 4: Checking if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))

# Pattern 5: Finding the maximum element without using max()
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

print(find_max([3, 7, 1, 9, 4]))

# Pattern 6: Two sum problem - find two numbers that add to a target
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))

# Pattern 7: FizzBuzz - classic interview question
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(20)

# Pattern 8: Binary search - efficient search in a sorted list
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
    return -1

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(sorted_list, 7))
print(binary_search(sorted_list, 6))

# Pattern 9: Bubble sort - simple sorting algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))

# Pattern 10: Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 50) if is_prime(n)]
print(primes)


# ============================================================
# END OF DAY 1 - GREAT WORK!
# Topics covered:
# 1. Built-in data types
# 2. Variables and assignment
# 3. Arithmetic operators
# 4. Comparison operators
# 5. Logical operators
# 6. Strings in depth
# 7. Lists
# 8. Tuples
# 9. Dictionaries
# 10. Sets
# 11. Conditional statements
# 12. For loops
# 13. While loops
# 14. List comprehensions
# 15. Functions
# 16. Scope
# 17. Error handling
# 18. File handling
# 19. Classes and OOP
# 20. Inheritance
# 21. Special methods
# 22. Modules and imports
# 23. Iterators and generators
# 24. Decorators
# 25. Built-in functions recap
# 26. String formatting
# 27. Interview patterns
# ============================================================
