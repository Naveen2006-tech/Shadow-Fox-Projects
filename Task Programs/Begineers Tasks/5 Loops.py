# -------------------------------------------------
# PROGRAM 1: Dice Rolling Simulation using for loop
# -------------------------------------------------

# Import random module to generate random dice values
import random

# Number of times the dice will be rolled
total_rolls = 20

# Initialize counters
count_6 = 0               # Counts how many times 6 appears
count_1 = 0               # Counts how many times 1 appears
two_6s_in_row = 0         # Counts how many times two 6s appear consecutively

# Variable to store the previous dice roll
previous_roll = None

print("Dice Rolling Simulation:\n")

# Loop to simulate rolling the dice 20 times
for i in range(total_rolls):
    roll = random.randint(1, 6)   # Generate random number between 1 and 6
    print(f"Roll {i + 1}: {roll}")

    # Check if roll is 6
    if roll == 6:
        count_6 += 1

        # Check for consecutive 6s
        if previous_roll == 6:
            two_6s_in_row += 1

    # Check if roll is 1
    if roll == 1:
        count_1 += 1

    # Store current roll for next iteration
    previous_roll = roll

# Display dice statistics
print("\nDice Statistics:")
print("Total times rolled a 6:", count_6)
print("Total times rolled a 1:", count_1)
print("Total times rolled two 6s in a row:", two_6s_in_row)


# -------------------------------------------------
# PROGRAM 2: Jumping Jacks Workout using for loop
# -------------------------------------------------

print("\n-----------------------------------")
print("Jumping Jacks Workout Program\n")

# Total jumping jacks required
total_jumping_jacks = 100

# Counter to track completed jumping jacks
completed = 0

# Loop runs 10 times (10 sets of 10 jumping jacks)
for _ in range(10):

    # Add 10 jumping jacks per set
    completed += 10

    # Calculate remaining jumping jacks
    remaining = total_jumping_jacks - completed

    # If all 100 jumping jacks are completed
    if completed == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    # Ask user if they are tired
    tired = input("You completed 10 jumping jacks. Are you tired? (yes/y or no/n): ").lower()

    # If user says yes
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()

        # If user wants to skip
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    else:
        # If user is not tired, show remaining jumping jacks
        print(f"{remaining} jumping jacks remaining.\n")
