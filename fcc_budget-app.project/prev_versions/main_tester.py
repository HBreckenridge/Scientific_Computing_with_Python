# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")
#food.deposit(1000, "initial deposit")
#food.withdraw(90000, "farts")

#Auto = budget.Category("Automobile")
#Auto.deposit(10000, "i gots the moneyz")
#Auto.withdraw(1009, "rat farts")
#Auto.get_balance()
#entertainment = budget.Category("Entertainment")
#entertainment.deposit(6000, "super duper ballz di duper")
#entertainment.withdraw(1009, "movies")
#entertainment.get_balance()
#Auto.transfer(20, entertainment)
#food.ledger = []
#Auto.ledger = []
#entertainment.ledger = []
#food.PrintLedger()
#entertainment.PrintLedger()
#Auto.PrintLedger()
#print(food)
#create_spend_chart([Auto,entertainment])

#entertainment.get_balance()

    #print('%.2f' % (total/len(range(1,N+1))))
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
#food.withdraw(105.55)
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
entertainment.withdraw(33.40)
business.withdraw(10.99)
food.transfer(20, entertainment)
print(food)
