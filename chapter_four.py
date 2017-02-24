"""
HIGH_SCORE = 95;

def main():
	test1 = int(input("Enter the score of the first test:"));
	test2 = int(input("Enter the score of the second test:"));
	test3 = int(input("Enter the score of the third test:"));
	average = (test1 + test2 + test3) / 3.0;
	
	if average >= HIGH_SCORE:
		print "Congrats!";
		print "That's a highscore!";

main();


BASE_HOURS = 40;
OT_MULTIPLIER = 1.5;

def main():
	hours_worked = float(input("Enter the amount of hours worked:"));
	pay_rate = float(input("Enter the hourly pay rate:"));
	
	if hours_worked > BASE_HOURS:
		calc_pay_with_OT(hours_worked, pay_rate);
	else:
		calc_regular_pay(hours_worked,pay_rate);
	
def calc_pay_with_OT(hours, rate):
		overtime_hours = hours - BASE_HOURS;
		
		overtime_pay = overtime_hours * rate * OT_MULTIPLIER;
		
		gross_pay = BASE_HOURS * rate + overtime_pay;
		
		print "The gross pay is $",gross_pay;
	

def calc_regular_pay(hours, rate):
	gross_pay = hours * rate;
	
	print "The gross pay is $", gross_pay;

main();

password = raw_input("Enter the password:");
if password == 'prospero':
	print 'password accepted!';
else:
	print "Sorry, incorrect password!";

Programming Exercises: 

//1.
def main():
	num = input("Enter a number between 1 through 10:");
	if num <= 0 or num > 10:
		print "Number out of range!";
	if num == 1:
		roman_num = 'I';
		print "Number\tRoman Numeral\n", 
		print num,"\t", roman_num;
	elif num ==2:
		roman_num = 'II';
		print "Number\tRoman Numeral\n", 
		print num,"\t",roman_num
	elif num ==3:
		print "Number\tRoman Numeral\n",
		roman_num = 'III';
		print num,"\t",roman_num
	elif num ==4:
		print "Number\tRoman Numeral\n", 
		roman_num = 'IV';
		print num,"\t",roman_num
	elif num ==5:
		print "Number\tRoman Numeral\n", 
		roman_num = 'V';
		print num,"\t",roman_num
	elif num ==6:
		print "Number\tRoman Numeral\n", 
		roman_num = 'VI';
		print num,"\t",roman_num
	elif num ==7:
		print "Number\tRoman Numeral\n", 
		roman_num = 'VII';
		print num,"\t",roman_num
	elif num ==8:
		print "Number\tRoman Numeral\n", 
		roman_num = 'VIII';
		print num,"\t",roman_num
	elif num ==9:
		print "Number\tRoman Numeral\n", 
		roman_num = 'IX';
		print num,"\t",roman_num
	elif num ==10:
		print "Number\tRoman Numeral\n", 
		roman_num = 'X';
		print num,"\t",roman_num

main();

//2.
def main():
	length_rec_one = int(input("Enter length of first rectangle:"));
	width_rec_one = int(input("Enter the width of first rectangle:"));
	
	length_rec_two = int(input("Enter the length of second rectangle:"));
	width_rec_two = int(input("Enter the width of second rectangle:"));
	
	area_one = length_rec_one * width_rec_one;
	area_two = length_rec_two * width_rec_two;
	
	if area_one > area_two:
		print "The first rectangle is larger:",area_one;
	else:
		print "The second rectangle is larger:",area_two;

main();


//3.
def main():
	mass = float(input("Enter the object's mass:"));
	weight = mass * 9.8;
	if weight > 1000:
		print "The object is too heavy!";
	elif weight < 10:
		print "The object is too light!";
	else:
		print "The object weighs just right!";
		
main();


//4.
def main():
	month = int(input("Enter the month in numerical form:"));
	day = int(input("Enter the day of the month:"));
	year = int(input("Enter a two digit year:"));
	if (month * day) == year:
		print "That is a magic date!";
	else:
		print "The date is:", month,"\\",day,"\\",year;

main();


//5.
def main():
	color_one = raw_input("Choose a primary color:");
	color_two = raw_input("Choose another primary color:");
	if color_one != "red" or color_one != "blue" or color_one != "yellow":
		print "That is not a primary color!";
	if color_two != "red" or color_two != "blue" or color_two != "yellow":
		print "That is not a primary color!";
	
	if color_one == 'red' and color_two == 'blue':
		print "When you mix",color_one,"and",color_two,",you get purple";
	elif color_one == 'red' and color_two == 'yellow':
		print "When you mix",color_one,"and",color_two,",you get orange";
	elif color_one == 'blue' and color_two == 'yellow':
		print "When you mix",color_one,"and",color_two,",you get green";

main();

//6.
def main():
	pennies_num = input("Enter number of pennies:");
	nickels_num = input("Enter number of nickels:");
	dimes_num = input("Enter number of dimes:");
	quarters_num = input("Enter number of quarter:");
	amount_of_pennies = pennies_num * .01;
	amount_of_nickels = nickels_num * .05;
	amount_of_dimes = dimes_num * .10;
	amount_of_quarters = quarters_num * .25;
	total = amount_of_pennies + amount_of_nickels + amount_of_dimes + amount_of_quarters;
	if total == 1.00:
		print "You won the game!";
		print "Total:", total;
	elif total > 1.00:
		print "The total is greater than $1.00";
		print "Total:", total;

	elif total < 1.00:
		print "The total is lower than $1.00";
		print "Total:", total;

main();


//7.
def main():
	num_of_books = input("Enter the number of books purchased:");
	if num_of_books == 0:
		points = 0;
		print "Number of points earned:",points;
	elif num_of_books == 1:
		points = 5;
		print "Number of points earned:", points;
	elif num_of_books == 2:
		points = 15;
		print "Number of points earned:", points;
	elif num_of_books == 3:
		points = 30;
		print "Number of points earned:", points;
	elif num_of_books >= 4:
		points = 60;
		print "Number of points earned:", points;

main();

//8.
def main():
	retail_price = 90;
	quantity = input("Enter number of packages:");
	if quantity >= 10 and quantity < 20:
		discount = .20;
		total = quantity * retail_price * (1 - discount);
		print "Discount: %",discount *100;
		print "Total: ",total;
	elif quantity >= 20 and quantity < 49:
		discount = .30;
		total = quantity * retail_price * (1 - discount);
		print "Discount: %",discount *100;
		print "Total: ",total;
	elif quantity >= 50 and quantity < 99:
		discount = .40;
		total = quantity * retail_price * (1 - discount);
		print "Discount: %",discount *100;
		print "Total: ",total;
	elif quantity >= 100:
		discount = .50;
		total = quantity * retail_price * (1 - discount);
		print "Discount: %",discount *100;
		print "Total: ",total;
	else:
		print "No discount for you!";
		total = quantity * retail_price;
		
main();

//9.
def main():
	weight_of_package = input("Enter weight of package:");
	if weight_of_package <= 2:
		rpp = 1.10;
		total = weight_of_package * rpp;
		print "Total:",total;
	elif weight_of_package >2 and weight_of_package < 6:
		rpp = 2.20;
		total = weight_of_package * rpp;
		print "Total:",total;
	elif weight_of_package >6 and weight_of_package < 10:
		rpp = 3.70;
		total = weight_of_package * rpp;
		print "Total:",total;
	elif weight_of_package >10:
		rpp = 3.80;
		total = weight_of_package * rpp;
		print "Total:",total;

main();


//10.
def main():
	weight = float(input("Enter weight:"));
	height = float(input("Enter height:"));
	BMI(weight, height);

def BMI(weight, height):
	bmi = weight * (703 / (height * height));
	if bmi >= 18.5 and bmi <= 25:
		print "Your weight is optimal!";
	elif bmi >= 25:
		print "Your overweight!";
	elif bmi < 18.5:
		print "Your underweight!";

main();

//10.

def main():
	seconds = float(input("Enter the amount of seconds:"));
	if seconds < 60:
		print seconds,"seconds";
	elif seconds >= 60 and seconds < 3600:
		minutes = seconds / 60;
		print minutes,"minutes";
	elif seconds >= 3600 and seconds < 86400:
		hours = seconds / 3600;
		print hours,"hours";
	elif seconds >= 86400:
		days = seconds / 86400;
		print days,"days";

main();
"""
	