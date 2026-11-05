# =====================================================================
# TOPIC 4: LOOPS (FOR & WHILE LOOPS)
# =====================================================================
# Loops are used to repeat tasks. Python has two types of loops:
# 1. 'for' loops: Used when you know how many times you want to loop.
# 2. 'while' loops: Used when you want to loop until a condition changes.

# ---------------------------------------------------------------------
# 1. The 'for' Loop and range() function
# ---------------------------------------------------------------------
# The range(start, stop, step) function generates a sequence of numbers.
# Note: It stops exactly ONE number before the 'stop' value.

print("--- Basic For Loop (0 to 4) ---")
for i in range(5):
    print("Count:", i)  # Prints 0, 1, 2, 3, 4

print("\n--- Custom Range (1 to 5) ---")
for num in range(1, 6):
    print("Number:", num)  # Prints 1, 2, 3, 4, 5

print("\n--- Counting with a Step of 2 ---")
for even in range(2, 11, 2):
    print("Even number:", even)  # Prints 2, 4, 6, 8, 10


# ---------------------------------------------------------------------
# 2. The 'while' Loop
# ---------------------------------------------------------------------
# Runs indefinitely as long as the condition remains True.
# CRITICAL NOTE: You must update the loop variable inside, or it will create 
# an infinite loop that crashes your program!

print("\n--- While Loop Countdown ---")
countdown = 3

while countdown > 0:
    print("T-Minus:", countdown)
    countdown -= 1  # Updates the condition so the loop will eventually stop

print("Blast off!")


# ---------------------------------------------------------------------
# 3. Loop Control Statements (break & continue)
# ---------------------------------------------------------------------
# You can alter how a loop behaves dynamically using these keywords:
# - break: Exits the loop entirely immediately.
# - continue: Skips the rest of the current turn and jumps to the next iteration.

print("\n--- Using 'break' to stop early ---")
for score in range(1, 10):
    if score == 5:
        print("Found 5! Breaking out of loop completely.")
        break
    print("Current score:", score)

print("\n--- Using 'continue' to skip a value ---")
for item in range(1, 6):
    if item == 3:
        print("Skipping 3...")
        continue  # Code below this inside the loop is skipped for number 3
    print("Processing item:", item)


# ---------------------------------------------------------------------
# 4. Nested Loops (Loops inside Loops)
# ---------------------------------------------------------------------
# Useful for coordinates or multi-step matrix grids.

print("\n--- Nested Loop Grid ---")
for row in range(1, 3):       # Outer loop
    for col in range(1, 4):   # Inner loop
        print(f"(Row {row}, Col {col})", end=" ")
    print()  # Moves to a new line after inner loop finishes a row
