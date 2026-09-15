# ==========================================================
#                PYTHON DICTIONARY (dict)
# ==========================================================

# A Dictionary is a built-in Python data type.
# It stores data in the form of KEY : VALUE pairs.
#
# Example:
#
# Name  -> Dhananjay
# Age   -> 19
# Skill -> Python
#
# Here,
# "Name", "Age", and "Skill" are KEYS.
# "Dhananjay", 19, and "Python" are VALUES.


# ==========================================================
# 1. Creating a Dictionary (Fast Way)
# ==========================================================

student = {
    "Name": "Dhananjay",
    "Age": 19,
    "Skill": "Python"
}

print(student)

# Explanation:
#
# student is the dictionary variable.
#
# {
#     "Name": "Dhananjay",
#     "Age": 19,
#     "Skill": "Python"
# }
#
# Every item has two parts:
#
# KEY          VALUE
# -------------------------
# "Name"   ->  "Dhananjay"
# "Age"    ->  19
# "Skill"  ->  "Python"
#
# Keys must be unique.
# Values can be repeated.


# ==========================================================
# 2. Membership Operator (in)
# ==========================================================

print(9 in [1,2,3,4,5,6,7,8,9])

# Explanation:
#
# "in" checks whether an element exists.
#
# Python checks:
#
# Is 9 inside the list?
#
# [1,2,3,4,5,6,7,8,9]
#
# Since 9 is present,
# Output -> True


# ==========================================================
# 3. Another Dictionary Example
# ==========================================================

fruits = {
    "Red": "Apple",
    "Yellow": "Mango",
    "Green": "Watermelon"
}

print(fruits)

# Explanation:
#
# Dictionary:
#
# Red     -> Apple
# Yellow  -> Mango
# Green   -> Watermelon
#
# Here,
# Color is the KEY.
# Fruit name is the VALUE.


# ==========================================================
# 4. Creating an Empty Dictionary
# ==========================================================

z = {}

print(z)

# Explanation:
#
# {} creates an empty dictionary.
#
# Output:
# {}


# ==========================================================
# 5. Creating Dictionary using dict()
# ==========================================================

colors = dict(
    apple="red",
    banana="yellow",
    kiwi="brown"
)

print(colors)

# Explanation:
#
# dict() is another way to create a dictionary.
#
# It automatically creates:
#
# {
#   "apple":"red",
#   "banana":"yellow",
#   "kiwi":"brown"
# }


# ==========================================================
# 6. Creating Dictionary from List of Tuples
# ==========================================================

d = dict([
    ("apple", "red"),
    ("banana", "yellow"),
    ("kiwi", "brown")
])

print(d)

# Explanation:
#
# Every tuple contains:
#
# (Key, Value)
#
# Example:
#
# ("apple", "red")
#
# becomes
#
# apple -> red
#
# Python converts all tuples into one dictionary.


# ==========================================================
# 7. Hash Table Concept
# ==========================================================

student = {
    "name": "Dhananjay",
    "age": 19,
    "skill": "Python"
}

# Explanation:
#
# Python dictionaries use a Hash Table internally.
#
# Hash Table makes searching extremely fast.
#
# Instead of checking every key one by one,
# Python converts the key into a hash number
# and directly jumps to its memory location.


# ==========================================================
# 8. hash()
# ==========================================================

print(hash("name"))
print(hash("age"))
print(hash("skill"))

# Explanation:
#
# hash() converts a key into a unique integer.
#
# Example:
#
# hash("name")
#
# might produce
#
# 548739287342
#
# (Your output will be different.)
#
# Python uses this number internally
# to store and find data quickly.


# ==========================================================
# 9. Hash Index Calculation
# ==========================================================

index = hash("name") % 8
print(index)

# Explanation:
#
# Suppose:
#
# hash("name") = 245
#
# Then
#
# 245 % 8 = 5
#
# This means Python stores the key
# at index number 5.
#
# Why % 8 ?
#
# Suppose the hash table size is 8.
#
# Valid indexes are:
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
#
# Modulo (%) always returns a number
# between 0 and 7.


# ==========================================================
# 10. Nested Dictionary
# ==========================================================

info = {

    "Dhananjay": {
        "Degree": "BCA",
        "Skill": "Python"
    },

    "Swaraj": {
        "Degree": "BTech",
        "Skill": "Java"
    }
}

# Explanation:
#
# This is called a Nested Dictionary.
#
# One dictionary is stored inside another dictionary.
#
# Structure:
#
# info
#
# ├── Dhananjay
# │      ├── Degree -> BCA
# │      └── Skill -> Python
# │
# └── Swaraj
#        ├── Degree -> BTech
#        └── Skill -> Java


# ==========================================================
# 11. Accessing Nested Values
# ==========================================================

print(info["Swaraj"]["Skill"])

# Explanation:
#
# Python works step by step.
#
# Step 1:
# Find key "Swaraj"
#
# Step 2:
# Inside Swaraj dictionary,
# find key "Skill"
#
# Step 3:
# Return its value.
#
# Output:
# Java


# ==========================================================
# 12. Updating a Value
# ==========================================================

info["Swaraj"]["Skill"] = "Python"

print(info)

# Explanation:
#
# Old Value:
#
# Skill -> Java
#
# New Value:
#
# Skill -> Python
#
# Dictionaries are mutable,
# so values can be changed.


# ==========================================================
# 13. Dictionary with Different Data Types
# ==========================================================

info = {

    "Ram": {
        "Degree": "BCA",
        "Skill": "Python"
    },

    (1,2): "cat",

    "x": [1,2,3],

    "y": (1,2,3,4),

    2026: "Best Year"
}

print(info)

# Explanation:
#
# Dictionary keys and values can have
# different data types.
#
# Key          Value
# ----------------------------
# "Ram"     -> Dictionary
# (1,2)     -> String
# "x"       -> List
# "y"       -> Tuple
# 2026      -> String


# ==========================================================
# 14. values()
# ==========================================================

print(info.values())

# Explanation:
#
# values() returns ONLY the values.
#
# It ignores the keys.
#
# Output:
#
# dict_values(...)
#
# Useful when you need only stored data.


# ==========================================================
# 15. items()
# ==========================================================

print(info.items())

# Explanation:
#
# items() returns every key
# together with its value.
#
# Example:
#
# ("Ram", {...})
#
# ("x", [1,2,3])
#
# Every item is returned as a tuple:
#
# (Key, Value)


# ==========================================================
# 16. get()
# ==========================================================

print(info.get("Ram"))

# Explanation:
#
# get() safely returns the value.
#
# Difference:
#
# info["Rahul"]
#
# Output:
# KeyError
#
# info.get("Rahul")
#
# Output:
# None
#
# Therefore get() is safer.


# ==========================================================
# 17. pop()
# ==========================================================

info.pop("x")

print(info)

# Explanation:
#
# pop("x")
#
# Removes key "x"
# along with its value.
#
# Before:
#
# x -> [1,2,3]
#
# After:
#
# x is removed.


# ==========================================================
# 18. clear()
# ==========================================================

info.clear()

print(info)

# Explanation:
#
# clear() removes ALL key-value pairs.
#
# Dictionary becomes empty.
#
# Output:
#
# {}


# ==========================================================
# MOST IMPORTANT DICTIONARY METHODS
# ==========================================================

# dict()       -> Create a dictionary
# get()        -> Get value safely
# keys()       -> Returns all keys
# values()     -> Returns all values
# items()      -> Returns key-value pairs
# update()     -> Add or update values
# pop()        -> Remove a specific key
# popitem()    -> Remove the last inserted item
# clear()      -> Remove everything
# copy()       -> Create a copy of the dictionary


# ==========================================================
# INTERVIEW QUESTION
# ==========================================================

# Q. Why is Dictionary faster than List?
#
# Answer:
#
# Because Dictionary uses a HASH TABLE.
#
# Process:
#
# Key
#   ↓
# hash()
#   ↓
# Hash Value (Large Integer)
#   ↓
# Memory Index
#   ↓
# Direct Access
#
# Time Complexity (Average Case):
#
# Search : O(1)
# Insert : O(1)
# Delete : O(1)
#
# This is why dictionaries are one of the fastest
# data structures in Python for searching by key.