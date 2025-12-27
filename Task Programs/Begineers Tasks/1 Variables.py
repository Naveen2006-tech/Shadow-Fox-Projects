# --------------------------------------------
# Python Program: Variables and Simple Interest
# --------------------------------------------

# Task 1:
# Create a variable named 'pi' and store the value 22/7
pi = 22 / 7

# Print the value of pi
print("Value of pi:", pi)

# Print the data type of pi
print("Data type of pi:", type(pi))


print("\n--------------------------------------------\n")


# Task 2:
# Attempting to create a variable named 'for'
# 'for' is a reserved keyword in Python and cannot be used as a variable name.
# Writing: for = 4
# will result in a SyntaxError.

# Correct approach: use a valid variable name
for_value = 4
print("Value stored in valid variable (for_value):", for_value)


print("\n--------------------------------------------\n")


# Task 3:
# Simple Interest Calculation

# Store the principal amount
principal = 10000   # P

# Store the rate of interest
rate = 5            # R (percentage)

# Store the time period in years
time = 3            # T

# Calculate Simple Interest using the formula:
# Simple Interest = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

# Display the Simple Interest
print("Simple Interest Calculation")
print("Principal Amount:", principal)
print("Rate of Interest:", rate)
print("Time Period:", time, "years")
print("Simple Interest:", simple_interest)
