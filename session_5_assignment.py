import random

def check_number():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

def check_even_odd():
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")

def grade_classification():
    score = int(input("Enter test score (0-100): "))
    if 80 <= score <= 100:
        print("Grade: A")
    elif 70 <= score <= 79:
        print("Grade: B")
    elif 60 <= score <= 69:
        print("Grade: C")
    elif 50 <= score <= 59:
        print("Grade: D")
    else:
        print("Grade: E")

def largest_of_three():
    a, b, c = float(input("Enter first number: ")), float(input("Enter second number: ")), float(input("Enter third number: "))
    print(f"The largest number is: {max(a, b, c)}")

def leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")

def calculator():
    num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/" and num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Invalid operation."
    
    print(f"Result: {result}")

def bmi_calculator():
    weight, height = float(input("Enter weight (kg): ")), float(input("Enter height (m): "))
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
    
    print(f"Your BMI is {bmi:.2f}, Category: {category}")

def triangle_type():
    a, b, c = float(input("Enter side 1: ")), float(input("Enter side 2: ")), float(input("Enter side 3: "))

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilateral Triangle")
        elif a == b or a == c or b == c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
    else:
        print("Not a valid triangle")

def login_system():
    username, password = input("Enter username: "), input("Enter password: ")

    if username == "admin" and password == "admin123":
        print("Admin access granted")
    elif username == "user" and password == "user123":
        print("Limited access granted")
    elif username == "guest":
        print("Minimal access granted")
    else:
        print("Access denied")

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        
        if user_choice == "quit":
            print("Game Over!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

# Menu-based system
while True:
    print("\nChoose a program to run:")
    print("1. Check Positive or Negative")
    print("2. Check Even or Odd")
    print("3. Grade Classification")
    print("4. Largest of Three Numbers")
    print("5. Leap Year Checker")
    print("6. Simple Calculator")
    print("7. BMI Calculator")
    print("8. Triangle Type Checker")
    print("9. Login System")
    print("10. Rock-Paper-Scissors Game")
    print("0. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        check_number()
    elif choice == "2":
        check_even_odd()
    elif choice == "3":
        grade_classification()
    elif choice == "4":
        largest_of_three()
    elif choice == "5":
        leap_year()
    elif choice == "6":
        calculator()
    elif choice == "7":
        bmi_calculator()
    elif choice == "8":
        triangle_type()
    elif choice == "9":
        login_system()
    elif choice == "10":
        rock_paper_scissors()
    elif choice == "0":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")
