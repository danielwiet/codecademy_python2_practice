class bankaccount(object):
  balance = 0

  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return('The account for %s has a balance of $%.2f' % (self.name, self.balance))

  def show_balance(self):
    print('Total balance is $%.2f' % self.balance)

  def deposit(self, amount):
    if amount <= 0:
      print('Deposit needs to be a positive amount')
      return
    else:
      print('Depositing $%.2f' % amount)
      self.balance += amount
      self.show_balance()
    
  def withdrawl(self, amount):
    if amount > self.balance:
      print('Not enough money in the account')
      return
    else:
      print('withdrawing $%.2f' % amount)
      self.balance -= amount
      self.show_balance()
    
my_account = bankaccount('Dan')
#print(my_account)
#my_account.show_balance()

#my_account.deposit(2000)
#my_account.withdrawl(1000)
#print(my_account)

print(my_account)