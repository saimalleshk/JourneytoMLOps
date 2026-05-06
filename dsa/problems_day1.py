# ============================================================
# PYTHON PRACTICE - PROBLEM SET DAY 1
# Your teacher has given you 3 problems to solve.
# Read the problem statement out loud first.
# Then plan your approach out loud before typing.
# Then code it out loud as you type.
# ============================================================


# ============================================================
# PROBLEM 1: STUDENT GRADE CALCULATOR
# Difficulty: Beginner
# Topics: Variables, if-elif-else, functions, f-strings
# ============================================================

# PROBLEM STATEMENT:
# Write a function called calculate_grade() that:
# - Takes a student's name and a list of marks as input
# - Calculates the average mark
# - Assigns a grade based on the average:
#       90 and above  -> "A"
#       80 to 89      -> "B"
#       70 to 79      -> "C"
#       60 to 69      -> "D"
#       Below 60      -> "F"
# - Returns a full report as a formatted string
#
# EXPECTED OUTPUT EXAMPLE:
# Student: Ravi
# Marks: [85, 90, 78, 92, 88]
# Average: 86.60
# Grade: B
# Result: Pass
#
# RULES:
# - If the student fails (grade F), the result should say "Fail"
# - Otherwise the result should say "Pass"
# - Average should be rounded to 2 decimal places
# - Do NOT use the built-in sum() or len() inside the average calculation
#   (practice writing it manually using a loop)
#
# ---- WRITE YOUR SOLUTION BELOW THIS LINE ----


def calculate_grade(name, marks):
    pass  # delete this line and write your solution here


# ---- TEST YOUR SOLUTION WITH THESE CALLS ----

# print(calculate_grade("Ravi", [85, 90, 78, 92, 88]))
# print(calculate_grade("Alice", [55, 48, 60, 52, 58]))
# print(calculate_grade("Bob", [95, 98, 100, 92, 97]))
# print(calculate_grade("Priya", [70, 75, 68, 72, 71]))


# ============================================================
# HINTS FOR PROBLEM 1 (read only if stuck for more than 20 mins)
# ============================================================

# HINT 1: To calculate average without sum() and len():
#   total = 0
#   count = 0
#   for mark in marks:
#       total = total + mark
#       count = count + 1
#   average = total / count

# HINT 2: To round to 2 decimal places use: round(average, 2)

# HINT 3: Build the grade string using if-elif-else:
#   if average >= 90:
#       grade = "A"
#   elif average >= 80:
#       grade = "B"
#   ... and so on

# HINT 4: To check for Pass or Fail:
#   result = "Fail" if grade == "F" else "Pass"

# HINT 5: To build the report string use f-strings:
#   report = f"Student: {name}\nMarks: {marks}\nAverage: {average}\nGrade: {grade}\nResult: {result}"
#   return report


# ============================================================
# WHAT YOU SHOULD SAY OUT LOUD WHILE SOLVING THIS:
# ============================================================
# "I am defining a function called calculate_grade that takes name and marks"
# "I need to loop through the marks to find the total"
# "I divide the total by the count to get the average"
# "I compare average to ranges using if-elif-else to assign a grade"
# "I use an f-string to format the final report"
# "I return the report string from the function"
# "I call the function with test data to verify it works"


# ============================================================
# PROBLEM 2: WORD FREQUENCY COUNTER
# Difficulty: Intermediate
# Topics: Strings, dictionaries, loops, sorting, functions
# ============================================================

# PROBLEM STATEMENT:
# Write a function called word_frequency() that:
# - Takes a paragraph (string) as input
# - Counts how many times each word appears
# - Ignores case (so "Python" and "python" are the same word)
# - Ignores punctuation: . , ! ? ; : ' "
# - Returns the top N most frequent words as a list of tuples
#   where each tuple is (word, count)
# - N should be a parameter with a default value of 5
#
# EXPECTED OUTPUT EXAMPLE:
# Input: "Python is great. Python is easy. Python is fun!"
# Output: [('python', 3), ('is', 3), ('great', 1), ('easy', 1), ('fun', 1)]
#
# RULES:
# - Do NOT use Counter from the collections module
#   (build the dictionary manually to practice)
# - Sort the result by count in DESCENDING order
#   (most frequent word comes first)
# - If two words have the same count, sort them alphabetically
#
# ---- WRITE YOUR SOLUTION BELOW THIS LINE ----


def word_frequency(paragraph, n=5):
    pass  # delete this line and write your solution here


# ---- TEST YOUR SOLUTION WITH THESE CALLS ----

# text = """
# Python is a great programming language.
# Python is easy to learn. Python is used everywhere.
# I love Python. Python is my favourite language.
# """
# print(word_frequency(text))
# print(word_frequency(text, n=3))
# print(word_frequency("hello world hello Python world hello", n=2))


# ============================================================
# HINTS FOR PROBLEM 2 (read only if stuck for more than 20 mins)
# ============================================================

# HINT 1: Convert the paragraph to lowercase first:
#   paragraph = paragraph.lower()

# HINT 2: Remove punctuation by looping through a list of characters:
#   for char in [".", ",", "!", "?", ";", ":", "'", '"']:
#       paragraph = paragraph.replace(char, "")

# HINT 3: Split the paragraph into individual words:
#   words = paragraph.split()

# HINT 4: Build a frequency dictionary manually:
#   freq = {}
#   for word in words:
#       if word in freq:
#           freq[word] += 1
#       else:
#           freq[word] = 1

# HINT 5: Convert the dictionary to a list of tuples:
#   items = list(freq.items())
#   This gives you: [("python", 3), ("is", 2), ...]

# HINT 6: Sort by count descending, then by word alphabetically:
#   sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))

# HINT 7: Return only the first N items:
#   return sorted_items[:n]


# ============================================================
# WHAT YOU SHOULD SAY OUT LOUD WHILE SOLVING THIS:
# ============================================================
# "I am converting the paragraph to lowercase to ignore case"
# "I am removing punctuation by replacing each punctuation character with empty string"
# "I am splitting the cleaned paragraph into a list of words"
# "I am looping through each word and updating a frequency dictionary"
# "I am converting the dictionary to a list of tuples using .items()"
# "I am sorting the list by count descending, and alphabetically for ties"
# "I am returning only the top N items using slicing"


# ============================================================
# PROBLEM 3: BANK ACCOUNT SYSTEM
# Difficulty: Intermediate to Advanced
# Topics: Classes, OOP, methods, error handling, __str__
# ============================================================

# PROBLEM STATEMENT:
# Build a BankAccount class that simulates a simple bank account.
#
# The class should have:
#
# ATTRIBUTES:
# - owner       : name of the account holder (string)
# - balance     : current balance (float), starts at 0 by default
# - transactions: a list that stores the history of all transactions
#
# METHODS:
# - deposit(amount)
#       Add money to the account.
#       Amount must be greater than 0.
#       If not, raise a ValueError with message: "Deposit amount must be positive"
#       Append a string like "+500 | Balance: 1500" to transactions
#
# - withdraw(amount)
#       Remove money from the account.
#       Amount must be greater than 0.
#       If not, raise a ValueError with message: "Withdrawal amount must be positive"
#       If amount is more than balance, raise a ValueError: "Insufficient funds"
#       Append a string like "-200 | Balance: 1300" to transactions
#
# - get_balance()
#       Return the current balance as a string like "Current balance: Rs.1300.00"
#
# - print_statement()
#       Print all transactions line by line with numbering
#       Example:
#           Transaction History for Ravi:
#           1. +1000 | Balance: 1000
#           2. -200 | Balance: 800
#           3. +500 | Balance: 1300
#
# - __str__()
#       Return: "BankAccount(owner=Ravi, balance=Rs.1300.00)"
#
# ---- WRITE YOUR SOLUTION BELOW THIS LINE ----


class BankAccount:
    pass  # delete this line and write your solution here


# ---- TEST YOUR SOLUTION WITH THESE CALLS ----

# account = BankAccount("Ravi", 1000)
# print(account)
# account.deposit(500)
# account.withdraw(200)
# account.deposit(300)
# print(account.get_balance())
# account.print_statement()
#
# Test error handling:
# try:
#     account.withdraw(10000)
# except ValueError as e:
#     print(f"Error: {e}")
#
# try:
#     account.deposit(-100)
# except ValueError as e:
#     print(f"Error: {e}")


# ============================================================
# HINTS FOR PROBLEM 3 (read only if stuck for more than 20 mins)
# ============================================================

# HINT 1: Define __init__ with parameters owner, balance=0:
#   def __init__(self, owner, balance=0):
#       self.owner = owner
#       self.balance = balance
#       self.transactions = []

# HINT 2: Inside deposit(), validate first, then add:
#   def deposit(self, amount):
#       if amount <= 0:
#           raise ValueError("Deposit amount must be positive")
#       self.balance += amount
#       self.transactions.append(f"+{amount} | Balance: {self.balance}")

# HINT 3: Inside withdraw(), check two conditions:
#   if amount <= 0:
#       raise ValueError("Withdrawal amount must be positive")
#   if amount > self.balance:
#       raise ValueError("Insufficient funds")
#   self.balance -= amount
#   self.transactions.append(f"-{amount} | Balance: {self.balance}")

# HINT 4: get_balance() just returns a formatted string:
#   return f"Current balance: Rs.{self.balance:.2f}"

# HINT 5: print_statement() loops through self.transactions with enumerate:
#   print(f"Transaction History for {self.owner}:")
#   for i, t in enumerate(self.transactions, start=1):
#       print(f"{i}. {t}")

# HINT 6: __str__ is a special method Python calls when you print the object:
#   def __str__(self):
#       return f"BankAccount(owner={self.owner}, balance=Rs.{self.balance:.2f})"


# ============================================================
# WHAT YOU SHOULD SAY OUT LOUD WHILE SOLVING THIS:
# ============================================================
# "I am defining a class called BankAccount"
# "The __init__ method initializes owner, balance, and an empty transactions list"
# "self refers to the current instance of the class"
# "The deposit method first validates the amount is positive"
# "If validation fails I raise a ValueError with a clear message"
# "After depositing I record the transaction in the transactions list"
# "The withdraw method checks two things - amount is positive and balance is enough"
# "The __str__ method defines what the object looks like when printed"
# "I use f-strings with :.2f to format the balance to two decimal places"


# ============================================================
# AFTER YOU FINISH ALL 3 - BONUS CHALLENGES
# ============================================================

# BONUS 1 (Problem 1 extension):
# Modify calculate_grade() to also accept a dictionary like:
# {"Maths": 85, "Science": 90, "English": 78}
# and print each subject name with its mark alongside the report

# BONUS 2 (Problem 2 extension):
# Modify word_frequency() to also EXCLUDE common words called stopwords:
# stopwords = ["is", "a", "the", "and", "to", "in", "of", "it", "i"]
# These words should not appear in the final result

# BONUS 3 (Problem 3 extension):
# Add a transfer(amount, other_account) method to BankAccount
# that withdraws from self and deposits into other_account
# and records the transfer in both accounts' transaction history


# ============================================================
# TODAY'S SUBMISSION CHECKLIST - Go through this before stopping
# ============================================================
# [ ] Did I read the problem statement out loud fully?
# [ ] Did I say my plan out loud before writing any code?
# [ ] Did I say what each line does as I typed it?
# [ ] Did I test with the provided test cases?
# [ ] Did I try the bonus challenges?
# [ ] Did my solution handle edge cases (negative input, empty list, etc.)?
# ============================================================
