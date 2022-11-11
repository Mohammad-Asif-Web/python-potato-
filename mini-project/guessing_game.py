import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
guess_count = 1

while guess_count <= 3:
    guess = int(input('guess: '))
    if guess == random.choice(list1):
        print('you win')
        break
    else:
        print('you fail')
    
    guess_count += 1