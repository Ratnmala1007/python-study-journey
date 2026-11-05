# =====================================================================
# TOPIC 2: ARITHMETIC OPERATORS & USER INPUT
# =====================================================================
# This section covers how Python performs math calculations and how 
# to collect dynamic information from someone interacting with your program.

# ---------------------------------------------------------------------
# 1. Arithmetic Operators (The Math Engines)
# ---------------------------------------------------------------------
a = 15
b = 4

print("--- Arithmetic Operations ---")
print("Addition (+):", a + b)         # 19
print("Subtraction (-):", a - b)      # 11
print("Multiplication (*):", a * b)   # 60
print("Division (/):", a / b)         # 3.75 (Always returns a decimal float)

# Special Operators you need to memorize:
print("Floor Division (//):", a // b) # 3 (Divides and rounds down to whole number)
print("Modulus (%):", a % b)           # 3 (Returns ONLY the remainder of division)
print("Exponentiation (**):", a ** b)  # 50625 (15 to the power of 4)


# ---------------------------------------------------------------------
# 2. Assignment Operators (Shortcuts)
# ---------------------------------------------------------------------
# Instead of writing x = x + 5, you can use a shorthand trick.
score = 10
score += 5   # Equivalent to: score = score + 5
score -= 2   # Equivalent to: score = score - 2
print("\nFinal Score Shortcut:", score) # 13


# ---------------------------------------------------------------------
# 3. Getting User Input
# ---------------------------------------------------------------------
# The input() function stops the program and waits for the user to type text.
# CRITICAL NOTE: input() ALWAYS saves data as a String (text), even if numbers are typed!

# Type your name in Colab when prompted:
user_name = input("\nEnter your name: ")
print("Welcome to the course, " + user_name + "!") 


# ---------------------------------------------------------------------
# 4. Combining Input with Type Casting
# ---------------------------------------------------------------------
# Because input() returns text, you must convert it if you want to do math.

birth_year_string = input("\nEnter your birth year (e.g., 2000): ")

# Convert the text string into a whole number integer to calculate age:
birth_year = int(birth_year_string)
current_year = 2026
calculated_age = current_year - birth_year

print("You will turn or have turned:", calculated_age, "years old in 2026.")
