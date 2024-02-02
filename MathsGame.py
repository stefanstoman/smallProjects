import random

print('Welcome to the maths game!')

rand1 = None
rand2 = None
score = 0

while True:
    rand1 = random.randint(1, 12)
    rand2 = random.randint(1, 12)
    while True:
        answ = input(f'What is {rand1} x {rand2}? ')
        try:
            answ_int = int(answ)
        except:
            print('Invalid input')
            continue
        if answ_int == rand1 * rand2:
            print('CORRECT!!')
            score = score + 1
            print(f'Your score is {score}')
            break
        else:
            print('Incorrect, try again!')
            score = 0
            print('Sorry, your score is now 0.')
            continue
    con = input('Continue? (y/n): ')
    if con == 'n': break

print('Thank you for playing!')
print(f'Score = {score}')