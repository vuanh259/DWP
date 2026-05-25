def calculate_simple_interest(principal, rate, time):
    """
    Calculates the simple interest and the total amount.
    rate is expected to be a percentage (e.g., 5 for 5%)
    time is expected to be in years
    """
    # Convert interest rate from percentage to decimal
    r = rate / 100
    
    # Calculate interest
    interest = principal * r * time
    
    # Calculate total amount
    total_amount = principal + interest
    
    return interest, total_amount

def main():
    print("--- Simple Interest Calculator ---")
    try:
        principal = float(input("Enter the principal amount (P): "))
        rate = float(input("Enter the annual interest rate in % (r): "))
        time = float(input("Enter the time period in years (t): "))
        
        interest, total_amount = calculate_simple_interest(principal, rate, time)
        
        print("\n--- Results ---")
        print(f"Interest Earned (I): {interest:.2f}")
        print(f"Total Amount (A): {total_amount:.2f}")
        
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
