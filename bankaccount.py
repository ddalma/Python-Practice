class BankAccount:
	#the __init__ methods accepts an argument for
	#the account's balance. It is assigned to
	#the __balance attribute.
	
	def __init__(self,bal):
		self.__balance = bal;
	
	#The deposit method makes a deposit into the account
	
	def deposit(self,amount):
		self.__balance += amount;
		
		#the withdraw method withdraws an amount
		#from the account
		
	def withdraw(self,amount):
		if self.__balance >= amount:
			self.__balance -= amount;
		else:
			print "Error: Insufficient funds";
	
	#the get_balance method returns the 
	#account balance.
	
	def get_balance(self):
		return self.__balance;
		
	def __str__(self):
		return "The balance is $", self.__balance;