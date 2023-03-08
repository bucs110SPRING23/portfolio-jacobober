rate = float(input("Please enter the current exchange rate for the Euro to Dollar "))
##OR CAN DO
# rate = input("Please enter the current exchange rate for the Euro to Dollar")
# rate = float(rate)
# SAME THING
amount = float(input("Please enter the amount of currency to exchange "))

new_amount = amount * rate
minus_fees = new_amount - 3
print("Your result minus a $3 convenience fee is : ", minus_fees)
