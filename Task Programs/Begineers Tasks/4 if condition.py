# ---------------------------------
# 1. BMI Category Program
# ---------------------------------

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")


# ---------------------------------
# 2. City to Country Program
# ---------------------------------

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ")

if city in australia:
    print(city, "is in Australia")
elif city in uae:
    print(city, "is in UAE")
elif city in india:
    print(city, "is in India")
else:
    print("City not found")


# ---------------------------------
# 3. Check if Two Cities Belong to Same Country
# ---------------------------------

city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")

if city1 in australia and city2 in australia:
    print("Both cities are in Australia")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")
elif city1 in india and city2 in india:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")
