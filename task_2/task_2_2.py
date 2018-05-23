dollars = int(input("Input dollars: "))
cents = int(input("Input cents: "))
quantity = int(input("Input quantity: "))
print("Total cost is", int((dollars+(cents/100))*quantity)//1, "dollars and", int(cents*quantity % 100), "cents.")
