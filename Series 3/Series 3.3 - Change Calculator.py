import decimal

print("-------------------------")
print("Works out change")
print("-------------------------")

print("Enter cost")
#tells user to enter price of something
cost = float(input("Enter: £"))
#takes users input in £

print()

print("Enter money given")
#tell user to enter money used
money = float(input("Enter: £"))
#takes users input in £

pencecost = decimal.Decimal(cost*100)
#turns input cost into pence
pencemoney = decimal.Decimal(money*100)
#turns input money into pence

pencechange = decimal.Decimal(pencemoney - pencecost)
#takes cost away from money amount
change = decimal.Decimal(pencechange / 100)
#turns change into £

print("-------------------------")
print("Your change: £" + str("{0:.2f}".format(change)))
print("-------------------------")
#displays change from money in £ only up to 2 decimal places

 
