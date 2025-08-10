from time import sleep  # To pause after showing a pattern

# =========================
# Pattern Functions
# =========================

# --- Right Patterns ---
def right_triangle(size):
    # Normal right-angled triangle
    for i in range(1, size + 1):
        print("*" * i)

def inverted_right_triangle(size):
    # Upside-down right-angled triangle
    for i in range(size, 0, -1):
        print("*" * i)

def right_triangle_hollow(size):
    # Right-angled triangle with only borders
    for i in range(1, size + 1):
        if i == 1:
            print("*")  # Top row
        elif i == size:
            print("*" * size)  # Bottom row
        else:
            print("*" + " " * (i - 2) + "*")  # Middle rows with spaces

def inverted_right_triangle_hollow(size):
    # Upside-down right-angled triangle with only borders
    for i in range(size, 0, -1):
        if i == size:
            print("*" * size)  # First row
        elif i == 1:
            print("*")  # Last row
        else:
            print("*" + " " * (i - 2) + "*")  # Middle rows with spaces

# --- Left Patterns ---
def left_triangle(size):
    # Left-angled triangle
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * i)

def inverted_left_triangle(size):
    # Upside-down left-angled triangle
    for i in range(size, 0, -1):
        print(" " * (size - i) + "*" * i)

def left_triangle_hollow(size):
    # Left-angled triangle with only borders
    for i in range(1, size + 1):
        if i == 1:
            print(" " * (size - 1) + "*")  # Top point
        elif i == size:
            print("*" * size)  # Base row
        else:
            print(" " * (size - i) + "*" + " " * (i - 2) + "*")  # Middle rows

def inverted_left_triangle_hollow(size):
    # Upside-down left-angled triangle with only borders
    for i in range(size, 0, -1):
        if i == size:
            print("*" * size)  # Top row
        elif i == 1:
            print(" " * (size - 1) + "*")  # Last point
        else:
            print(" " * (size - i) + "*" + " " * (i - 2) + "*")  # Middle rows

# --- Pyramid Patterns ---
def pyramid(size):
    # Normal pyramid
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * (2 * i - 1))

def inverted_pyramid(size):
    # Upside-down pyramid
    for i in range(size, 0, -1):
        print(" " * (size - i) + "*" * (2 * i - 1))

# --- Diamond ---
def diamond(size):
    # Diamond shape
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * (2 * i - 1))
    for i in range(size - 1, 0, -1):
        print(" " * (size - i) + "*" * (2 * i - 1))

# --- Hourglass ---
def hourglass(size):
    # Hourglass shape
    for i in range(size, 0, -1):
        print(" " * (size - i) + "*" * (2 * i - 1))
    for i in range(2, size + 1):
        print(" " * (size - i) + "*" * (2 * i - 1))

# --- Square Patterns ---
def square(size):
    # Solid square
    for _ in range(size):
        print("*" * size)

def hollow_square(size):
    # Square with only borders
    for i in range(size):
        if i == 0 or i == size - 1:
            print("*" * size)  # Top or bottom row
        else:
            print("*" + " " * (size - 2) + "*")  # Middle rows with spaces

# =========================
# Main Menu
# =========================
while True:
    # Show main menu
    print("\nWelcome to Pattern Printer")
    print("Choose a pattern type:")
    print("1. Right patterns")
    print("2. Left-Angled patterns")
    print("3. Pyramid patterns")
    print("4. Diamond")
    print("5. Hourglass")
    print("6. Square")
    choice = input("Enter the number or 'e' to exit: ")

    if choice.lower() == "e":
        print("Thank you for using the app!")  # Exit message
        break
    elif not choice.isdigit():
        print("Invalid input! Please enter a number.")  # Error for non-numbers
        continue

    choice = int(choice)

    # --- Right patterns menu ---
    if choice == 1:
        print("\nRight Patterns:")
        print("1. Right-Angled Triangle")
        print("2. Inverted Right-Angled Triangle")
        print("3. Right-Angled Triangle (Hollow)")
        print("4. Inverted Right-Angled Triangle (Hollow)")
        sub = input("Enter the pattern number: ")
        if sub.isdigit():
            size = int(input("Enter the size: "))
            if sub == "1": right_triangle(size)
            elif sub == "2": inverted_right_triangle(size)
            elif sub == "3": right_triangle_hollow(size)
            elif sub == "4": inverted_right_triangle_hollow(size)
            else: print("Invalid number!")
        else:
            print("Invalid input!")
        sleep(2)  # Pause before menu returns

    # --- Left patterns menu ---
    elif choice == 2:
        print("\nLeft Patterns:")
        print("1. Left-Angled Triangle")
        print("2. Inverted Left-Angled Triangle")
        print("3. Left-Angled Triangle (Hollow)")
        print("4. Inverted Left-Angled Triangle (Hollow)")
        sub = input("Enter the pattern number: ")
        if sub.isdigit():
            size = int(input("Enter the size: "))
            if sub == "1": left_triangle(size)
            elif sub == "2": inverted_left_triangle(size)
            elif sub == "3": left_triangle_hollow(size)
            elif sub == "4": inverted_left_triangle_hollow(size)
            else: print("Invalid number!")
        else:
            print("Invalid input!")
        sleep(2)

    # --- Pyramid patterns menu ---
    elif choice == 3:
        print("\nPyramid Patterns:")
        print("1. Pyramid")
        print("2. Inverted Pyramid")
        sub = input("Enter the pattern number: ")
        if sub.isdigit():
            size = int(input("Enter the size: "))
            if sub == "1": pyramid(size)
            elif sub == "2": inverted_pyramid(size)
            else: print("Invalid number!")
        else:
            print("Invalid input!")
        sleep(2)

    # --- Diamond pattern ---
    elif choice == 4:
        size = int(input("Enter the size: "))
        diamond(size)
        sleep(2)

    # --- Hourglass pattern ---
    elif choice == 5:
        size = int(input("Enter the size: "))
        hourglass(size)
        sleep(2)

    # --- Square patterns menu ---
    elif choice == 6:
        print("\nSquare Patterns:")
        print("1. Square")
        print("2. Hollow Square")
        sub = input("Enter the pattern number: ")
        if sub.isdigit():
            size = int(input("Enter the size: "))
            if sub == "1": square(size)
            elif sub == "2": hollow_square(size)
            else: print("Invalid number!")
        else:
            print("Invalid input!")
        sleep(2)

    # --- If user enters wrong menu number ---
    else:
        print("Invalid main menu choice!")
