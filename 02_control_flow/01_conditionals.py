# =====================================================================
# TOPIC 3: CONTROL FLOW (IF, ELIF, ELSE)
# =====================================================================
# Control flow allows your program to make decisions and execute specific 
# blocks of code only when certain conditions are met.

# ---------------------------------------------------------------------
# 1. Comparison Operators (The Decision Makers)
# ---------------------------------------------------------------------
# Before making a decision, Python compares values. These always return True or False.
# x == y  (Is equal to? Note the double equal sign!)
# x != y  (Is NOT equal to?)
# x > y   (Greater than?)
# x < y   (Less than?)
# x >= y  (Greater than or equal to?)
# x <= y  (Less than or equal to?)


# ---------------------------------------------------------------------
# 2. Basic If / Else Structure & Indentation
# ---------------------------------------------------------------------
# CRITICAL NOTE: Python does not use curly brackets {} for code blocks. 
# It uses structural INDENTATION (4 spaces). All code indented under a 
# statement belongs to that block.

age = 19

if age >= 18:
    print("Decision: You are an adult.")
    print("This runs only if condition is True.")
else:
    print("Decision: You are a minor.")
    print("This runs only if condition is False.")

print("This line always runs because it is NOT indented!")


# ---------------------------------------------------------------------
# 3. Checking Multiple Conditions (If, Elif, Else)
# ---------------------------------------------------------------------
# Use 'elif' (short for else-if) to check multiple conditions sequentially.
# Python checks them top-to-bottom and exits the block after the first match.

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This will execute
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"\nYour grade is: {grade}")  # Outputs B


# ---------------------------------------------------------------------
# 4. Logical Operators (Combining Conditions)
# ---------------------------------------------------------------------
# You can combine multiple checks in a single 'if' statement using:
# - and: True only if BOTH conditions are true.
# - or:  True if AT LEAST ONE condition is true.
# - not: Reverses the boolean result (turns True to False, and vice-versa).

has_ticket = True
has_id = False

# Using 'and'
if has_ticket and has_id:
    print("\nAllowed into concert: Yes (Both ticket and ID present)")
else:
    print("\nAllowed into concert: No (Missing either ticket or ID)")

# Using 'or'
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("Alarm Status: Turned Off (It is a day off)")


# ---------------------------------------------------------------------
# 5. Nested If Statements (Conditions inside Conditions)
# ---------------------------------------------------------------------
# You can place an if statement inside another if statement for deeper checks.

is_logged_in = True
is_admin = True

if is_logged_in:
    print("\nUser Status: Logged in.")
    if is_admin:
        print("Access Level: Admin Panel Unlocked.")
    else:
        print("Access Level: Standard User Dashboard.")
else:
    print("\nUser Status: Please log in first.")
