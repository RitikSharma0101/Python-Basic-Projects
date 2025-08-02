from random import randint # For simulating dice rolls
from time import sleep # For adding delay effect

# Main loop: run until user types 'e' to exit
while True:
    user = input("Enter your number or Exit(e): ")

    if user == "e":
        print("Thanks for playing!")
        break

    elif user.isdigit(): # Check if input is a number
            rolls = []   # List to store all dice results

            # Roll the dice as many times as the user entered
            for i in range(1,(int(user)+1)):
                print("Rolling the dice...", end="\r") # Simulate rolling effect
                sleep(2) # Wait 2 seconds for suspense
                a = randint(1,6) # Random number between 1-6
                rolls.append(a) # Save the roll
                print(f"You rolled a {a}!")

                # Display corresponding ASCII art
                match a:
                    case 1:
                        print("""
+-------+
|       |
|   o   |
|       |
+-------+""")

                    case 2:
                        print("""
+-------+
|o      |
|       |
|      o|
+-------+""")

                    case 3:
                        print("""
+-------+
|o      |
|   o   |
|      o|
+-------+""")

                    case 4:
                        print("""
+-------+
|o     o|
|       |
|o     o|
+-------+""")

                    case 5:
                        print("""
+-------+
|o     o|
|   o   |
|o     o|
+-------+""")

                    case 6:
                        print("""
+-------+
|o     o|
|o     o|
|o     o|
+-------+""")
            # After rolling is done, show summary
            print(f"\nYour Rolls: {rolls}")
            print(f"Total Score: {sum(rolls)}")

    else:
        # Handle invalid input
        print("Invalid input. Enter a number or 'e' to exit.")
