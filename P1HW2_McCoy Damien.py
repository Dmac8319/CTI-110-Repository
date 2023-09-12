# A brief description of the program
# 09/05/23
# CTI-110 P1HW2 - Travel Expense
# Damien McCoy
#
#Request Information
print("This program calculates and displays travel expenses.\n")
print()
budget = float(input("Enter your budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you'll spend on gas?: "))
print()
hotel = float(input("Approximately, how much will you need for accomadation/hotel?: "))
print()
food = float(input("Last, how much do you need for food?: "))
print()

#Minus expenses
balance = ((budget) - (gas) - (hotel) - (food))

#Display Results
print("----------Travel Expenses----------")
print("Location:" ,(destination))
print("Initial Budget:" , (budget))
print()
print("Fuel:" , (gas))
print("Acconmadation:" , (hotel))
print("Food:", (food))
print()
print("Remaining Balance:" , (balance))
