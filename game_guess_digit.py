"""
This game for others mind
Check right digit in random
"""

import random

number = random.randint(0, 101)
while True:
    answer = input('Enter digit: ')
    if not answer or 'exit' in answer or 'break' in answer:
        break

    if not answer.isdigit():
        print('Enter right digit!')
        continue

    user_answer = int(answer)

    if user_answer > number:
        print('Digit less..')
    elif user_answer < number:
        print('Digit more..')
    else:
        print('OK, correct answer is', number)
        break
