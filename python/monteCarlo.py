import random
import numpy as np
from matplotlib import pyplot as plt

def coin_flip():
    """
    Simulates flipping a coin.
    0 -> heads
    1 -> tails
    """
    return random.randint(0, 1)

def roll_die():
    return random.randint(1, 6)

def get_grade():
    return random.uniform(50.0, 100.0)

def monteCarlo(n_itr, game):
    results = 0
    lst = list()

    for n in range(n_itr):
        if game == "die":
            rand_results = roll_die()
        elif game == "coin":
            rand_results = coin_flip()
        else:
            rand_results = get_grade()

        results += rand_results

        # Calculatings the probability value
        prob_val = results / (n + 1)
        lst.append(prob_val)

    if game == "die":
        plt.axhline(y = 3.5, color='r')
    elif game == "coin":
        plt.axhline(y = 0.5, color='r')
    else:
        plt.axhline(y = 75, color = 'r')

    plt.xlabel("Iterations")
    plt.ylabel("Probability")
    plt.plot(lst)
    plt.show()

    return results / n_itr

def main():
    #answer = monteCarlo(10000, "coin")
    #answer = monteCarlo(10000, "die")
    answer = monteCarlo(10000, "grade")
    print(f"Final Answer:\t{answer}")

if __name__ == '__main__':
    main()