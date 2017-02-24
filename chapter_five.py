"""
def main():
	keep_going = 'y';
	
	while keep_going == 'y':
		sales = float(input("Enter the amount of sales:"));
		comm_rate = float(input("Enter the commission rate:"));
		
		
		commission = sales * comm_rate;
		
		print "The commission is $",commission;
		
		keep_going = raw_input("Do you want to calculate another commission(Enter y for yes):");
		

main();



MAX_TEMP = 102.5;


def main():
	temperature = float(input("Enter the substance's Celsius temperature:"));
	
	while temperature > MAX_TEMP:
		print "The temperature is too high.";
		print "Turn the thermostat down and wait";
		print "5 minutes. Then take the temperature";
		print "again and enter it.";
		
		temperature = float(input("Enter the new Celsius temperature:"));
		
	
	print "The temperature is acceptable.";
	print "Check it again in 15 minutes.";


main();

def main():
	print "I will display the numbers 1 through 5.";
	for num in [1,2,3,4,5]:
		print(num);

main();


def main():
	for x in range(5):
		print "Hello World!";
	
	for num in range(10):
		print num;

main();

def main():
	print "Number\tSquare";
	print "----------------"
	for number in range(1,11):
		square = number ** 2;
		print number,"\t",square;

main();

START = 60;
END = 131;
INCREMENT = 10;
CONVERSION_FACTOR = 0.6214;

def main():
	print "KPH\tMPH";
	print "-------------";
	
	for kph in range(START, END, INCREMENT):
		mph = kph * CONVERSION_FACTOR;
		print kph,'\t', mph;

main();

def main():
	print "This program displays a list of number";
	print "(Starting at 1) and their squares.";
	end = int(input("How high should I go?"));
	
	print "";
	print "Number\tSquare";
	print "------------------";
	
	for number in range(1, end + 1):
		square = number ** 2;
		print number, "\t", square;

main();

def main():
	start = int(input("Enter the start:"));
	end = int(input("How high should I go?"));
	
	print "";
	print "Number\tSquare";
	print "-------------------";
	
	for number in range(start, end + 1):
		square = number ** 2;
		print number, "\t", square;

main();


MAX = 5;

def main():
	total = 0.0;
	
	print "This program calculates the sum of"
	print MAX,"numbers you will enter";
	
	for counter in range(MAX):
		number = int(input("Enter a number:"));
		total += number;
	
	print "The total is", total;

main();


TAX_FACTOR = 0.0065;

def main():
	print "Enter the property lot number";
	print "or enter 0 to end.";
	lot = int(input("Lot number:"));
	
	while lot != 0:
		show_tax();
		
		print "Enter the next lot number or";
		print "enter 0 to end.";
		lot = int(input("Lot number: "));

def show_tax():
	value = float(input("Enter the property value:"));
	
	tax = value * TAX_FACTOR;
	
	print "Property tax: $", tax;
	
main();


def main():
	hours = int(input("Enter the hours worked this week:"));
	
	pay_rate = float(input("Enter the hourly pay rate: "));
	
	gross_pay = hours * pay_rate;
	
	print "Gross pay: ", gross_pay;

main();


def main():
	num_students = int(input("How many students do you have?"));
	
	num_test_scores = int(input("How many test scores per student?"));
	
	for student in range(num_students):
		total = 0.0
		
		print "Student number", student + 1;
		print  "----------------";
		for test_num in range(num_test_scores):
			print "Test number", test_num + 1;
			score = float(input(":"));
			total += score;
		
		average = total / num_test_scores;
		
		print "The average for student number", student +1, "is:", average;
		print "";

main();


def print_rect(row_count, col_count):
   for row in range(row_count):
      for col in range(col_count):
         print "*",
      print

row_count = int(raw_input("How many rows of asterisks?\n   "))
col_count = int(raw_input("How many columns in each row?\n   "))
print_rect(row_count, col_count)
print "Bye!"


for row in range(7):
	for col in range(6):
		print "*", 
	print
	
def main():
	rows = int(input("How many rows?"));
	columns = int(input("How many columns?"));
	
	for r in range(rows):
		for c in range(columns):
			print "*",
		print

main();


BASE_SIZE = 8;

for r in range(BASE_SIZE):
	for c in range(1 + r):
		print "*",
	print 


NUM_STEPS = 6;
for r in range(NUM_STEPS):
	for c in range(r):
		print ' ',
	print '#';
	
Algorithm Workbench

//1.
product = 0;
while product < 100 :
	number = int(input("Enter a number:"));
	product = number * 10;
	print "Product:",product;


//2.
answer = 'y';
while answer == 'y':
	num1 = int(input("Enter a number: "));
	num2 = int(input("Enter a second number: "));
	print "Number 1:", num1;
	print "Number 2:", num2;
	sum = num1 + num2;
	print "The sum:", sum;
	answer = raw_input("Do you wanna go again? (Enter y for yes or n for no)");


//3.
for num in range(0,1001,10):
	print num,
print	

//4.
total = 0.0;
for num in range(10):
	num = int(input("Enter a number: "));
	total += num;

print "Total: ",total;

//5.
total = 0.0;
for i in range(30):
	total += ((i + 1) / (30 - i));

print "Total:",total;


//7.
for row in range(10):
	for column in range(15):
		print "*",
	print

Programming Exercises:

//1.
total = 0.0;
for num in range(7):
	print "Day:",num + 1;
	bug_num = int(input("Enter number of bugs collected today:"));
	total += bug_num;

print "Total bugs collected for the week:", total;


//2.
CALORIES_PER_MIN = 3.9
for num in range(10,31,5):
	cpm = CALORIES_PER_MIN * num;
	print "Calories burned in", num,"minutes:",cpm;

//3.
answer = 'y';
total = 0.0
while answer == 'y':
	budget = float(input("Enter the budget for the day of the month: "));
	total += budget;
	answer = raw_input("Do you want to enter another budget?(y for yes or n for no):");

print "Total:",total;


//4.
def main():
	speed = int(input("What is the speed of the vehicle in mph?"));
	time = int(input("How many hours has it traveled?"));
	print "Hour\tDistance Traveled";
	print "--------------------------";
	for num in range(time):
		distance = speed * (num+1);
		print num+1,"\t",distance;

main();

//5.
num_of_rain = int(input("Enter the number of days rainfall per month:"));
for month in range(12):
	total = 0.0;
	
	print "Month ", month + 1;
	print "--------------------";
	for rainfall in range(num_of_rain):
		print 'Day', rainfall + 1;
		rain_num = float(input(':'));
		total += rain_num;
	
	average = total / num_of_rain;
	
	print "The average rainfall of month",month + 1,"is:", average;



//6.
def main():
	print "Celsius\tFarenheit";
	print "---------------------";
	for c in range(1,21):
		farenheit = float(((9/5) * c) + 32);
		print c,"\t",farenheit;

main();	

//7. Did it on legal pad

//8. Did it on legal pad



//9.
for r in range(7,0,-1):
	for c in range(r):
		print '*',
	print '';
	
"""

//10.
steps=6
for r in range(steps):
    print'#', 
    for c in range(r):
        print' ', 
    print'#'


	