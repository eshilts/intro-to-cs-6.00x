# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

## Example end printout:
# Lowest Payment: 180

# REMOVE THESE #
balance = 999999
annualInterestRate = 0.18
# REMOVE THESE

monthlyInterestRate = annualInterestRate / 12.0
balanceHolder = balance
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
payment = (lowerBound + upperBound) / 2
remaining = 100

while abs(balance) > 0.001:
  totalPaid = 0
  balance = balanceHolder 

  for month in range(12):
    unpaidBalance = balance - payment
    balance += (unpaidBalance * monthlyInterestRate) - payment
    totalPaid += payment

  if balance > 0:
    lowerBound = payment
  else:
    upperBound = payment

  payment = (upperBound + lowerBound) / 2

print "Lowest payment: {0:.2f}".format(payment)
