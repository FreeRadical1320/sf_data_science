"""Game 'Guess the number'"""

import numpy as np

number = np.random.randint(1, 101) # Guess the number

# Try counts
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100: '))
    
    if predict_number > number:
        print('Your number is grater than need!')

    elif predict_number < number:
        print('Your number is smaller than need!')
    
    else:
        print(f'You win!!! The nuber is {number}. You had tried {count} times')
        break # Game over. Quit the cycling
