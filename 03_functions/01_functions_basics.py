# =====================================================================
# TOPIC 5: FUNCTIONS (BASICS, ARGUMENTS, & RETURN VALUES)
# =====================================================================
# A function is a block of organized, reusable code. It only runs 
# when it is explicitly "called".

# ---------------------------------------------------------------------
# 1. Defining and Calling a Simple Function
# ---------------------------------------------------------------------
# Use the 'def' keyword to create a function. 
# Give it a descriptive name followed by parentheses ().

def greet_user():
    """This is a docstring. It documents what the function does."""
    print("Hello! Welcome to your Python study notebook.")

# Defining a function does NOT run it. You must call it:
greet_user()  # Invokes the function


# ---------------------------------------------------------------------
# 2. Passing Information (Parameters and Arguments)
# ---------------------------------------------------------------------
# - Parameters: The variable placeholders defined inside the function's brackets.
# - Arguments: The actual values you send to the function when calling it.

def personalized_greeting(username, course_name):
    print(f"Hi {username}, good luck with your {course_name} course!")

# Calling with positional arguments (order matters):
personalized_greeting("Ratna", "Python Basics")


# ---------------------------------------------------------------------
# 3. Default Parameter Values
# ---------------------------------------------------------------------
# You can assign a fallback default value to a parameter if no argument is provided.

def power_calculator(base, exponent=2):
    result = base ** exponent
    print(f"{base} to the power of {exponent} is: {result}")

power_calculator(5)      # Uses default exponent of 2 -> Outputs 25
power_calculator(5, 3)   # Overrides default with 3  -> Outputs 125


# ---------------------------------------------------------------------
# 4. Returning Values (The 'return' Keyword)
# ---------------------------------------------------------------------
# print() only displays text to the screen. 
# 'return' sends data BACK to the main program so you can store it or reuse it.
# CRITICAL NOTE: A function exits immediately when it hits a return statement!

def add_numbers(num1, num2):
    sum_result = num1 + num2
    return sum_result  # Sends the total back

# Capture the returned value into a new variable:
total_score = add_numbers(45, 55)
print("\nThe calculated total score is:", total_score)


# ---------------------------------------------------------------------
# 5. Variable Scope (Local vs. Global)
# ---------------------------------------------------------------------
# - Local Variables: Created inside a function and CANNOT be accessed outside it.
# - Global Variables: Created in the main body of the script and accessible anywhere.

global_var = "I am global"

def scope_test():
    local_var = "I am local"
    print("\nInside function:", global_var)  # Works
    print("Inside function:", local_var)   # Works

scope_test()

print("Outside function:", global_var)     # Works
# print("Outside function:", local_var)    # ERROR! local_var does not exist out here.
