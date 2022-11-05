birth_year = input('>Birth year: ')
age = 2022 - int(birth_year)
# the input() always return string type data, so if we need integer or float type data we have to use int() and float().
print(f"I am {age} years old")
print(type(birth_year))
# type() will return -  <class 'str'>

# double/ single quotes problem - always use double quotes when need of single quotes
course = "python's Course for beginners"
print(course)
