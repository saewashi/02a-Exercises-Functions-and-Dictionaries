'''

02a Exercises

These skills can be used in assignment 2. These exercises are designed to teach you about some more complex data and control structures

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening.


'''
# Paste the following lines into IDLE, and then enter the result in the comment following the block
example_list = [1,17,20]
s = 0
for e in example_list:
	s += e
print(s)
#
# What do these five lines of code do?
# I got this: 38
# supposed to do, I would say that it is supposed to take  the numbers in the list that is assigned to "s"
# and "e" to produce the addition outcome.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
example_set = {1,2,3,4,2,3,1,4,3,2,1}
print(example_set)
for c in range(3,10):
	if c in example_set:
		print('{count} is in the set'.format(count=c))
example_set_2 = {4,5,6,7}
example_set = example_set - example_set_2
print(example_set)
set_to_list = list(example_set)
print(set_to_list)
#{1, 2, 3, 4}
# 3 is in the set
# 4 is in the set
# {1, 2, 3}
# [1, 2, 3]
#
#
#
#
# What qualities of a python set do you see in the (above) example?

# The qualities that I see of a python set, is that it finds the nummbers in a specfic set, and
# prints the set. It also finds the same repeating numbers in two sets.

# In what situations might a python set be a useful data structure?
#  A python set may be useful data structure when there are items within the set, that the user-
# may want to find without having to search through all the sets themselves to find data.
# For example, if we wanted to find someone within a public file but didn't want to search through all-
# the people within that public file, they could create a data structure that finds specfic people
# with a specific name that seperates them from all the other names on file.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
example_dictionary = { 'class':'Z-399', 'teacher':'Jason Francis', 'time':9.0, 5:12345 }
print(example_dictionary)
print(example_dictionary[5])
example_dictionary['time'] = '9:00'
print(example_dictionary)
students = ['James','Paige','George','Ruth','Gwen','Claire']
example_dictionary['students'] = students
print(example_dictionary)
print(example_dictionary['students'][2])

#{'class': 'Z-399', 'teacher': 'Jason Francis', 'time': 9.0, 5: 12345}
# 12345
# {'class': 'Z-399', 'teacher': 'Jason Francis', 'time': '9:00', 5: 12345}
# {'class': 'Z-399', 'teacher': 'Jason Francis', 'time': '9:00', 5: 12345, 'students': ['James', 'Paige', 'George', 'Ruth', 'Gwen', 'Claire']}
# George
#
#
#
# What qualities of a python dictionary do you see in the (above) example?
# The qualities that I see in this python dictionary, is that it finds the name of the person, the class, the teacher, the time,
# and the class section number and pulls all of the data from the dictionary about that class.

# Write a python dictionary that might describe a bicycle. I'll get you started. Think about what qualities a bicycle could have (top speed, mileage, pedals, seat height, etc)
bicycle = { 'color':'Blue', 'wheels': 'Speedy Wheels', 'model:''Speed bikes':1966 }
print(bicycle)
bicycle['model'] = 'Speedy Bikes'
print(bicyle)
bicycle['color'] = 'Blue'
print(bicycle)
bicycle['wheels'] = 'Speedy Wheels,' '1966'
print(bicyle)

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
def product_list(example_list):
	s = 1
	for e in example_list:
		s *= e
	return s
r = product_list([1,2,3])
print(r)
print(product_list([2,5,6]))
print(product_list([-2,3,-4,5,-6]))
# 6
# 60
# -720
#
# What is happening in the (above) example?
# What is happening i the above example is that the list is multplying all the numbers together in each list to get the ending multiplication result.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
def is_leap_year(year):
	'''
	year is an integer that represents a year in the Gregorian calendar, and is_leap_year describes the policy of whether a given year will have 366 days
	A leap year is every fourth year, except when that year is divisible by 100, except when that year is divisible by 400
	'''
	leap = False
	try:
		if year % 400 == 0:
			leap = True
		elif year % 100 == 0:
			leap = False
		elif year % 4 == 0:
			leap = True
	except TypeError:
		leap = False
	return leap
years = [2017,2018,2000,2100,2400,"This isn't even a year"]
for y in years:
	if is_leap_year(y):
		print(str(y) + ': I get an extra day this year!')
	else:
		print(str(y) + ': Just 365 for me')
#
#2017: Just 365 for me
#2018: Just 365 for me
#2000: I get an extra day this year!
#2100: Just 365 for me
# 2400: I get an extra day this year!
#This isn't even a year: Just 365 for me
#
#
#
#
# What is happening in the (above) example?

# What is happening in the example above, is that we are defining a function that is checking to see if-
# each year has a leap year for the following years. Ex: if 2017 doesn't have a leap year, then the programs runs-
# it has false, and the same goes for True.

# What is the purpose for the multi-line comment at the beginning of the is_leap_year function?

# The purpose of the multi-line comment is that it describes what the function is supposed to do, -
# and it's helpful if someone has a long comment to input.

# What happens if you pass a value to the function that isn't a year? Why?
#  If you pass a value to the function that isn't a year, then it would produce an error.
# The reason being, is that the function is designed to check and see if each year is a regular year, -
# or a leap year. If a value isn't a year, then there's no way for the function to perform the Boolean.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
def is_fizz(test):
	if not isinstance(test,int):
		return False
	if test % 3 == 0:
		return True
	return False
def is_buzz(test):
	if not isinstance(test,int):
		return False
	if test % 2 == 0:
		return True
	return False
for i in range(0,10):
	if is_fizz(i) and is_buzz(i):
		print('%d: fizzbuzz'%i)
	elif is_fizz(i):
		print('%d: fizz'%i)
	elif is_buzz(i):
		print('%d: buzz'%i)
	else:
		print(i)
#0: fizzbuzz
# 1
# 2: buzz
# 3: fizz
# 4: buzz
# 5
# 6: fizzbuzz
# 7
# 8: buzz
# 9: fizz
#
#
#
#
#
#
#
#
#
# What is happening in this example?

# What is happening in this example is that the function taking a range of numbers, and testing if each number -
# will produce a fizz, buzz, or fizzbuzz, in a Boolean statement.

# How would you alter the program so that it prints fizz on multiples of 5 and buzz on multiples of 4?

# How I would alter the program so that it prints fizz on multiples of 5 and buzz on 4, is change the two -
# numbers in the if statements.

# We actually don't want the program to print fizzbuzz when i <= 0. How would you fix this problem?

#  How I would fix that is by changing the values in the if statements so that each time it runs -
# past a certain nummber in the range, it won't print fizzbuzz.

# How would you alter the program so that it prints your name whenever both conditions are met?

# How I would alter the prgram so that it prints my name whenever both conditions are met, -
# is to add another if statement that contains my name, and prints after the conditions are met.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
def get_option(options):
	'''
	Prints out the choices for this location and invites the player to make a selection
	Parameters: options is a list of dictionaries {choice, location}; choice is a string and location is an int
	Returns: location if one is available and selected, 0 otherwise
	'''
	to_return = 0
	if len(options) == 0:
		print('The end!')
		return to_return
	while to_return == 0:
		choice = 1
		for o in options:
			print('{which_option}: {description}'.format(which_option=choice, description=o['choice']))
			choice += 1
		print('q: to quit')
		decision = input('Which option do you choose? ')
		try:
			if decision == 'q':
				return 0
			decision = int(decision)-1
			if decision >= 0 and decision < len(options):
				to_return = options[decision]['location']
		except ValueError:
			print('Please enter one of the options')
			to_return = 0
	return to_return


script = [
	{
		'location':1
		,'description':'It was a dark and stormy night. The door is locked.'
		,'options':[
			{'choice':'Open the door','location':2}
			,{'choice':'Run away','location':3}
		]
	},
	{
		'location':2
		,'description':'I said it was locked!'
		,'options':[]
	},
	{
		'location':3
		,'description':'Coward!'
		,'options':[]
	}
]
starting = 0
get_option(script[starting]['options'])
# What is happening in this block of code?
# What is happeninh in this block of code, is that it is introducting the user to a storyline game.
# It is specifically giving the user options to choose from, and whichever the user inputs,-
# it leads to another storyline by the choices they make.

# What does the get_option function do?

# get_option stores the list of options that the user has to choose from, instead of each option -
# being written individually.

# How would you display the description of the current location?
# How I would display the description of the current location, is being in a haunted house, and it's storming,
# the user can either run away, or they can try and open the door which is locked.

# How would you display the description of the next location (after selecting an option)?
# I would display the description as a narrator telling the person that the door was locked,
# but that they decided to do it anyway.
