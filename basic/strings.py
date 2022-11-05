# multi line string
str = '''
Hi sir,

This is Md Asif from Bangladesh
I hope you are well.

Thank you
The support team
'''
# print(str)

# Get single character by index
course = "python for beginners"
print(course[0]) # Ans- p will return
# negative one index of the last character
print(course[-1]) # Ans- s will return from last
# start from 0 index and ends before 3. won't return 3 no index
print(course[0:3]) # return pyt not h
# returns all character exclude p 
print(course[1:]) # ans- ython for beginners
# to clone the all character
print(course[:]) # returns python for beginners

name = 'muhammad'
print(name[1:-1]) #returns uhamma


            # Formatted strings - two way to formate strings
first = 'Asif'
last = 'hossain'
# 1- concatenation style
message = first + ' [' + last + '] is a coder'
print(message)
# 2 - template leteral type
msg = f'{first} [{last}] is a coder'
print(msg)


                # STRING METHODS
# Get lenght
print(len(course)) #return the total character number
# uppercase and lowercase
print(course.upper())
print(course.lower())
#find the index number by input the character
print(course.find('p')) # return 0 index
# we can get a total number by input the words
print(course.find('beginners')) 
# replace
print(course.replace('beginners', 'Absolute beginners'))
# get boolean expression
print('python' in course) # returns true
