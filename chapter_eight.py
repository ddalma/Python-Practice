"""
#Algorithm Workbench

#5.
def main():
	num = get_list();
	
	print "List:", num;
	
	total(num);

def get_list():
	value = [];
	again = 'y';
	
	while again == 'y' or again == 'Y':
		num = input("Enter a number:");
		value.append(num);
		again = raw_input("Again?(y for yes anything else is no):");
	
	return value;

def total(value):
	total = 0;
	for num in value:
		total += num;
	
	print "Total:",total;

main();


#6.

def main():
	names = ['Daryl', 'James', 'Luiz','Lola','Jason'];
	search = raw_input("Enter a name your searching:");
	
	if search in names:
		print "Hello",search;
	else:
		print "No",search;

main();


#7.

list1 = [40,50,60];
list2 = [10,20,30];
list3 = list1 + list2;
print list3;


#8.

ROWS = 5;
COLS = 3;	

def main():
	values = [[0,0,0],
			  [0,0,0],
			  [0,0,0],
			  [0,0,0],
			  [0,0,0]];
	
	for r in range(ROWS):
		for c in range(COLS):
			values[r][c] = input("Enter a number:");
	
	print values;

main();

#Programming Exercises:

#1.

def main():
	total = 0;
	for day in range(1,8):
		value = input("Value of the day:");
		total += value;
	
	print "Values:", value;
	print "Total:", total;

main();


#2.
import random

def main():
	list = [];
	for num in range(7):
		value = random.randint(0,9);
		list.append(value);
	
	print "List:", list;
	
	print "The lottery numbers are:";
	for val in range(len(list)):
		print "#",val+1,":",list[val];
	
main();

#3.

def main():
	rain_list = [];
	for num in range(12):
		print "Enter the rainfall of month",num +1,":";
		num = float(input());
		rain_list.append(num);
	
	total = 0.0;
	for value in rain_list:
		total += value;
	
	print "Total rainfall for year:",total;
	
	average = total / len(rain_list);
	
	print "Average monthly rainfall:",average;
	
	min_val = min(rain_list);
	max_val = max(rain_list);
	
	print "The smallest rainfall:",min_val;
	print "The largest rainfall:",max_val;


main();

#4.

def main():
	num_list = [];
	for num in range(20):
		value = input("Enter a number:");
		num_list.append(value);
	
	min_value = min(num_list);
	max_value = max(num_list);
	
	total = 0.0;
	for val in num_list:
		total+= val;
	
	average = total /len(num_list);
	
	print "The lowest number in the list:",min_value;
	print "The highest number in the list:",max_value;
	print "Total:",total;
	print "Average:",average;

main();

#5.
import random

def main():
	num_list = [];
	for num in range(7):
		val = random.randint(0,9);
		num_list.append(val);
	
	outfile = open('charge_accounts.txt','w');
	
	for item in num_list:
		outfile.write(str(item) + '\n');
	
	outfile.close();
	
	print "Numbers added to charge_accounts.txt";
	
	infile = open('charge_accounts.txt','r');
	
	numbers = infile.readlines();
	
	infile.close();
	
	index = 0;
	while index < len(numbers):
		numbers[index] = int(numbers[index]);
		index += 1;
	
	print numbers;
	
	search = input("Enter a number:");
	if search in num_list:
		print search,"is in num_list";
	else:
		print search,"is not in num_list";

main();

#6.
def main():
	grade_list =['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A'];
	
	outfile = open('test_answer.txt','w');
	
	for item in grade_list:
		outfile.write(item + '\n');
	
	outfile.close();	
	print "Grades submitted to test_answer.txt";
	
	
	student_choice =[];
	infile = open('student_ans.txt','w');
	for item in range(20):
		grade = raw_input("Enter answer:");
		infile.write(grade + '\n');
	
	infile.close();
	print "Student grades added to student_ans.txt";
	
	file = open('test_answer.txt','r');
	file2 = open('student_ans.txt','r');
	
	solutions = file.readlines();
	choice = file2.readlines();
	
	file.close();
	file2.close();
	
	index = 0;
	total = 0;
	while index < len(solutions):
		solutions[index] = solutions[index].rstrip('\n');
		choice[index] = choice[index].rstrip('\n');
		index += 1;
		
		if solutions[index] == choice[index]:
			total +=1;
	
	print "Total correct:",total;
	if total < 15:
		print "You failed the exam!";
	else:
		print "You passed!";
	
main();

"""
#7.

