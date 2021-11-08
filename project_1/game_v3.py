"""
Game 'Guess the number'
The computer have to guess the number in minimum tryings
"""

import numpy as np


def random_predict(number: int=1) -> int:
    """Guess the number algorithm
    Args:
        number (int, optional): The hidden number. Defaults to 1.
    Returns:
        int: Try counts
    """
    count = 0 # Try counts
    range_low = 1 # Set the basic low range border
    range_high= 101 # Set the basic high range border

    while True:
        count += 1
        predict_number = np.random.randint(range_low, range_high)  # Estimated number
        
        if predict_number == number:
            break  # Game over. Quit the cycling
        elif predict_number > number: 
            range_high = predict_number # Set new high range border
        else:
            range_low = predict_number # Set new low range border
    return count


def score_game(random_predict) -> int:
    """Measuring the average number of attempts over 1000 approaches
    Args:
        random_predict ([type]): guess function
    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1)  # Fixing seed for reproducibility of the result
    random_array = np.random.randint(1, 101, size=(1000))  # Generate the list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses the number on average in: {score} tries')
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
