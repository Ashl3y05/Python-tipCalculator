#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the Tip Calculator!")
totalBill = float(input("Total Bill?:")) #getting the total bill and converting it to a float
numberOfPayees = int(input("How Many are paying?:")) #getting the number of people paying and converting it to an integer
tipPercentage = float(input("How much tip you want to give in percentage?")) #getting the tip percentage and converting it to a float
tip = totalBill * (tipPercentage/100) #dividing the tip percentage by 100 to get the decimal value of the tip and multiplying it by the total bill to get the tip

totalBill += tip #adding the tip to the total bill
print(totalBill)
billPerPreson= totalBill/numberOfPayees #dividing the total bill by the number of people paying to get the bill per person
finalAmount= round(billPerPreson,2)
finalAmount = "{:.2f}".format(billPerPreson) #formatting the bill per person to 2 decimal places"
print(f"Individual payment: {finalAmount}")
