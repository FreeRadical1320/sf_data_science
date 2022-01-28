"""Game Guess the number. The computer tries by itself
"""
import numpy as np

def random_predict(number: int=1) -> int:
    """Randomly trying to guess

    Args:
        number (int, optional): [Guess number]. Defaults to 1.

    Returns:
        int: [Trying counts]
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Generate number
        if number == predict_number:
            break # Quit the cycle if guess
    return(count)


def score_game(randow_predict) -> int:
    """[Mean times of 1000 tryies ]

    Args:
        randow_predict ([type]): [Guess function]

    Returns:
        int: [Mean count times]
    """
    count_ls = []
    np.random.seed(1) # Fixing random seed
    random_array = np.random.randint(1, 101, size=1000) # Generate list of 1000 numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Your algorithm guess avarege in {score} times. ')
    return(score)

if __name__ == '_main_':
    # RUN
    score_game(random_predict)   