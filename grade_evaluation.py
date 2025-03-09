# Get user input for scores
math = float(input("Enter Math score: "))
science = float(input("Enter Science score: "))
english = float(input("Enter English score: "))

# Calculate average score
average = (math + science + english) / 3

# Count subjects below 70
below_70 = sum([math < 70, science < 70, english < 70])

# Check passing conditions
if average > 75 and below_70 <= 1 or 100 in [math, science, english]:
    print("You passed!")
else:
    print("You failed.")