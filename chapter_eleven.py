"""
#Classes

import coin
"
def main():
	my_coin = Coin();
	
	print "This side is up:", my_coin.get_sideup();
	
	print "I am tossing the coin";
	my_coin.toss();
	
	print "This side is up:", my_coin.get_sideup();

main();


def main():
	my_coin = coin.Coin();
	
	print "This side is up:", my_coin.get_sideup();
	
	print 'I am going to toss the coin ten times:';
	for count in range(10):
		my_coin.toss();
		print my_coin.get_sideup();
		

main();
#



import bankaccount
		
def main():
	#get the starting balance.
	
	start_bal = float(input("Enter your starting balance:"));
	
	#create a bankaccount object.
	savings = bankaccount.BankAccount(start_bal);
	
	#Deposit the user's paycheck;
	
	pay = float(input("How much were you paid this week?"));
	print "I will deposit that into your account";
	
	savings.deposit(pay);
	
	#display the balance
	print "Your account balance is $", savings.get_balance();
	
	#get the amount to withdraw
	
	cash = float(input("How much would you like to withdraw?"));
	print "I will withdraw that from your account.";
	savings.withdraw(cash);
	
	#Display the balance/
	#print "Your account balance is $", savings.get_balance();
	
	print savings;
	
main();


import coin

def main():
	#Create three objects from the Coin class
	coin1 = coin.Coin();
	coin2 = coin.Coin();
	coin3 = coin.Coin();
	
	#Display the side of each coin that is facing up.
	print "I have three coins with these sides up:";
	print coin1.get_sideup();
	print coin2.get_sideup();
	print coin3.get_sideup();
	print " ";
	
	#Toss the coin
	print "I am tossing all three coins...";
	print " ";
	coin1.toss();
	coin2.toss();
	coin3.toss();
	
	#Display the side of each coin that is facing up
	print "Now here are the sides that are up:";
	print coin1.get_sideup();
	print coin2.get_sideup();
	print coin3.get_sideup();
	print " ";

main();


import cellphone

def main():
	man = raw_input("Enter the manufacturer:");
	mod = raw_input("Enter the model:");
	retail = float(input("Enter the retail price:"));
	
	#Create an instance of the cellphone class
	phone = cellphone.CellPhone(man, mod, retail);
	
	#display the data was entered.
	print "Here is the data that you entered:";
	print "Manufacturer:", phone.get_manufact();
	print "Model:", phone.get_model();
	print "Retail Price:", phone.get_retail_price();

main();


import cellphone

def main():
	#Get a list of CellPhone objects
	phones = make_list();
	
	#Display the data in the list
	print "Here is the data you entered:";
	display_list(phones);
	
#The make_list function gets data from the user
#for five phones. The function returns a list
#of Cellphone objects containing the data

def make_list():
	phone_list = [];
	
	#Add five cellphone objects to the list
	print "Enter data for five phones";
	for count in range(1,6):
		#Get the phone data.
		print "Phone "+str(count)+':';
		man = raw_input("Enter the manufacturer:");
		mod = raw_input("Enter the model number:");
		retail = float(input("Enter the retail price:"));
		print " ";
		
		#Create a new CellPhone object in memory and
		#assign it to the phone variable.
		phone = cellphone.CellPhone(man, mod, retail);
		
		#Add the object to the list.
		phone_list.append(phone);
	
	return phone_list;
	
#The display_list function accepts a list containing
#CellPhone objects as an argument and displays the
#data stored in each object:

def display_list(phone_list):
	for item in phone_list:
		print item.get_manufact();
		print item.get_model();
		print item.get_retail_price();

main();
	

import coin

#This program passes a Coin object as an
#argument to a function

def main():
	my_coin = coin.Coin();
	
	print my_coin.get_sideup();
	
	flip(my_coin);
	
	print my_coin.get_sideup();

def flip(coin_obj):
	coin_obj.toss();

main();


import pickle
import cellphone

FILENAME = 'cellphones.dat';

def main():
	again = 'y';
	
	output_file = open(FILENAME, 'wb');
	
	while again.lower() == 'y':
		man = raw_input("Enter the manufacturer:");
		mod = raw_input("Enter the model number:");
		retail = float(input("Enter the retail price:"));
		
		#create a CellPhone object.
		phone = cellphone.CellPhone(man,mod,retail);
		
		pickle.dump(phone,output_file);
		
		again = raw_input("Enter more phone data? (y/n):");
	
	output_file.close();
	print "The data was written to", FILENAME;

main();


#This program unpickles CellPhone objects
import pickle
import cellphone

FILENAME = 'cellphones.dat';

def main():
	end_of_file = False;
	
	input_file = open(FILENAME,'rb');
	
	#read to the end of the file
	while not end_of_file:
		try:
			#unpickle the next object
			phone = pickle.load(input_file);
			
			#display the cell phone data
			display_data(phone);
		except EOFError:
			#set the flag to indicate the end
			#of the file has been reached.
			end_of_file = True;
	
	input_file.close();

def display_data(phone):
	print "Manufacturer:",phone.get_manufact();
	print "Model Number:",phone.get_model();
	print "Retail Price: $", phone.get_retail_price();

main();


#The program manages contacts.
import contact
import pickle

#Global constants for menu choices.
LOOK_UP = 1;
ADD = 2;
CHANGE = 3;
DELETE = 4;
QUIT = 5;

FILENAME = 'contacts.dat';

def main():
	#load the existing contact dictionary and
	#assign it to mycontacts
	mycontacts = load_contacts();
	
	#initializes a variable for the user's choice.
	
	choice = 0;
	
	#process menu selections until the user
	#wants to quit the program.
	
	while choice !=QUIT:
		#Get the user's menu choice.
		choice = get_menu_choice();
		
		#Process the choice.
		if choice == LOOK_UP:
			look_up(mycontacts);
		elif choice == ADD:
			add(mycontacts);
		elif choice == CHANGE:
			change(mycontacts);
		elif choice == DELETE:
			delete(mycontacts);
	
	save_contacts(mycontacts);

def load_contacts():
	try:
		#open the contacts.dat file.
		input_file = open(FILENAME,'rb');
		
		#unpickle the dictionary.
		contact_dct = pickle.load(input_file);
		
		#close the phone_inventory.dat file.
		input_file.close();
	except IOError:
		#Could not open the file, so create
		#an empty dictionary.
		contact_dct = {};
	
	return contact_dct;

#the get_menu_choice function displays the menu
#and gets a validated choice from the user.

def get_menu_choice():
	
	print " ";
	print "Menu";
	print "-----------------";
	print "1. Look up a contact";
	print "2. Add a new contact";
	print "3. Change an existing contact";
	print "4. Delete a contact";
	print "5. Quit the program";
	print " ";
	
	#Get the user's choice.
	choice = int(input("Enter your choice:"));
	
	#validate the choice
	while choice < LOOK_UP or choice > QUIT:
		choice = int(input("Enter a valid choice:"));
	
	return choice;
	


import information

def main():
	me = information.Information("Daryl Dalman","Arkansas", 22,"917-273-2908");
	friend1 = information.Information("Luiz Fernando", "Brazil", 25, "3478451154");
	friend2 = information.Information("Lola Peng", "China", 24, "12344566");
	
	print me.get_name();
	print friend1.get_name();
	print friend2.get_name();

main();

value = [];
for item in range(1000):
	if item % 3 == 0:
		value.append(item);
	elif item % 5 == 0:
		value.append(item);
	
print value;

total = 0;
for num in value:
	total += num;

print total;
"""
my_list =[];
for num in range(1,300425737572):
	if 300425737572 % num == 0:
		my_list.append(num);
	

print my_list;

