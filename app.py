# Python features: Versatile, Strong Community Support, English like
# Python Shell (Interactive)
# 	quit() to come out of shell of python
# VSCode has Play Button
# A Script of Python

# Datatypes are infered
phone = 9822174322
height =  5.9

# Datatype conversion
num = int(10.03) # will be 10

# single double qoutes 
# + operator for string concatenation
"Rais"+'Sana'

# for getting input from user
input("msg") 

# Datatypes
num:int = 10,
name:str = 'Rais',
name = "Sana"

height:float = 5.9 
male:bool = True #True or False is boolean
female:bool = False	

# Operator
10//5 #for whole division
23%2 #for modular division
# not True: # not for negation

		
# List is container can have mix-types (built-in?)
my_list = ['a', 'b', 'c']
my_list[0] # 0 zero index 
my_list.append('d')
my_list.remove('c') # the value to be removed
del my_list[2] # to remove by position

# to check if item is in the list 
if 1 in [1,2,3]: 
	print('Present')
	
# also you can pass list
if 'a' in my_list: 
    print('a present int the empty')

# Loop
for item in my_list:
	print(item)
	
# Even a list of list
	
family = [
    ['Rais', 'Sana', 'Nazar', 'Gauhar'],
    ['Eesa', 'Mammu', 'Yousuf']
]
	
# Dictionary: Key value pairs

my_dict = {
    'key1': 'value1',
    'key2': 'value2',
}

my_dict['key1']	# look-up 
	
# can be
	
menu = {'key1': 12, 'key2': 13}
my_new_dict = { 10: 'hello', 12: 6.5} # mix hetrogeneous types

my_dict = {}
my_dict['key7'] = 'value7'
 
# to delete
# key error when there is not that key
del my_dict['key1']

my_dict.get('key7') # safe way to read value, if returns none, it is absent

# Dictionary loop
for item in my_dict:
    # when you loop over dictionary it only returns keys
    print(item)
	

# for key and value
for key, value in my_dict.items():
	print(key, value)


# Will iterate from 1 to 10
for i in range(1,10):
	print(i)


for index, value in enumerate(my_list):
	print(index, value)	

# for loop run definate number of loops
#On the hand while loop in suitable for indefinate number of loop
# or when you are not sure how many loops are there and need contional end
num = 0
while(True):
	num = input('Enter Even Number')
	if num%2 != 0:
		break

# continue will jump to next iteration
#continue

# python doesn't have do-while like other langs


# pip package-name  (difference pip and pip3?)

# Variables are function scoped
# add example

class Person:
	name: str
	last: str
	
	def __init__(self, fn, ln):
		self.name = fn
		self.last = ln
		
	def display_name():
		print(f'name {self.name} last {self.last}')
		

Person(fn='Rais', ln='Iqbal') # name of of class to call initializer


# inheritance
class Student(Person):
	roll: int
	def __init__(self, fn, ln, rn):
		super().__init__(fn, ln)
		self.roll = rn
		
    def display_name():
        super().display_name()
        print('is a student and wife')

		

wife_obj = Student('Sana', 'Rais', 123)

wife_obj.display_name()


# Try catch save program from crashing? how?
# finally is used to do something irrespetive of try succeed of failed
# like close file or DB connection
try:
	fs = open('README.txt') # returns file object
	fs.read() # read file as string
	fs.readline() # to read single line
	for line in fs.readlines(): # loop on file
		print(line)
    
        

except err:
	print('Error')
finally:
	fs.close()

# How to throw exceptions yourself
try:
	if my_dict['stream'] == None:
		raise Exception('Stream not provided') # custome exception
except err:
	print('Error')
	

# using with you can handle files dont need to close yourself
with open('README.txt') as file:
	file.write('Adding line to the file.')
	print('Print file')
	


