# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

## Example end printout:
# Lowest Payment: 180

# REMOVE THESE #
balance = 320000
annualInterestRate = 0.2
# REMOVE THESE

monthlyInterestRate = annualInterestRate / 12.0                                 
totalPaid = 0                                                                   
balanceHolder = balance                                                         

for payment in range(10, balance, 10):                                          
  balance = balanceHolder                                                       

  for month in range(12):                                                       
    unpaidBalance = balance - payment                                           
    balance += (unpaidBalance * monthlyInterestRate) - payment                  
    totalPaid += payment                                                        

  if unpaidBalance <= 0:                                                        
  break                                                                       
                                                                
print "Lowest payment: {0}".format(payment) 
