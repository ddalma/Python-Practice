"""
def main():
	outfile = open("practice.txt", 'w');
	
	outfile.write('John Locke\n');
	outfile.write('David Hume\n');
	outfile.write('Edmund Burke\n');
	
	outfile.close();


main();


#reading a file:
def main():
	#open a file named practice.txt
	infile = open('practice.txt','r');
	
	#read the file's contents
	file_contents = infile.read();
	
	#close the file
	infile.close();
	
	#print the data that was read into
	print file_contents;

main();


#reading a file line by line
def main():
	infile = open('practice.txt', 'r');
	
	line1 = infile.readline();
	line2 = infile.readline();
	line3 = infile.readline();
	
	infile.close();
	
	print line1;
	print line2;
	print line3;

main();


def main():

	print "Enter the names of three friends.";
	
	name1 = raw_input("Friend #1:");
	name2 = raw_input("Friend #2:");
	name3 = raw_input("Friend #3:");
	
	myfile = open('practice.txt', 'w');
	
	myfile.write(name1 + '\n');
	myfile.write(name2 + '\n');
	myfile.write(name3 + '\n');
	
	myfile.close();
	print "The names were written to practice.txt";

main();


def main():
	infile = open("practice.txt", 'r');
	
	line1 = infile.readline();
	line2 = infile.readline();
	line3 = infile.readline();
	
	line1 = line1.rstrip('\n');
	line2 = line2.rstrip('\n');
	line3 = line3.rstrip('\n');
	
	infile.close();
	
	print line1;
	print line2;
	print line3;

main();



#appending data to file:

def main():
	outfile = open('practice.txt', 'a');
	outfile.write("Matt\n");
	outfile.write("Chris\n");
	outfile.write("Suze\n");
	outfile.close();
	

#Programming Exercises:

#1.

def main():
	openfile = open('numbers.txt','w');
	for num in range(1,101):
		openfile.write(str(num)+'\n');
	
	print "Numbers added in numbers.txt";
	openfile.close();
	
	num_file = open('numbers.txt', 'r');
	line = num_file.readline();
	
	while line != '':
		amount =float(line);
		
		print amount;
		
		line = num_file.readline();
	
	num_file.close();
	
main();


#2.

def main():
	file = raw_input("Enter a name of a file you want to read:");
	num_file = open(file,'r');
	total = 0.0;
	while total != 5.0:
		line = num_file.readline();
		amount = float(line);
		print amount;
		total += 1;
	num_file.close();

main();


#3.
def main():
	file = raw_input("Enter a name of a file you want to read:");
	num_file = open(file,'r');
	for line in num_file:
		amount = float(line);
		print line,":",amount;
	num_file.close();

main();


#3. redo

def main():
	file = raw_input("Enter a name of a file you want to read:");
	num_file = open(file, 'r');
	count = 0.0;
	
	print "Here are the contents of",file;
	
	for line in num_file:
		num_value = float(line);
		count += 1;
		
		print count,':', num_value;
	
	num_file.close();

main();

#4.

def main():
	
	num_name = int(input("How many names do you want in the file:"));
	write_file = open('names.txt','w');
	for count in range(1,num_name +1):
		name = raw_input("Enter name:");
		write_file.write(name + '\n');
	
	write_file.close();
	print "Names were added to names.txt";
	
	open_file = open('names.txt','r');
	
	total = 0.0;
	
	for line in open_file:
		print "Name:", line;
		total += 1;
	
	print "Total names:",total;
	
	open_file.close();
	
main();


#5.

def main():
	num_file = open('numbers.txt', 'r');
	
	total = 0.0;
	
	count = 0.0;
	
	print "Printing the contents of numbers.txt";
	
	for line in num_file:
		num_value = float(line);
		
		count += 1;
		
		print count,':', num_value;
		
		total += num_value;
	
	num_file.close();
	
	print "The total is:",total;

main();

#6.
def main():
	num_file = open('numbers.txt', 'r');
	
	total = 0.0;
	
	count = 0.0;
	
	print "Printing the contents of numbers.txt";
	
	for line in num_file:
		num_value = float(line);
		
		count += 1;
		
		print count,':', num_value;
		
		total += num_value;
	
	num_file.close();
	average = total / count ;
	
	print "The total is:",total;
	print "The total average is:", average;

main();


#7.
import random

def main():
	num = input("How many numbers do you want to put in the file:");
	file = open('numbers.txt','w');
	for number in range(1,num +1):
		rand = random.randint(1,100);
		file.write(str(rand)+'\n');
	print "Random numbers were added to numbers.txt";
	
	file.close();

main();


#8.
import random

def main():
	num_file = open('numbers.txt','r');
	
	total = 0.0;
	count = 0.0;
	
	print "Printing the contents of numbers.txt";
	
	for line in num_file:
		num_value = float(line);
		
		count += 1;
		
		print count,":",num_value;
		total += num_value;
		
	
	print "Total:", total;
	num_file.close();
	
main();


#9. Exceptions dont work

"""

#10.

def main():
	num = input("How many people do you want in the file:");
	
	golf_file = open('golf.txt', 'w');
	
	for num in range(1, num +1):
		player_name = raw_input("Enter players name:");
		golf_score = input("Enter golf score:");
		
		golf_file.write(player_name + '\n');
		golf_file.write(str(golf_score) + '\n');
		
		print '';
	
	golf_file.close();
	print "Golf player records written to golf_file.txt";

	
	emp_file = open('golf.txt','r');
	
	name = emp_file.readline();
	
	while name != '':
		g_score = emp_file.readline();
		
		name = name.rstrip('\n');
		g_score = g_score.rstrip('\n');
		
		print "Name:", name;
		print "Golf Score:", g_score;
		
		name = emp_file.readline();
	
	emp_file.close();

main();
		


main(); 

	




	