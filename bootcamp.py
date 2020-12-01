# Some parts of https://www.udemy.com/course/complete-python-bootcamp/
import math

print('Hello, world!')

my_name = "Dmytro Tsybulia"
print(my_name[::-1])

print('Python {r}'.format(r = 'rules!'))

r = 'rules!'
print(f'Python {r}')

my_list = [150, 'Dmytro', 150.55]
print(my_list[::])
# OR
for each_item in range(len(my_list)):
	print(my_list[each_item])

my_list = [150, 'Dmytro', 150.55] #mutable
my_tuple = (150, 'Dmytro', 150.55) #immutable
my_dictionary = {'k1': 150, 'k2': 'Dmytro', 'k3': 150.55} #mutable

# Assessment Test 
s = 'hello'
# Print out 'e' using indexing
print(s[1:2])

# Reverse the string using slicing
print(s[::-1])

# Print out the 'o'
# Method 1:
print(s[-1])
# Method 2:
print(s[4::])

# Build this list [0,0,0] two separate ways.
# Method 1:
my_list_2 = [0, 0, 0]
print(my_list_2[::])
# Method 2:
my_list_3 = [0, 0]
my_list_4 = [0]
my_list_3_4 = my_list_3 + my_list_4
print(my_list_3_4[::])

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3[::])

# Sort the list below:
list4 = [5, 1, 4, 6, 3]
list4.sort()
print(list4[::])

# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# Grab hello
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# Grab hello
print(d['k1'][2]['k2'][1]['tough'][2][0])

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(list5)
list6 = set(list5) 
print(list6[::])

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
sentence = st.split()
for words in sentence:
	if words[0] == 's': print(words)

# Use range() to print all the even numbers from 0 to 10.
for number in range(0, 11, 2):
	print(number)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
my_string = [x for x in range(1, 51) if x % 3 == 0]
print(my_string)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
sentence = [i for i in st.split() if len(i) % 2 == 0]
for word in sentence:
	print('{} –– even!'.format(word))

st = 'Print every word in this sentence that has an even number of letters'
sentence = st.split()

for word in sentence:
if len(word) % 2 == 0:
	print('{} –– even.'.format(word))
else:
	print('{} –– not even!'.format(word))

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
for number in range(1, 101):
	if (number % 3 == 0 and number % 5 == 0):
		print('FizzBuzz')
	elif number % 5 == 0:
		print('Buzz')
	elif (number % 3 == 0):
		print('Fizz')
	else:
		print(number)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
my_string = [x[0] for x in st.split()]
print(my_string)

def myfunc(*args):
	number = [x for x in args if x % 2 == 0]
	return number

myfunc(1,2,3,4,5,6,6,-2)

def myfunc(string):
	new_string = []
	for i in range(len(string)):
		if i % 2 == 0:
			new_string.append(string[i].lower())
		else:
			new_string.append(string[i].upper())
	print(''.join(new_string))

myfunc('abcd')

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(number_01, number_02):
	if (number_01 % 2 == 0 and number_02 % 2 == 0):
		print(min(number_01, number_02))
	else:
		print(max(number_01, number_02))

lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
	separated_text = text.split(" ")
	if separated_text[0][0] == separated_text[1][0]: ### or just 1 line instead of 4 => "return separated_text[0][0] == separated_text[1][0]"
		print(True)
	else:
		print(False)

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(number_01, number_02):
	if (number_01+number_02 == 20 or number_01 == 20 or number_02 == 20):
		print(True)
	else:
		print(False)

makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# Note: 'macdonald'.capitalize() returns 'Macdonald'
def old_macdonald(name):
	new_macdonald = []
	for letter in range(len(name)):
		if letter == 0 or letter == 3:
			new_macdonald.append(name[letter].upper())
		else: 
			new_macdonald.append(name[letter].lower())
	print(''.join(new_macdonald))

old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
def master_yoda(entered_phrase):
	reversed_phrase = list(reversed(entered_phrase.split()))
	print(' '.join(reversed_phrase))

master_yoda('I am home')
master_yoda('We are ready')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
def almost_there(entered_number):
	if entered_number >= 90 and entered_number <= 110:
		print(entered_number, True)
	elif entered_number >= 190 and entered_number <= 210:
		print(entered_number, True)
	else:
		print(entered_number, False)

# BVA of the 1st if
almost_there(89)
almost_there(90)
almost_there(110)
almost_there(111)
almost_there(105)

# BVA of the 2nd if
almost_there(189)
almost_there(190)
almost_there(210)
almost_there(211)
almost_there(195)

# EP
almost_there(50)
almost_there(150)
almost_there(220)

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
def has_33(array):
	for each_item in range(0, len(array) - 1):
		if array[each_item] == 3 and array[each_item + 1] == 3:
			return True
	return False

if has_33([1, 3, 3]) == True:
	print(True)
else:
	print(False)
if has_33([1, 3, 1, 3]) == True:
	print(True)
else:
	print(False)
if has_33([3, 1, 3]) == True:
	print(True)
else:
	print(False)

# PAPER DOLL: Given a string, return a string where for every 
# character in the original there are three characters
def paper_doll(text):
	result = []
	for each_letter in text:
		result += each_letter * 3
	print(''.join(result))

paper_doll('Hello!')
paper_doll('Mississippi')