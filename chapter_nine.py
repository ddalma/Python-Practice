"""
def main():
	count = 0;
	
	my_string = raw_input("Enter a sentence:");
	
	for ch in my_string:
		if ch =='t' or ch == 't':
			count += 1;
	
	print "The letter T appears", count,"times";

main();

def main():
	name = 'Carmen';
	print "The name is", name;
	name = name + ' Brown';
	print "Now the name is", name;

main();

#The get_login_name function accepts a first
#name, last name and ID number as arguments
#.It returns a system login name



def get_login_name(first, last, idnumber):
	set1 = first[0:3];
	
	set2 = last[0:3];
	
	set3 = idnumber[-3:]
	
	login_name = set1 + set2 + set3;
	
	return login_name;

def main():
	first = raw_input("Enter your first name:");
	last = raw_input("Enter your last name:");
	idnumber = raw_input("Enter your student ID number:");
	
	print "Your system login name is:";
	print get_login_name(first,last,idnumber);

main();

mystring = 'abcdefg';
print mystring[2:5];
#cde

my_string = 'abcdefg';
print my_string[3:];
#defg

mystring1 = 'abcdefg';
print mystring1[:3];
#abc


mystring2 = 'abcdefg';
print mystring2[:];
#abcdefg

text = "Four score and seven years ago";
if 'seven' in text:
	print 'The string "seven" was found.';
else:
	print 'The string "seven" was not found.';

#isalnum() - returns true if the string contains
#only alphabetic letters or digits and is at least
#one character in length. Return false otherwise.


#isalpha() - returns true if the string contains only
#alphabetic letters, and is at least one character
#in length. Return false otherwise.

#isdigit() - return true if the string contains only numeric
#digits and is at least one character in length. Return false
#otherwise.

#islower() - Returns true if all of the alphabetic letters in the string
#are lowercase, and the string contains at least one alphabetic letter.
#Return false otherwise.

#isspace() - Returns true if the string contains only whitespace characters,
#and is at least one character in length. Return false otherwise.(Whitespace
#characters are spaces, newline (\n), and tabs(\t);

#isupper() - Returns true if all of the alphabetic letters in the string are 
#uppercase, and the string contains at least one alphabetic letter. Returns false
#otherwise.

def main():
	user_string = raw_input("Enter a string:");
	
	if user_string.isalnum():
		print "The string is aphanumeric:";
	if user_string.isdigit():
		print "The string contains only digits";
	if user_string.isalpha():
		print "The string contains only alphabetic characters.";
	if user_string.isspace():
		print "The string contains only whitespace characters.";
	if user_string.islower():
		print "The letters in the string are all lowercase";
	if user_string.isupper():
		print "The letters in the string are all uppercase";

main();


#Modification Methods:

lower() - converts all alphabetic letter to lowercase

lstrip() - returns a copy of the string with all leading
whitespace characters removed.

lstrip(char) - The char argument is string containing a character.
Returns a copy of the string with all instance of char that appear
at the beginning of the string removed.

rstrip() - returns a copy of the string with all trailing whitespace
characters removed.

rstrip(char) - method returns a copy of the string with all instances of
char that appear at the end of the string removed.

strip() - returns a copy of the string with all leading and trailing whitespace
characters removed.

strip(char) - returns a copy of the string with all instances of char that appear
at the beginning and the end of the string removed..

upper() - return a copy of the string with all alphabetic letters converted to uppercase.

#Search and replace methods:

endswith(substring) - The substring argument is a string. The method returns true if the string ends
with substring.

find(substring) - The method returns the lowest index in the string where substring is found. If
substring is not found, the returns -1.

replace(old, new) - the old and new arguments are both strings. The method returns a copy of the
string with all instances of old replaced by new.

startswith(substring) - the substring argument is a string. The method returns true if the string
starts with substring.

#this program calls the split method, using the

def main():
	date_string = '11/26/2012';
	
	date_list = date_string.split('/');
	
	print "Month:", date_list[0];
	print "Day:", date_list[1];
	print "Year:",date_list[2];

main();

def get_login_name(first, last, idnumber):
	set1 = first[0:3];
	
	set2 = last[0:2];
	
	set3 = idnumber[-3:];
	
	login_name = set1 + set2 + set3;
	
	return login_name;

def valid_password(password):
	correct_length = False;
	has_uppercase = False;
	has_lowercase = False;
	has_digit = False;
	
	if len(password) >= 7:
		correct_length = True;
		
		for ch in password:
			if ch.isupper():
				has_uppercase = True;
			if ch.islower():
				has_lowercase = True;
			if ch.isdigit():
				has_digit = True;
	
	if correct_length and has_uppercase and has_lowercase and has_digit:
		is_valid = True;
	else:
		is_valid = False;
		
	return is_valid;


def main():
	password = raw_input("Enter your password:");
	
	while not valid_password(password):
		print "That password is not valid.";
		password = raw_input("Enter your password:");
	
	print "That is a valid password.";

main();

def main():
	#print nice rows increasing in length.
	for count in range(1,10):
		print 'Z' * count;
	
	#print nine rows decreasing in length.
	for count in range(8,0,-1):
		print 'Z' * count;
main();


#This program demonstrates the split method.

def main():
	#Create a string with multiple words.
	my_string = "One two three four";
	
	#Split the string.
	word_list = my_string.split();
	
	#Print the list of words
	print word_list;

main();


#This program calls the split method using the 
#'/' character as a separator

def main():
	date_string = "10/07/1993";
	date_list = date_string.split('/');
	
	print "Month:",date_list[0];
	print "Day:",date_list[1];
	print "Year:",date_list[2];

main(); 

#Algorithm Workbench:

#1.
total = 0;
again = 'Y';
while again == 'Y':
	total += 1;
	choice = raw_input("Again?( Y or y for yes, anything else is no):");
	again = choice.upper();

print "Total:",total;

#2.

def main():
	sentence = raw_input("Enter a sentence:");
	total = 0;
	for num in range(len(sentence)):
		total += 1;
	
	print "Total:", total;

main();

#3.

def main():
	mystring = 'Sunday Monday Tuesday Wednesday';
	space_count = 0;
	
	for space in mystring:
		if space == ' ':
			space_count += 1;
	
	print space_count;

main();


#4.

def main():
	mystring = "One:1 Two:2 Three:3";
	
	count = 0;
	
	for lcc in mystring:
		if lcc.islower():
			count += 1;
	
	print count;

main();


#5.

def main():
	word = raw_input("Enter a website:");
	
	searching(word);

def searching(string):
	found = False;
	if '.com' in string:
		found = True;
		print ".com was found"
		print found;
	else:
		print "Not found";
		print found;
		

main();

#6.

def main():
	mystring = "Talking tuesday that is the day";
	stringcopy = '';
	for ch in mystring:
		if ch == 't':
			ch = ch.upper();
			stringcopy = stringcopy + ch;
	
	print stringcopy;

main();

#7.

def main():
	sentence = raw_input("Enter a sentence:");
	print "The sentence you choose:",sentence;
	reversing(sentence);

def reversing(string):
	word = string[::-1];
	print "Reversed word:",word;
	
main();


#8.

def main():
	string = raw_input("Enter a string:");
	substring = string[0:3];
	
	print "Sentence:", string;
	print "The first three characters of the sentence is:", substring;

main();

#9. 
def main():
	sentence = raw_input("Enter a sentence:");
	sub_sentence = sentence[-3:];
	
	print "Sentence:", sentence;
	print "The last three characters of the sentence is:", sub_sentence;
	

main();

#10.

def main():
	mystring = 'cookies>milk>fudge>cake>ice cream';
	print mystring;
	my_list = mystring.split('>');
	print my_list;

main();
	

#Programming Exercises

#1.
def main():
	first = raw_input("Enter your first name:");
	middle = raw_input("Enter your middle name:");
	last = raw_input("Enter your last name:");
	
	initials(first,middle,last);

def initials(f, m,l):
	first = f[0].upper();
	middle = m[0].upper();
	last = l[0].upper();
	
	total = first+'.'+middle+'.'+last+'.';
	
	print total;

main();	

#2.

def main():
	string = raw_input("Enter a series of numbers with no space:");
	print "Number string:", string;
	my_list = list(string);
	print my_list;
	
	total = 0;
	for num in my_list:
		value = int(num);
		total += value;
	
	print "The total value:", total;
main();


#3.

def main():
	date = raw_input("Enter the date in mm/dd/yyyy format:");
	date_list = date.split('/');
	if date_list[0] == '01':
		date_list[0] = "January";
		
	elif date_list[0] == '02':
		date_list[0] = 'February';
		
	elif date_list[0] == '03':
		date_list[0] = 'March';
		
	elif date_list[0] == '04':
		date_list[0] = 'April';
		
	elif date_list[0] == '05':
		date_list[0] = 'May';
		
	elif date_list[0] == '06':
		date_list[0] = 'June';
		
	elif date_list[0] == '07':
		date_list[0] = 'July';
		
	elif date_list[0] == '08':
		date_list[0] = 'August';
		
	elif date_list[0] == '09':
		date_list[0] = 'September';
		
	elif date_list[0] == '10':
		date_list[0] = 'October';
		
	elif date_list[0] == '11':
		date_list[0] = 'November';
		
	elif date_list[0] == '12':
		date_list[0] = 'December';
	
	day = date_list[1];
	year = date_list[2];
	
	string_date = date_list[0]+" "+day+", "+year;
	
	print string_date;

main(); 

#4.
def main():
	sentence = raw_input("Enter a sentence to be encrypted in morse code:");
	upper_sentence = sentence.upper();
	my_list = list(upper_sentence);
	print my_list;
	
	morse_code(my_list);

def morse_code(list):
	morse_list =[];
	for index in range(len(list)):
		if list[index] == ' ':
			list[index] = ' ';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] ==',':
			list[index] = '--..--';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='.':
			list[index] = '..--..';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='?':
			list[index] = '..--..';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='0':
			list[index] = '-----';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='1':
			list[index] = '.----';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='2':
			list[index] = '..---';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='3':
			list[index] = '...--';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='4':
			list[index] = '....-';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='5':
			list[index] = '.....';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='6':
			list[index] = '-....';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='7':
			list[index] = '--...';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='8':
			list[index] = '---..';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='9':
			list[index] = '----.';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='A':
			list[index] = '.-';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='B':
			list[index] = '-...';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='C':
			list[index] = '-.-.';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='D':
			list[index] = '-..';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='E':
			list[index] = '.';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='F':
			list[index] = '..-.';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='G':
			list[index] = '--.';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='H':
			list[index] = '....';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='I':
			list[index] = '..';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='J':
			list[index] = '.---';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='K':
			list[index] = '-.-';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='L':
			list[index] = '.-..';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='M':
			list[index] = '--';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='N':
			list[index] = '-.';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='O':
			list[index] = '---';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='P':
			list[index] = '.--.';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='Q':
			list[index] = '--.-';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='rR':
			list[index] = '.-.';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='S':
			list[index] = '...';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='T':
			list[index] = '-';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='U':
			list[index] = '..-';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='V':
			list[index] = '...-';
			morse_list.append(list[index]);
			print list[index];	
			
		elif list[index] =='W':
			list[index] = '.--';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='X':
			list[index] = '-..-';
			morse_list.append(list[index]);
			print list[index];	
			
		elif list[index] =='Y':
			list[index] = '-.-';
			morse_list.append(list[index]);
			print list[index];
			
		elif list[index] =='Z':
			list[index] = '--..';
			morse_list.append(list[index]);
			print list[index];
	print morse_list;
	
main();


#5. Alphabetic Telephone Number Translator

def main():
	telephone = raw_input("Enter a telephone number (XXX-XXX-XXXX):");
	upper_num = telephone.upper();
	telephone_list = list(upper_num);
	print telephone_list;
	
	number_translator(telephone_list);

def number_translator(list):
	num_list = [];
	for num in range(len(list)):
		if list[num] == 'A' or list[num] == 'B' or list[num] == 'C':
			list[num] = '2';
			num_list.append(list[num]);
			print list[num];
		elif list[num] == 'D' or list[num] == 'E' or list[num] == 'F':
			list[num] = '3';
			num_list.append(list[num]);
			print list[num];
		elif list[num] == 'G' or list[num] == 'H' or list[num] == 'I':
			list[num] = '4';
			num_list.append(list[num]);
			print list[num];
		elif list[num] == 'J' or list[num] == 'K' or list[num] == 'L':
			list[num] = '5';
			num_list.append(list[num]);
			print list[num];
		elif list[num] == 'M' or list[num] == 'N' or list[num] == 'O':
			list[num] = '6';
			num_list.append(list[num]);
			print list[num];
		elif list[num] == 'P' or list[num] == 'Q' or list[num] == 'R' or list[num]== 'S':
			list[num] = '7';
			num_list.append(list[num]);
			print list[num];
		elif list[num] == 'T' or list[num] == 'U' or list[num] == 'V':
			list[num] = '8';
			num_list.append(list[num]);
			print list[num];
		elif list[num] == 'W' or list[num] == 'X' or list[num] == 'Y' or list[num]== 'Z':
			list[num] = '9';
			num_list.append(list[num]);
			print list[num];
		else:
			num_list.append(list[num]);
			print list[num];
	
	print num_list;			

main();

"""

#8.Sentence Capitalizer
def main():
	string = raw_input("Enter a sentence/sentences please:");
	sentence = string.split('.');
	for i in sentence:
		print i.strip().capitalize()+".";

main();