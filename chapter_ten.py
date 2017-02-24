"""
#10.3 Serializing Objects

#You open a file for binary writing

#You call the pickle module;s dump method to
#pickle the object and write it to the specified file

#After you have pickled all the objects that you want
#to save to the file, you close the file.

import pickle

phonebook = {'Chris':'555-1111',
			'Katie':'555 -2222',
			'Joanne':'555-3333'};

output_file = open('phonebook.dat', 'wb');
pickle.dump(phonebook, output_file);
output_file.close();

input_file = open('phonebook.dat', 'rb');
pb = pickle.load(input_file);
print pb;

input_file.close();


import pickle

#This program demonstrates object pickling

def main():
	again = 'y';
	
	output_file = open('info.dat','wb');
	
	while again.lower() == 'y':
		save_data(output_file);
		
		again = raw_input("Enter more data? (y/n):");
		
	
	output_file.close();

def save_data(file):
	person = {};
	
	person['name'] = raw_input('Name:');
	person['age'] = raw_input('Age:');
	person['weight'] = raw_input('Weight:');
	
	pickle.dump(person,file);

main();


import pickle

#This program demonstrates object unpickling

def main():
	end_of_file = False;
	
	input_file = open('info.dat', 'rb');
	
	while not end_of_file:
		try:
		
			person = pickle.load(input_file);
			display_data(person);
		except EOFError:
			
			end_of_file = True;
		
	input_file.close();

def display_data(person):
	print "Name:",person['name'];
	print "Age:",person['age'];
	print "Weight:",person['weight'];
	print " ";

main();


#Algorithm

#1.

dict = {'a':1, 'b':2,'c':3};

#2.

dict = {};

#3 & #4.

def main():
	names = {'John':'555-1111',
		'Jason':'555-2222',
		'Joanne': '555-3333'}
	
	value = names.get('Alice', "Does not exist");
	print value;

main();


#5. 
num = set([10,20,30,40]);

#6.
set1 = set([1,2,3,4,5]);
set2 = set([3,5,6,7,8]);


#7.
set3 = set1.union(set2);
print set3;

#8.
#find whats in set 1 but not in set 2
set4 = set1.difference(set2);
print set4;

#9.
#find whats in set2 but not in set1:
set5 = set2.difference(set1);
print set5;

#10
#Finding elements each set doesnt share:

set6 = set1.symmetric_difference(set2);
print set6;


#11.

import pickle

def main():
	outputfile = open("mydata.dat", 'wb');
	
	again = 'y';
	while again.lower() == 'y':
		save_data(outputfile);
		
		again = raw_input("Go again? (y/n):");
	
	outputfile.close();
	
	end_of_file = False;
	infile = open('mydata.dat','rb');
	
	while not end_of_file:
		try:
			data = pickle.load(infile);
			display_data(data);
		except EOFError:
			end_of_file = True;
	
	infile.close();

def display_data(data):
	print "Name:",data['name'];
	print "Number:",data['number'];

	

def save_data(file):
	data = {};
	
	data['name'] = raw_input('Name:');
	data['number'] = raw_input("Number:");
	
	pickle.dump(data, file);

main();


#Programming Exercises:

#1.

def main():
	set1 = {'CS101': 3004, 'CS102':4501, 'CS103':6755,
	'NT110':1244,'CM241':1411};

	set2 = {'CS101': 'Haynes', 'CS102':'Alvarado', 'CS103':'Rich',
	'NT110':'Burke','CM241':'Lee'};
	
	set3 = {'CS101': '8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.',
	'NT110':'11:00 a.m.','CM241':'1:00 p.m.'};

	
	again = 'y';
	
	while again.lower() == 'y':
		key = raw_input("Enter a course number:");
		value1 = set1.get(key, 'Entry not found');
		value2 = set2.get(key, 'Entry not found');
		value3 = set3.get(key, 'Entry not found');
		
		print key,"Room Number:",value1;
		print key,"Instructor:",value2;
		print key,"Meeting Time:",value3;
		
		again = raw_input("Try again? (y/n):");

main();

#2.
import random

def main():
	capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
	'Arizona':'Phoenix','Arkansas':'Little Rock', 'California':'Sacramento',
	'Colorado':'Denver','Connecticut':'Hartford','Delaware':'Dover',
	'Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu',
	'Idaho':'Boise', 'Illinois':'Springfield','Indiana':'Indianapolis',
	'Iowa':'Des Moines', 'Kansas':'Topeka', 'Kentucky':'Frankfort',
	'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis',
	'Massachusetts':'Boston','Michigan':'Lansing','Minnesota':'St. Paul',
	'Mississippi':'Jackson','Missouri':'Jefferson City', 'Montana':'Helena',
	'Nebraska':'Lincoln','Neveda':'Carson City','New Hampshire':'Concord',
	'New Jersey':'Trenton','New York':'Albany','North Carolina':'Raleigh',
	'North Dakota':'Bismarck','Ohio':'Columbus','Oklahoma':'Oklahoma City',
	'Oregon':'Salem','Pennsylvania':'Harrisburg','Rhode Island':'Providence',
	'South Carolina':'Columbia','South Dakota':'Pierre','Tennessee':'Nashville',
	'Texas':'Austin','Utah':'Salt Lake City','Vermont':'Montpelier','Virginia':'Richmond',
	'Washington':'Olympia','West Virginia':'Charleston','Wisconsin':'Madison',
	'Wyoming':'Cheyenne'};
	
	again = 'y';
	total_right = 0;
	total_wrong = 0;
	
	while again.lower() == 'y':
		pick = random.choice(list(capitals.keys()));
		correct_answer = capitals.get(pick);
		print "What is the capital of",pick,"?";
		your_answer = raw_input("Your answer:");
		
		if your_answer.lower() == correct_answer.lower():
			print "Correct!";
			total_right += 1;
		else:
			print "Wrong!";
			total_wrong += 1;
		
		again = raw_input("Try again? (y/n):");
	
	print "Total right:", total_right;
	print "Total wrong:", total_wrong;
			
	
main();

#3.

import random

def main():

	codes = {'A':'%', 'a':'9',
			'B':'@', 'b':'#',
			'C':'$', 'c':'5',
			'D':'^', 'd':'6',
			'E':'7', 'e':'7',
			'F':'*', 'f':'8',
			'G':'(', 'g':')',
			'H':'-', 'h':'.',
			'I':'`', 'i':'~',
			'J':'<', 'j':'>',
			'K':'//', 'k':'\\',
			'L':'{', 'l':'}',
			'M':'[',  'm':']',
			'N':'|', 'n':'||',
			'O':'.', 'o':'..',
			'P':'...','p':'....',
			'Q':'----','q':'____',
			'R': '+', 'r':'=',
			'S':'.,', 's': ',.',
			'T': 'TT', 't':'tt',
			'U': 'Q', 'u':'q',
			'V':'v', 'v':'V',
			'W':'M', 'w':'m',
			'X':'X', 'x':'x',
			'Y':'yy', 'y':'YY',
			'Z':'ZZZ', 'z':'zzz',
			 ' ':'0'};
	
	openfile = open('names.txt','r');
	
	file_contents = openfile.read();
	letters = list(file_contents);
	
	print letters;
	print file_contents;
	
	openfile.close();
	encrypt = [];
	
	for letter in range(len(letters)):
		if letters[letter] in codes:
			encrypt.append(codes[letters[letter]]);
	
	print encrypt;
	
	writefile = open('encrypt.txt','w');
	
	for item in encrypt:
		writefile.write(item+"\n");
	
	writefile.close();
	
	print "Written in encrypted file";

main();


#4.

def main():
	myset = set();
	openfile = open('numbers.txt','r');
	for num in openfile:
		myset.add(num.rstrip('\n'));
	
	print myset;

main();

"""
#5. Word frequency

words = file("test.txt", "r").read().split() #read the words into a list.
uniqWords = sorted(set(words)) #remove duplicate words and sort
for word in uniqWords:
    print words.count(word), word
    
#6.

1. import pickle
2. read file 1, split it into a list.
3. read file 2, split it into a list
4. Change lists to sets.
5. check which words appear in file 1, file 2, etc..

