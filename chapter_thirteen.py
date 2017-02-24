"""
def main():
	message(5);

def message(times):
	if times > 0:
		print "This is a recursive function.";
		message(times - 1);

main();


#factorial
def main():
	num = int(input("Enter a number:"));
	value = factorial(num);
	print value;

def factorial(number):
	if number == 0:
		return 1;
	else:
		return number * factorial(number - 1);

main();


def range_sum(my_list, start, end):
	if start > end:
		return 0;
	else:
		return num_list[start] + range_sum(num_list, start + 1, end);

numbers = [1,2,3,4,5,6,7,8,9];
my_sum = range_sum(numbers, 3, 7);


print my_sum;

def main():
	number = int(input("Enter a nonnegative integer:"));
	
	fact = factorial(number);
	
	print "The factorial of", number, 'is', fact;

def factorial(num):
	if num == 0:
		return 1;
	else:
		return num * factorial(num - 1);

main();


#A problem can be solved with recursion if it can be
broken down into smaller problems that are identical in
struture to the overall problem.
def main():
	numbers =

def main():
	num = int(input("Enter a number:"));
	value = factorial(num);
	print num,"!: ",value;

def factorial(num):
	if num == 0:
		return 1;
	else:
		return num* factorial(num - 1);

main();



#Summing a range of List Elements with Recursion

def main():
	numbers = [1,2,3,4,5,6,7,8,9];
	
	my_sum = range_sum(numbers, 2,5);
	
	print "The sum of items 2 through 5 is", my_sum;

def range_sum(num_list, start, end):
	if start > end:
		return 0;
	else:
		return num_list[start] + range_sum(num_list, start + 1, end);

main();


#This program uses recursion to print numbers
#from the Fibonacci series

def main():
	print "The first 10 numbers in the";
	print "Fibonacci series are:";
	
	for number in range(1,11):
		print (fib(number));

def fib(n):
	if n == 0:
		return 0;
	elif n == 1:
		return 1;
	else:
		return fib(n-1) + fib(n-2);

main();

def main():
	num1 = int(input("Enter an integer:"));
	num2 = int(input("Enter another integer:"));
	
	print "The greatest common divisor of";
	print "the two number is", gcd(num1, num2);

def gcd(x,y):
	if x % y == 0:
		return y;
	else:
		return gcd(x, x % y);

main();


def main():
	num1 = int(input("Enter an integer:"));
	num2 = int(input("Enter another integer:"));
	
	print "The greatest common divisor of";
	print "The two numbers is", gcd(num1, num2);
	

def gcd(x,y):
	if x % y == 0:
		return y;
	else:
		return gcd(x, x % y);

main();


def main():
	num_discs = 3;
	from_peg = 1;
	to_peg = 3;
	temp_peg = 2;
	
	move_discs(num_discs, from_peg, to_peg, temp_peg);
	print "All the pegs are moved!";
	

#The moveDiscs function display a disc move in
#the towers of hanoi game
#the parameters are:
# num: the number of discs to move.
# from_peg: the peg to move from
#to_peg: the peg to move on
#temp_peg: the temporary peg.

def move_discs(num, from_peg, to_peg, temp_peg):
	if num > 0:
		move_discs(num - 1, from_peg, temp_peg, to_peg);
		print "Move a disc from peg", from_peg,"to peg", to_peg;
		move_discs(num - 1, temp_peg, to_peg, from_peg);

main();


def main():
	num = 0;
	show_me(num);
def show_me(arg):
	if arg < 10:
		show_me(arg + 1);
	else:
		print arg;

main();


#Programming Exercises:

#1.
def main():
	num = int(input("Enter a number:"));
	countup(num);
	
def countup(n):
	if n != 0:
		countup(n-1);
		print n;

main();

"""

#2.

def main():
	x = int(input("Enter a number:"));
	y = int(input("Enter another number:"));
	result = mult(x,y);
	print "Result:", result;
def mult(a,b):
	if a == 0:
		return 0;
	elif a == 1:
		return b;
	else:
		return b + mult(a - 1, + b);

main();