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