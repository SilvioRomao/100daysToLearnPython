# Get the values
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? €"))
tip = int(input("What percentage tip would like to give? 10,12, or 15? "))
Num_People = int(input("How many people to split the bill? "))

# Calculate the result
result = bill * (1 + tip / 100) / Num_People

# Print the value to pay

print(f"Each person should pay: €{result:.2f}")