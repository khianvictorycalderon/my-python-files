# Loan Calculator
while True:
    # Initial Variables
    month = 1

    # Input
    print()
    amount = float(input("How much would you like to loan?\n-> $"))
    period = int(input("How many months would you like to pay it?\n-> "))
    annual_interest_rate = float(input("What is the annual interest rate (in percentage)?\n-> "))

    # Calculations
    principal = amount / period
    monthly_interest_rate = annual_interest_rate / 100 / 12

    # Table Header
    print()
    print("\tMonth\t\t|\tPayment\t\t|\tInterest\t|\tPrincipal\t|\tBalance")
    print("-" * 120)

    # Table Data
    while month <= period:
        interest = amount * monthly_interest_rate # Interest for the current month
        payment = principal + interest # Total payment for this month
        amount -= principal # Deduct the principal from the balance

        # Print the current month's details
        print(f"\t{month}\t\t|\t${round(payment, 2)}\t\t|\t${round(interest, 2)}\t\t|\t${round(principal, 2)}\t\t|\t${round(amount, 2)}")
        month += 1

    print("-" * 120)

    # Ask another
    print()
    again = input("Would you like to try again?\nType 'yes' if you would like to.\nType any other character to exit.\n-> ")
    if again.lower() != "yes":
        print()
        print("Thank you for using this program!")
        break
