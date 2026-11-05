# =====================================================================
# TOPIC 1: VARIABLES AND DATA TYPES
# =====================================================================
# In Python, a variable is a named container used to store data.
# Unlike other languages, you don't need to declare a variable's type.
# Python figures it out automatically (Dynamic Typing).

# ---------------------------------------------------------------------
# 1. Core Data Types
# ---------------------------------------------------------------------

# Integer (Whole numbers)
age = 25 
print("Age Type:", type(age))  # type() tells you what the data type is

# Float (Decimal numbers)
price = 19.99
print("Price Type:", type(price))

# String (Text - wrapped in single or double quotes)
name = "Ratna"
greeting = 'Hello, World!'
print("Name Type:", type(name))

# Boolean (True or False - must be capitalized)
is_learning_python = True
is_tired = False
print("Boolean Type:", type(is_learning_python))


# ---------------------------------------------------------------------
# 2. Naming Rules & Best Practices
# ---------------------------------------------------------------------
# - Must start with a letter or an underscore (_).
# - Cannot start with a number.
# - Can only contain alphanumeric characters and underscores (A-z, 0-9, and _).
# - Case-sensitive (age, Age, and AGE are three different variables).
# - Best practice: Use 'snake_case' (lowercase words split by underscores).

user_home_address = "123 Main St"  # Good snake_case
# 2user = "Error"                  # INVALID: Starts with number
# user-name = "Error"              # INVALID: Contains a hyphen


# ---------------------------------------------------------------------
# 3. Dynamic Typing (The Shifting Box)
# ---------------------------------------------------------------------
# You can change a variable's data type at any time just by assigning a new value.

box = "I am a string text"
print("Box contains text:", box)

box = 100  # Re-assigned to an integer
print("Box now contains a number:", box)


# ---------------------------------------------------------------------
# 4. Type Casting (Converting Types Manually)
# ---------------------------------------------------------------------
# Sometimes you need to force a variable from one data type to another.

x = "10"  # This is a String because of the quotes
y = 5     # This is an Integer

# print(x + y) # ERROR: You cannot add a string and a number together!

# Fix it by casting x into an integer:
converted_x = int(x)
total = converted_x + y
print("Sum after Type Casting:", total)  # Outputs 15

# Other casting functions:
str_number = str(45)    # Converts integer 45 to string "45"
float_number = float(7)  # Converts integer 7 to decimal 7.0
