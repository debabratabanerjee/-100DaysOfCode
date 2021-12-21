print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))



tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

tip_as_percentage = tip_percentage/100

total_tip= total_bill*tip_as_percentage
total_bill = total_bill + total_tip

people_splitting = int(input("How many people to split the bill? " ))



total_split = round(total_bill/people_splitting,2)


print(f"Each person should pay: ${total_split} ")


