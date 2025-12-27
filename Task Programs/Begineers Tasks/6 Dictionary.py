# ----------------------------------------
# PART 1: Friends List and Tuple Creation
# ----------------------------------------

# Create a list of friends' names (at least 5 names)
friends = ["Aditya", "Rahul", "Sneha", "Priya", "Amit"]

# Create an empty list to store tuples
friends_name_length = []

# Loop through each friend's name
for name in friends:
    # Create a tuple with name and length of the name
    name_tuple = (name, len(name))
    
    # Add the tuple to the list
    friends_name_length.append(name_tuple)

# Print the list of tuples
print("Friends and length of their names:")
print(friends_name_length)


# ----------------------------------------
# PART 2: Trip Expense Tracking using Dictionaries
# ----------------------------------------

# Dictionary for your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Dictionary for your partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for you
your_total = sum(your_expenses.values())

# Calculate total expenses for your partner
partner_total = sum(partner_expenses.values())

# Print total expenses
print("\nTotal Expenses:")
print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Determine who spent more money
if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount of money.")

# ----------------------------------------
# Finding category with significant difference
# ----------------------------------------

# Variable to track maximum difference
max_difference = 0

# Variable to store the category with maximum difference
difference_category = ""

# Loop through each expense category
for category in your_expenses:
    # Calculate absolute difference for each category
    difference = abs(your_expenses[category] - partner_expenses[category])
    
    # Check if this difference is the largest
    if difference > max_difference:
        max_difference = difference
        difference_category = category

# Print the category with the highest spending difference
print("\nCategory with the highest spending difference:")
print(difference_category, "with a difference of", max_difference)
