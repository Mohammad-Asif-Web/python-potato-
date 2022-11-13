try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
# the ZeroDivisonError used for 0 numeric number, some time it gives error
# that's why to handle this error,use this exeption
except ZeroDivisionError:
    print('Age cannot be 0.')
# the ValueError used for input converted value, when we need integer value
# user has given a string value, so it gives a error,
except ValueError:
    print('Invalid value')