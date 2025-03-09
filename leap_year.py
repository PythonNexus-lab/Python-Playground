def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    try:
        # Get user input
        number = float(input("Enter a number: "))
        
        # Determine if the number is negative, positive, or zero
        result = check_number(number)
        
        # Output the result
        print(f"The number {number} is {result}.")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()