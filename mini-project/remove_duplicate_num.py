# Write a program to remove the duplicates in a list

nubers = [5, 8, 3, 8, 4, 5,  1, 8, 4, 0]

single = []
for num in nubers:
    if num not in single:
        single.append(num)

print(single)

