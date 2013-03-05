# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

## Example monthly printout:
# Month: 1
# Minimum monthly payment: 96.0
# Remaining balance: 4784.0
## Example end printout:
# Total paid: 96.0
# Remaining balance: 4784.0

# REMOVE THESE #
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# REMOVE THESE

monthlyInterestRate = annualInterestRate / 12.0
unpaidBalance = balance
totalPaid = 0

for month in range(12):
  minimumMonthlyPayment = monthlyPaymentRate * balance
  totalPaid += minimumMonthlyPayment
  unpaidBalance = balance -  minimumMonthlyPayment
  interest = monthlyInterestRate * unpaidBalance
  balance = unpaidBalance + interest

  print "Month: {0}".format(month + 1)
  print "Minimum monthly payment: {0:.2f}".format(minimumMonthlyPayment)
  print "Remaining balance: {0:.2f}".format(balance)
  
print "Total paid: {0:.2f}".format(totalPaid)
print "Remaining balance: {0:.2f}".format(balance)
