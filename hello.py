"""
original_price = input("Enter the price of the item: ");
discount = input("Enter the discount (enter a whole percentage): ");
percent_to_frac = discount/100.00;

overall_price = original_price - (original_price *percent_to_frac);
print("The overall price is: ", overall_price);
savings = original_price-overall_price;
print("You are saving: ", savings);

2.
score1 = float(input("Enter grade of the first exam: "));
score2 = float(input("Enter grade of the second exam: "));
score3 = float(input("Enter grade of the third exam: "));

average = (score1 + score2+ score3)/ 3.0

print("The average of exam grades are: ", average);


future_value = input("Enter the desired future value: ");
rate = float(input("Enter the annual interest rate: ")/100.00);
years = input("Enter the number of years the money will grow: ");
present = future_value / ((1 + rate)**years);
print("You will need to deposit this amount: ", present);


#3.

name = raw_input("What is your name: ");
address = raw_input("What is your address, with city, state and zip: ");
tele_number = input("What is your number: ");
major = raw_input("What is your major: ");
print ("Name: ", name);
print("address: ",address);
print("telephone number: ",tele_number);
print("major: ", major); 


#4.
total_sale = float(input("Enter the amount of total sales: "));
annual_profit =total_sale -  (total_sale * .23);
print("The annual profit is: ",annual_profit);



#5.

print("One acre of land is 43,650 square feet");
square_feet = input("Enter the number of square feet: ");
total_acre = square_feet / 43650;
print "The total amount of acres is: ", total_acre;


#6.
item1 = input("Enter the price of the first item: ");
item2 = input("Enter the price of the second item: ");
item3 = input("Enter the price of the third item: ");
item4 = input("Enter the price of the fourth item: ");
item5 = input("Enter the price of the fifth item: ");

sales_tax = .06;
total_price  = item1 + item2 + item3 + item4 + item5;
amount_of_sales_tax = total_price * sales_tax;
overall_price = total_price + amount_of_sales_tax;

print "The amount of sales tax: ", amount_of_sales_tax;
print "Overall price: ", overall_price;

speed = 60.00;
distance1 = speed * 5;
distance2 = speed * 8;
distance3 = speed * 12;

print "The distance the car will travel in 5 hours is: ", distance1," miles";
print "The distance the car will travel in 8 hours is: ", distance2," miles";
print "The distance the car will travel in 12 hours is: ", distance3," miles";

#7.

amount_of_purchase = input("Enter the amount of purchase: ");
states_sales_tax = 0.04;
country_sales_tax = 0.02;
total_sales_tax = states_sales_tax + country_sales_tax;
total_of_the_sale = amount_of_purchase + (amount_of_purchase * total_sales_tax);
print "The total sales tax: ", total_sales_tax;
print "The total of the salw: ", total_of_the_sale;

#8.
miles_driven = input("Enter the number of miles driven: ");
gallons_of_gas_used = input("Enter the number of gallons used: ");
MPG = miles_driven / gallons_of_gas_used;
print "The car's MPG is: ", MPG;


#9.

meal_amount = input("Enter the price of the meal: ");
tip = meal_amount * .15;
sales_tax = meal_amount * .07;
total_price = meal_amount + tip + sales_tax;

print "The tip is: ", tip;
print "Sales tax is: ", sales_tax;
print "The total price is: ", total_price;


#10.
celsius = input("Enter the temperature in celsius: ");
farenheit = (9*celsius)/5 + 32;
print "The temperature in farenheit is: ", farenheit;


#11.
number_of_shares = 1000;
initial_stock_price = 32.87;
investment = number_of_shares * initial_stock_price;
commission_bought = investment * 0.02;

print "Initial investment: ",investment;
print "Commission for broker: ",commission_bought;

after_stock_price = 33.92;
trading = number_of_shares * after_stock_price;
commission_sold = trading * 0.02;

profit = trading - investment;

print "Trading price: ",trading;
print "Comission for broker: ", commission_sold;

print "Profit: ", profit;

#functions
def main():
	print "I have a message for you!";
	message();
	print "Goodbye";

def message():
	print "I am King Arthur";
	print "King of the Britons";

main();



def main():
	print "This program converts measurements";
	print "in cups to fluid ounces. For your ";
	print "reference the formula is: ";
	print "1 cup = 8 fluid ounces ";
	
	cups = input("Enter the number of cups: ");
	convert(cups);

def convert(number):
	ounces = number * 8;
	print "That converts to", ounces, "ounces";
	
main();


def main():
	first_name = raw_input("Enter your first name: ");
	last_name = raw_input("Enter your last name: ");
	reverse(first_name, last_name);

def reverse(first, last):
	print "Your name reverse is: ";
	print last, first;

main();

#1.
def main():
	number = input('Enter a number: ');
	times_ten(number);
	
def times_ten(num):
	value = 10 * num;
	print "The number you enter is: ",num;
	print "Times 10 is: ", value;

main(); 

#2.
def main():
	num = input('Enter a number: ');
	show_value(num);

def show_value(number):
	print "The number you entered is: ", number;

main();

#3.
def main():
	a = input('Enter a number: ');
	b = input('Enter another number: ');
	c = input('Enter anoter number: ');
	my_function(a,b,c);

def my_function(a,b,c):
	d = (a + c) / b;
	print d;
	
main();

#4.

def main():
	kilo = float(input('Enter the distance in kilometers: '));
	kilo_to_miles(kilo);

def kilo_to_miles(number):
	miles = number * 0.6214;
	print "Kilometers: ", number;
	print "Kilometers to miles: ", miles;

main();

#5.

def main():
	amount = input("Enter the amount of purchase: ");
	taxes(amount);
	
def taxes(number):
	states_sales_tax = number * 0.04;
	country_sales_tax = number * 0.02;
	total_price = number + states_sales_tax + country_sales_tax;
	print "States sales tax: ", states_sales_tax;
	print "Country sales tax: ", country_sales_tax;
	print "The total price: ", total_price;
	
main();

#6.
def main():
	amount = input("Enter the cost of the building: ");
	insurance(amount);

def insurance(number):
	total_insurance = number * .80;
	print "The total insurance is: ", total_insurance;

main();

#7.
def main():
	acre_value = input("Enter the value of land: ");
	print "The acre value is: ", acre_value;
	assessment_value(acre_value);

def assessment_value(number):
	assess_value = number * 0.60;
	print "The assessment value: ", assess_value;
	property_tax(assess_value);

def property_tax(num):
	p_tax = (num / 100.00) * .64;
	print "The property tax is: ", p_tax;

main();
	
#8.

def main():
	weight = input("Enter weight: ");
	height = input("Enter height: ");
	bmi(weight, height);

def bmi(w, h):
	BMI = (w * 703)/(h**2);
	print "The BMI is: ", BMI;

main();

#9.
def main():
	fat_gram = input('Enter the fat grams: ');
	carb_gram = input('Enter the fat gram: ');
	calories_from_fat(fat_gram);
	calories_from_carbs(carb_gram);

def calories_from_fat(fat):
	calories_of_fat = fat * 9;
	print "Calories from fat: ", calories_of_fat;

def calories_from_carbs(carbs):
	calories_of_carbs = carbs * 4;
	print "Calories for carbs: ", calories_of_carbs;
	
main();

#10.
def main():
	class_a_tickets = input('Enter the number of tickets you want for class A: ');
	class_b_tickets = input('Enter the number of tickets you want for class B: ');
	class_c_tickets = input('Enter the amount of tickets you want for class C: ');
	total_tickets = class_a_tickets + class_b_tickets + class_c_tickets;
	print 'Total tickets: ', total_tickets;
	
	price_of_a(class_a_tickets);
	price_of_b(class_b_tickets);
	price_of_c(class_c_tickets);

def price_of_a(num):
	cost = num *15;
	print 'Price of A seats: ', cost;
	
def price_of_b(num):
	cost = num * 12;
	print 'Price of B seats: ', cost;

def price_of_c(num):
	cost = num * 9;
	print 'price of C seats: ', cost;
	
main();


#11.
def main():
	total_sales = input('Enter the total sales of the month: ');
	state_sales_tax(total_sales);
	country_sales_tax(total_sales);
	total_sales_tax(total_sales);

def state_sales_tax(num):
	state_tax = num * 0.04;
	print 'States Tax: ', state_tax;

def country_sales_tax(num):
	country_tax = num * 0.02;
	print 'Country tax: ', country_tax;

def total_sales_tax(num):
	total = num + (num*0.04) + (num*0.02);
	print 'Total sales tax: ', total;

main();

name1 = raw_input('Enter a name (last name first): ');
name2 = raw_input('Enter a name (last name first): ');

print 'Here are the names, listed alphabetically.';

if name1 < name2:
	print name1;
	print name2;
else: 
	print name2;
	print name1;
	

MIN_SALARY = 30000.0;
MIN_YEARS = 2;	

def main():
	salary = float(input('Enter your annual salary: '));
	years_on_job = int(input('Enter the number of years employed: '));
	
	if salary >= MIN_SALARY:
		if years_on_job >= MIN_YEARS:
			print('You qualify for the loan.');
			
		else:
			print('You must have been employed', \
					'for at least', MIN_YEARS, \
					'years to qualify. ');
	else:
		print('You must earn at least $', \
				format(MIN_SALARY, ',.2f'), \
				' per year to qualify.');

main();

#1. 

def main():
	x = input('Enter a number: ');
	if x > 100:
		y = 20;
		z = 40;
		
		print 'Y:', y;
		print 'Z:', z;
	else:
		print 'X:', x;
		print 'X is less than a hundred';

main();

#2.
def main():
	amount1 = input('Enter an amount: ');
	amount2 = input('Enter an amount: ');
	if amount1 > 10 and amount2 < 100:
		print amount1;
		print amount2;
	else:
		print 'Do nothing!';

main();

#3.
def main():
	speed = input('Enter the speed: ');
	if speed > 24 and speed< 56:
		print 'Speed is normal: ', speed;
	else:
		print 'Speed is abnormal: ', speed;

main();

#4.

def main():
	x = input('Enter a number: ');
	if x == 1:
		num = 'I';
		print x,':',num;
	elif x == 2:
		num = 'II';
		print x, ':', num;
	elif x == 3:
		num = 'III';
		print x,':', num;
	elif x == 4:
		num = 'IV';
		print x,':', num;
	elif x == 5:
		num = 'V'
		print x,':', num;
	elif x == 6:
		num = 'VI';
		print x,':', num;
	elif x == 7:
		num = 'VII';
		print x, ':', num;
	elif x == 8:
		num = 'VIII';
		print x, ':', num;
	elif x == 9:
		num = 'IX';
		print x, ':', num;
	elif x == 10:
		num = 'X';
		print x, ':', num;
	else:
		print 'Not within range: ',x;
main();

#5.
def main():
	length1 = input('Enter a length: ');
	width1 = input('Enter a width: ');
	length2 = input('Enter a length: ');
	width2 = input('Enter a width: ');
	area1 = length1 * width1;
	area2 = length2 * width2;
	
	if area1 > area2:
		print area1;
		print area2;
	else:
		print area2;
		print area1;

main();

#6.
def main():
	mass = float(input('Enter mass: '));
	weight = mass * 9.8;
	if weight > 1000:
		print 'The weight is too heavy: ', weight;
	elif weight < 10:
		print 'The weight is too light: ', weight;
	else:
		print 'The weight is just right!'

main();

#7.

def main():
	month = input('Enter a month (in number form): ');
	day = input('Enter a day of the month: ');
	year = input('Enter a two digit year: ');
	product = month * day;
	if product == year:
		print 'The date is magic!';
	else:
		print 'The date is not magic!';

main();

#8.

def main():
	color1 = raw_input('Choose a color (red, blue or yellow): ');
	color2 = raw_input('Choose another color (again red, blue, or yellow): ');
	mix(color1, color2);

def mix(color1, color2):
	if (color1 != 'red' or color1 != 'blue' or color1 !=yellow) or (color2 != 'red' or color2 != 'blue' or color2 !=yellow):
		print 'These are not the primary colors in the choice!';
	else:
		if color1 == 'red' and color2 == 'blue':
			print 'The mixed color will be purple!';
		elif color1 == 'red' and color2 == 'yellow':
			print 'The mixed color will be orange!';
		elif color1 == 'blue' and color2 == 'yellow':
			print 'The mixed color will be green!';

main();

#9.

PENNY_VALUE = .01;
NICKEL_VALUE = .05;
DIME_VALUE = .10;
QUARTER_VALUE = .25;

def main():
	penny_num = input('Enter the amount of pennies you have: ');
	nickel_num = input('Enter the amount of nickels you have: ');
	dime_num = input('Enter the amount of dimes you have: ');
	quarter_num = input('Enter the amount of quarters you have: ');
	
	penny = PENNY_VALUE * penny_num;
	nickel = NICKEL_VALUE * nickel_num;
	dime = DIME_VALUE * dime_num;
	quarter = QUARTER_VALUE * quarter_num;
	
	total_value = penny + nickel + dime + quarter;
	
	if total_value >= 1.00 :
		print 'You win the game!';
	else:
		print 'The amount is not 1.00. The amount you have is: ', total_value;

main();

#10.

def main():
	purchases = input('Enter the amount of books you purchased: ');
	if purchases == 0:
		print 'You earned 0 points';
	elif purchases == 1:
		print 'You earned 5 points';
	elif purchases == 2:
		print 'You earned 15 points';
	elif purchases == 3:
		print 'You earned 30 points';
	elif purchases >= 4:
		print 'You earned 60 points';
main();

#11.
def main():
	quantity = input('Enter the amount of packages you bought: ');
	if quantity >=10 and quantity <= 19:
		discount = .20;
		total_price = (quantity*99)*discount;
		print 'The total price is: ', total_price;
	elif quantity >=20 and quantity <= 49:
		discount = .30;
		total_price = (quantity*99)*discount;
	elif quantity >=50 and quantity <=99:
		discount = .40;
		total_price = (quantity * 99)*discount;
	elif quantity > 100:
		discount = .50;
		total_price = (quantity * 99) *.50;
		print 'The total price is: ', total_price;
	else:
		total_price = quantity * 99;
		print 'The total price is: ', total_price;

main();

#12.

def main():
	weight = input('Enter the amount of weight in pounds: ');
	if weight <= 2:
		rpp = 1.10;
		price = weight * rpp;
		print 'Price: ', price;
	elif weight > 2 and weight < 6:
		rpp = 2.20;
		price = weight * rpp;
		print 'Price: ', price;
	elif weight > 6 and weight < 10:
		rpp = 3.70;
		price = weight * rpp;
		print 'Price: ', price;
	elif weight > 10:
		rpp = 3.80;
		price = weight * rpp;
		print 'Price: ', price;

main();

#13.

def main():
	weight = input('Enter weight: ');
	height = input('Enter height: ');
	BMI = (weight * 703)/(height**2);
	if BMI >= 18.5 	and BMI < 25:
		print 'BMI is optimal';
	elif BMI < 18.5:
		print 'BMI is underweight';
	else:
		print 'Overweight!';

main();

#14.

def main():
	seconds = float(input('Enter an amount of time (seconds): '));
	
	if seconds < 60:
		print 'Time: ', seconds;
	elif seconds >= 60 and seconds < 3600 :
		minutes = seconds / 60 ;
		print 'Time in Minutes: ',minutes;
	elif seconds >= 3600 and seconds < 86400:
		hours = seconds / 3600;
		print 'Time in Hours: ', hours;
	elif seconds >= 86400:
		days = seconds / 86400;
		print 'Time in days: ', days;

main();

keep_going = 'y';

while keep_going == 'y':
	sales = float(input('Enter the amount of sales: '));
	comm_rate = float(input('Enter the commission rate: '));
		
	commission = sales * comm_rate;
		
	print 'The commission rate is $',commission;
		
	keep_going = raw_input('Do you want to calculate anohter commission (Enter y for yes): ');

MAX_TEMP = 102.5;

def main():
	temperature = float(input("Enter the substance's Celsius temperature: "));
	
	while temperature > MAX_TEMP:
		print 'The temperature is too high.';
		print 'Turn the thermostat down and wait';
		print '5 minutes. Take the temperature';
		print 'again and enter it.';
		temperature = float(input('Enter the new Celsius temperature: '));
	
	print 'The temperature is acceptable. ';
	print 'Check it again in 15 minutes.';
	
main(); 

def main():
	keep_going = 'y';
	
	while keep_going == 'y':
		show_commission();
		
		keep_going = raw_input('Do you want to calculate another commission (Enter y for yes): ');
		
def show_commission():
	
	sales = float(input('Enter the amount of sales: '));
	comm_rate = float(input('Enter the commission rate: '));
	
	commission = sales * comm_rate;
	
	print 'The commission is ', commission;
	
main();


def main():
	print 'I will display the numbers 1 through 5';
	for num in [1,2,3,4,5]:
		print(num);
main();


def main():
	for name in ['Winker', 'Blinken', 'Nod']:
		print name;
main();

def main():
	for x in range(5):
		print 'Hello World!';

main();

def main():
	for num in range (1,5):
		print num;

main();


def main():
	for num in range(1,10,2):
		print num;
		
main();

def main():
	print 'Number\tSquare';
	print '----------------'
	
	for num in range(1,11):
		square = num**2;
		print num, '\t', square;
main();

def main():
	print 'KPH\tMPH';
	print '------------';
	for kph in range(60, 131, 10):
		mph = kph * 0.6214;
		
		print kph, '\t',mph;
main();
 

def main():
	print 'This program displays a list of numbers';
	print '(starting at 1) and their squares. ';
	end = input('How high should I go? ');
	
	print 'Number\tSquare';
	print '-----------------';
	for num in range(1, end + 1):
		square = num**2;
		print num, '\t', square;

main();

def main():
	print 'This program displays a list of numbers';
	print 'and their squares.';
	start = input('Enter the starting number: ');
	end = input('How high should I go?');
	
	print 'Number\tSquare';
	print '-------------------';
	
	for num in range(start, end + 1):
		square= num**2;
		print num, '\t', square;

main();

MAX = 5;
def main():
	total = 0.0;
	
	print 'This program calculates the sum of ';
	print '5 numbers you will enter. ';
	for counter in range(MAX):
		number = int(input('Enter a number: '));
		total+=number;
	
	print 'The total is', total;

main();


TAX_FACTOR =0.0065;

def main():
	print 'Enter the property lot number';
	print 'or enter 0 to end.';
	lot = int(input('Lot number: '));
	
	while lot !=0:
		show_tax();
		
		print 'Enter the property lot number';
		print 'or enter 0 to end.';
		lot = int(input('Lot number: '));
		
def show_tax():
	value = float(input('Enter the property value: '));
	tax = value * TAX_FACTOR;
	
	print 'Property tax: $',tax;
	
main();

def main():
	hours = int(input('Enter the hours worked this week: '));
	
	pay_rate = float(input('Enter the hourly pay rate: '));
	
	gross_pay = hours * pay_rate;
	
	print 'Gross Pay: $', gross_pay;

main();

MARK_UP = 2.5;

def main():
	another = 'y';
	
	while another == 'y' or another == 'Y':
		show_retail();
		
		another = raw_input('Do you have another item? (Enter y for yes):');
		
def show_retail():
	wholesale = float(input("Enter the item's wholesale cost: "));
	retail = wholesale * MARK_UP;
	
	print ' Retail price: $',retail;
	
main();

MARK_UP = 2.5;

def main():
	another = 'y';
	while another == 'y' or another == 'Y':
		show_retail();
		
		another = raw_input('Do you have another item? (Enter y for yes):');
		
def show_retail():
	wholesale = float(input("Enter the item's wholesale cost: "));
	
	while wholesale < 0:
		print 'Error: the cost cannot be negative.';
		wholesale = float(input('Enter the correct wholesale cost: '));
	
	retail = wholesale * MARK_UP;
	print 'Retail price: $',retail;
	
main();


num_students = int(input('How many students do you have? '));
num_test_scores = int(input('How many test scores per student? '));

for student in range(num_students):
	total = 0.0;
	
	print 'Student Number', student +1;
	print '-----------------------';
	
	for test_num in range(num_test_scores):
		print 'Test number', test_num + 1;
		score = float(input(':'));
		total+=score;
		
	average = total / num_test_scores;
	
	print 'The average for student number', student + 1, 'is:', average;
	print'';

for row in range(8):
	for col in range(6):
		print '*', ;
	print '';	

for col in range(6):
	print'*',;


for row in range(8):
	for col in range(6):
		print '*',;
	print '';
"""
print "Hello World";
	