"""Game Guess the number
"""
import numpy as np
number = np.random.randint(1, 101) # generate the number
    
# try counting
count = 0
   
while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100: ')) 
        
    if predict_number > number:
        print('Your number is bigger than basic')
    elif predict_number < number:
        print('Your number is smaller than basic')
    else:
        print(f'You win!!! The number is {number}. You had tried {count} times.')
        break # Quit the cycle