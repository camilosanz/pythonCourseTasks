"""
Loan payment calculator
"""
import math

# Get the details of the loan from the user: How much money do you owe, in dollars?​
money_owed = int(input('How much money do you owe, in dollars?​ '))
# Convert input to float​
float(money_owed)
# Get the annual percentage rate: what us the annual percentage rate?​
apr = int(input('what us the annual percentage rate?​ '))
# Get the monthly payment: what will your monthly payment be, in dollars?​
payment = int(input('what will your monthly payment be, in dollars? '))
# Get  months to calculate results: how many months do you want to see the results for?​
months = int(input('how many months do you want to see the results for?​ '))
# Repeat the calculation for all the months the user  wants to see results for​
for i in range(months):
  # Divide annual percentage rate by 100 to make it a percent, then divide by 12 to get the monthly insterest rate
  monthly_rate = apr/100/12
  # add in  interest
  interest_paid = money_owed * monthly_rate
  money_owed = money_owed + interest_paid
  # Make payment
  money_owed = money_owed - payment
  # Print the results 
  print("\nPaid", round(payment,2), "of which", round(interest_paid,2), "was interest")
  print("Now, I owe", round(money_owed,2))

  # add control to check if money_owed - payment < 0 then print messages and break repetition
  month_count = math.ceil(money_owed/(payment-interest_paid))

  if money_owed < 0:
      print("This is the last payment of your loan")
  else:
    print("the last payment is", round(money_owed,2))
    print("You pay off the loan in", round(month_count,0), "months")

# round the dollar amount to two decimals   