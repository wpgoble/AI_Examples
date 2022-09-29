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

def monteCarlo(n_itr):
    results = 0
    lst = list()

    for n in range(n_itr):
        flip_results = roll_die()
        results += flip_results

        # Calculatings the probability value
        prob_val = results / (n + 1)
        lst.append(prob_val)

    plt.axhline(y = 3.5, color='r')
    plt.xlabel("Iterations")
    plt.ylabel("Probability")
    plt.plot(lst)
    plt.show()

    return results / n_itr

def main():
    answer = monteCarlo(10000)
    print(f"Final Answer:\t{answer}")

if __name__ == '__main__':
    main()