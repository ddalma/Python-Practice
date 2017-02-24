#The contact class holds contact information.

class Contact:
	#the __init__ method initializes the attributes	
	def __init__(self,name, phone,email):
		self.__name = name;
		self.__phone = phone;
		self.__email = email;
		
	#The set_name methods sets the name attribute.
	def set_name(self, name):
		self.__name = name;
		
	#the set_phone method sets the phone attribute.
	def set_phone(self, phone):
		self.__phone = phone;
	
	#the set_email methods sets the email attribute.
	def set_email(self, email):
		self.__email = email;
	
	#the get_name method returns the name attribute.
	def get_name(self):
		return self.__name;
	
	#the get_phone method returns the phone attribute.
	def get_phone(self):
		return self.__phone;
	
	#the get_email method returns the email attribute.
	def get_email(self):
		return self.__email;
	
	#The __str__ method returns the object's state
	#as a string.
	
	def __str__(self):
		return "Name: "+self.__name+ \
			"\nPhone: "+self.__phone+ \
			"\nEmail: "+self.__email;
