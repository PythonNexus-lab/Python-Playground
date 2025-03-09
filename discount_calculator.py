# Get user input
total_purchase = float(input("Enter the total purchase amount: "))

# Apply discount rules
if total_purchase > 100000:
    discount = 0.10 * total_purchase
elif total_purchase > 50000:
    discount = 0.05 * total_purchase
else:
    discount = 0

# Calculate final amount
total_payment = total_purchase - discount

# Display results
print(f"Discount received: {discount:.2f}")
print(f"Total amount to be paid: {total_payment:.2f}")