# Write a program to find the largest number in a list

numbers = [20, 5, 43, 93, 8, 72, 0, 52, 39]

guess = numbers[0]
for num in numbers:
    if guess < num:
        guess = num
print(guess)
