from time import sleep

print("Welcome to the Split bill and tip calculator.")

sleep(2)

totalBill = input("What was the total of the bill? ")
totalBill = float(totalBill)
billSplit = input("How many people to split the bill? ")
billSplit = float(billSplit)

costPerPerson = round(totalBill / billSplit, 2)

print(f"Cost per person before tip will be ${costPerPerson}. ")

tipPercentage = input("What percentage tip would you like to give? ")

tipPercentage = float(tipPercentage) / 100

tipAmountAfterSplit = costPerPerson * tipPercentage 


totalToPay = costPerPerson + tipAmountAfterSplit

totalToPay = round(totalToPay, 2)

print(f"Each person should pay {totalToPay}")
