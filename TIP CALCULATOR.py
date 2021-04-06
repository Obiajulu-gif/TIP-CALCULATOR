#Welcome Statement For the User
print("Welcome To the Tip calculator")

#asking for the User Total Bill
#converting from String to Integer(Because input give out a string)
#we also add a float to it so that we will get the most accurate result from it
totalBill = float(input ("What was the Total Bill? \n$"))
totalBill_as_int = int(totalBill)


#asking for the User Percentage Tip
#coverting from String to Integer
#we add a float to the input
percentageTip = float(input ("What Percentage Tip would you Like To Give? 10, 12, or 15?\n"))
percentageTip_as_int = int(percentageTip)


#asking for the User Spill Bill
#converting from String to Integer
spilledBill = float(input ("How Many People To Split the Bill?\n"))
spilledBill_as_int = int(spilledBill)

#this section try to calculate the inputs from the above
calculateBill = ((percentageTip_as_int / 100) * totalBill_as_int) +  totalBill_as_int

#this section is trying to round the float Number Down To a Two Digit
# calculateBill_as_RoundNumber = round(calculateBill,2)
#this Line of code below will do the same as the One Above in rounding off  numbers
calculateBill_as_RoundNumber = "{:.2f}".format(calculateBill)


# this section will Print Out the Command
print (f"Each person should pay: ${calculateBill_as_RoundNumber}")
