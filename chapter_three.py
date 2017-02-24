"""
//chapter 3

def main():
	first_name = raw_input("Enter your firstname:");
	last_name = raw_input("Enter your lastname:");
	print "Your name reversed is";
	reverse_name(first_name,last_name);

def reverse_name(first, last):
	print last,first;

main();


//1.
def main():
	kilometers = float(input("Enter the distance of kilometers:"));
	miles(kilometers);

def miles(distance):
	miles = distance * 0.6214;
	print miles,"miles";

main();


//2.
def main():
	original_price = float(input("Enter the price:"));
	tax(original_price);

def tax(price):
	county_tax = price * .02;
	print "county tax", county_tax;
	states_tax = price * .04;
	print "states tax",states_tax;
	total = price + county_tax + states_tax;
	print "Total:",total;

main();

//3.
def main():
	replace_amount = float(input("Enter the amount it would cost to replace the structure:"));
	print "The replacement amount:",replace_amount;
	insurance(replace_amount);

def insurance(amount):
	min_amount_insurance = amount * .8;
	print "The minimum insurance needed:",min_amount_insurance;

main();
	

//4.
def main():
	loan_payment = float(input("Enter the loan payment:"));
	insurance = float(input("Enter the amount of insurance:"));
	gas = float(input("Enter the amount spent on gas:"));
	oil = float(input("Enter the amount spent on oil:"));
	tires = float(input("Enter the amount spent on tires:"));
	maintenance = float(input("Enter the maintenance spent:"));
	monthly_pay(loan_payment,insurance,gas, oil, tires, maintenance);
	yearly_pay(loan_payment,insurance,gas, oil, tires, maintenance);

def monthly_pay(amount1, amount2, amount3, amount4, amount5):
	amount_per_month = amount1 + amount2 + amount3 + amount4 +amount5;
	print "Monthly payment:",amount_per_month;

def yearly_pay(amount1, amount2, amount3, amount4, amount5):
	amount_per_year = (amount1 + amount2 + amount3 + amount4 +amount5) * 12;
	print "Yearly payment:",amount_per_year;

main();

//5.
def main():
	land_value = float(input("Enter the property's actual value:"));
	print "Property value",land_value;
	assessment_value = land_value * .60;
	print "Assessment value:",assessment_value;
	property_tax(assessment_value);

def property_tax(amount):
	value = amount / 100.00;
	tax = value * .64;
	print "Property tax:", tax;

main();

//6.
def main():
	weight = float(input("Enter weight:"));
	height = float(input("Enter height:"));
	BMI(weight, height);

def BMI(weight, height):
	bmi = weight * (703 / (height*height));
	print "BMI:",bmi;

main();	

//7.
def main():
	fat_grams = float(input("Enter the amount of fat grams:"));
	carb_grams = float(input("Enter the amount of carb grams:"));
	calories_from_fat(fat_grams);
	calories_from_carbs(carb_grams);

def calories_from_fat(amount):
	cff = amount * 9;
	print "Calories from fat:", cff;

def calories_from_carbs(amount):
	cfc = amount * 4;
	print "Calories from carbs:", amount * 4;

main();

//8.
def main():
	class_A = input("Enter tickets for class A:");
	class_B = input("Enter tickets for class B:");
	class_C = input("Enter tickets for class C:");
	tickets(class_A,class_B, class_C);

def tickets(amount_one, amount_two, amount_three):
	
	ticket_A_price = amount_one * 15;
	print "Class A tickets:",amount_one;

	ticket_B_price = amount_two * 12;
	print "Class B tickets:",amount_two;

	ticket_C_price = amount_three * 9;
	print "Class C tickets:",amount_three;
	
	total_amount = ticket_A_price + ticket_B_price + ticket_C_price;
	
	print "Total price of tickets:$",total_amount;

main();
"

//9.
def main():
	square_feet = float(input("Enter the square feet of wall space to be painted:"));
	price_ppg = float(input("Enter the price of the paint per gallon:"));
	num_of_gallons(square_feet, price_ppg);
	hours_of_labor(square_feet);
	

def num_of_gallons(amount, amount_two):
	wall_space = amount / 115;
	gallons_of_paint = 1 * wall_space;
	price = gallons_of_paint * amount_two
	print "gallons of paint required:",gallons_of_paint;
	print "Total cost of the paint job:$",price;
	
def hours_of_labor(amount):
	labor_amount = amount / 115;
	labor_required = labor_amount * 8;
	charges = 20.00 * labor_required;
	print "Hours required:", labor_required;
	print "Company charges:$", charges;

main();

//10.
def main():
	total_sales = float(input("Enter the total sales for the month:"));
	county_sales_tax(total_sales);
	states_sales_tax(total_sales);
	total_sales_tax = total_sales*.04 + total_sales*.02;
	print "Total sales tax:$", total_sales_tax;

def county_sales_tax(amount):
	cst = amount * .02;
	print "County sales tax:$", cst;

def states_sales_tax(amount):
	sst = amount * .04;
	print "State sales tax:$", sst;

main();

"""