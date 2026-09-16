print(" WELCOME TO BILL SPLITTER")

while True:   
    bill = float(input("Enter total bill amount: ₹"))
    people = int(input("Enter number of people: "))
    tip = int(input("Enter tip percentage (0/5/10/15/20): "))

    
    if bill < 0:
        print("Error: Bill amount cannot be negative.")
        continue

    if people <= 0:
        print("Error: Number of people must be greater than 0.")
        continue

    if tip < 0:
        print("Error: Tip percentage cannot be negative.")
        continue

    if tip not in [0, 5, 10, 15, 20]:
        print("Error: Please enter tip as 0, 5, 10, 15, or 20.")
        continue

    tip_amount = bill * (tip/100)
    final_bill = bill + tip_amount
    per_person = final_bill / people
    
    print(f"\nTip Amount: ₹{tip_amount:.2f}")
    print(f"Total Bill (with tip): ₹{final_bill:.2f}")
    print(f"Each person should pay: ₹{per_person:.2f}")


    again = input("\nWould you like to calculate another bill? (y/n): ")

    if again != "y":
        print("\nThank you for using Bill Splitter!")
        break

print("Program ended.")

  

