class Employee:
	def __init__(self, name, id_num, dept, job_tit):
		self.__name = name;
		self.__id_num = id_num;
		self.__dept = dept;
		self.__job_tit = job_tit;
	
	def set_name(self, name):
		self.__name = name;

	def set_id_num(self, id_num):
		self.__id_num = id_num;
		
	def set_dept(self, dept):
		self.__dept = dept;
	
	def set_job_tit(self, job_tit):
		self.__job_tit = job_tit;
	
	
