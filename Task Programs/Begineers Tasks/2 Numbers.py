# -----------------------------
# 1. Format function example
# -----------------------------

def format_number(num, fmt):
    return format(num, fmt)

result = format_number(145, 'o')
print("1. Formatted result:", result)
print("   Representation used: Octal\n")


# -----------------------------
# 2. Area of circular pond & water calculation
# -----------------------------

pi = 3.14
radius = 84

# Area of the pond
area = pi * radius ** 2
print("2. Area of the pond:", area, "square meters")

# Bonus: Water calculation
water_per_sq_meter = 1.4  # liters
total_water = area * water_per_sq_meter

# Print without decimal point
print("   Total water in the pond:", int(total_water), "liters\n")


# -----------------------------
# 3. Speed calculation
# -----------------------------

distance = 490  # meters
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds

# Print without decimal point
print("3. Speed:", int(speed), "meters per second")
