"""
import random

def main():
	number = random.randint(1,10)
	
	print "The number is",number;

main();

import random

def main():
	for count in range(5):
		number = random.randint(1,100);
		print number;

main();


import random

MIN = 1;
MAX = 6;

def main():

	again = 'y';
	
	while again == 'y' or again == 'Y':
		print "Rolling the dice...";
		print "Their values are:";
		print random.randint(MIN,MAX);
		print random.randint(MIN,MAX);
		
		again = raw_input("Roll them again? (y =yes):");

main();


import random

HEADS = 1;
TAILS = 2;
TOSSES = 10;

def main():
	for toss in range(TOSSES):
		if random.randint(HEADS,TAILS) == HEADS:
			print "Heads";
		else:
			print "Tails";

main();


def main():
	num1 = input("Enter a number:");
	num2 = input("Enter another number:");
	
	num3 = sum(num1,num2);
	print "Number 1:", num1;
	print "Number 2:", num2;
	print "Sum:", num3;	

def sum(a,b):
	
	value = a + b;
	
	return value;

main();

def main():
	first_age = int(input("Enter your age:"));
	
	second_age = int(input("Enter your best friend's age:"));
	
	total = sum(first_age, second_age);
	
	print "Together you are",total,"years old.";
	

def sum(num1, num2):
	result = num1 + num2;
	return result;

main();


DISCOUNT_PERCENTAGE = 0.20;

def main():
	reg_price = get_regular_price();
	
	sale_price = reg_price - discount(reg_price);
	
	print "The sale price is $", sale_price;
	
def get_regular_price():
	price = float(input("Enter the item's regular price:"));
	return price;

def discount(price):
	return price * DISCOUNT_PERCENTAGE;

main();

//11.
import random

def main():

	rand = random.randint(1,50);
	guess = 0;
	print "Random num:",rand;
	total = 0;
	while guess != rand:
		guess = input("Enter another guess:");
		if guess > rand:
			print  "The guess is too high!";
			total+=1;
		elif guess < rand:
			print "The guess is too low!";
			total+=1;
		else:
			print "Perfect guess";
			total+=1;
	
	print "Total amount of guesses:",total;

main();

//12.
import random

def main():
	answer = 'y';
	while answer == 'y' or answer == 'Y':
		rand = random.randint(1,3);
		game_choice = choice(rand);
		display_menu();
		your_pick = input("Enter your choice:");
		user_choice = choice(your_pick);
		battle(game_choice,user_choice);

def choice(num):
	if num == 1:
		return "rock";
	elif num == 2:
		return "paper";
	else:
		return "scissor";

def battle(g,y):
	if g == "rock" and y == "scissor":
		print "Rock wins";
		print "The rock smashes the scissors";
		print "Computer wins!";
	elif g == "scissor" and y == "paper":
		print "Scissors wins";
		print "Scissors cuts paper";
		print "Computer wins!";
	elif g == "paper" and y == "rock":
		print "Paper wins";
		print "Paper wraps rock!";
		print "Computer wins!";
	elif g == "scissor" and y == "rock":
		print "Rock wins";
		print "The rock smashes the scissors";
		print "You win!";
	elif g == "paper" and y == "scissor":
		print "Scissors wins";
		print "Scissors cuts paper";
		print "You win!";
	elif g == "rock" and y == "paper":
		print "Paper wins";
		print "Paper wraps rock!";
		print "You win!";

def display_menu():
	print " 1) Rock";
	print " 2) Paper";
	print " 3) Scissor";

main();

"""