names = ['Asif', 'Jane', 'Khan', 'John', 'Sarah', 'Mary']

print(names) #['Asif', 'Jane', 'Khan', 'John', 'Sarah', 'Mary']
print(names[0]) #Asif
print(names[-1]) #Mary
print(names[:]) #['Asif', 'Jane', 'Khan', 'John', 'Sarah', 'Mary']
print(names[2:]) #['Khan', 'John', 'Sarah', 'Mary']
print(names[2:4]) #['Khan', 'John']

                            # Lists Methods
numbers = [5, 2, 9, 5, 8]
numbers.append(33) #add number to last
numbers.insert(0, 10) #fist take index number, second takes the value
numbers.remove(2) #remove 2
numbers.sort() #sorted the number
numbers.reverse() #reverse the number
numbers.clear() # empty the list, all our items will be clear
numbers.pop() #removes the last item of the list
print(numbers.index(9))   #find the index of number
print(50 in numbers) # it will give boolean value True/False
print(numbers.count(5)) #counts how many 5 are in the list -- 2
print(numbers)
