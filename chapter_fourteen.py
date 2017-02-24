"""
import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()



import Tkinter

def main():
	main_window = Tkinter.Tk();
	
	Tkinter.mainloop();

main();

sum = 0
second_sum = 0
for i in range(1,101):
	sum += i **2

for i in range(1,101):
	second_sum += i;

second_sum = second_sum **2

print "second sum:", second_sum
print "sum:", sum
print "difference:", second_sum - sum


for i in range(1,13195):
	if 13195 % i == 0:
		print(i)
"""

lst = [1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1]
e_list = [0] * len(lst)
k = 3
count = 0
for n in range(1, len(lst)):
	value_one = lst[n-1]
	value_two = lst[n]
	if value_one + value_two == 10:
		e_list[n-1] = value_one
		e_list[n] = value_two
		count += 1
		
print "pairs:",count
print e_list
