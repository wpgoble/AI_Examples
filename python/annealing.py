from numpy import arange, exp, asarray
from numpy.random import rand, randn, seed
from matplotlib import pyplot as plt

def objective(x):
    val = x[0]**2.0
    return val

def draw_plot(x, y, optima=False):
    plt.plot(x, y)
    if optima:
        x_optima = 0.0
        plt.axvline(x = x_optima, ls='--', color = 'red')
    plt.show()

def main():
    r_min, r_max = -5.0, 5.0
    inputs = arange(r_min, r_max, 1e-1)
    results = [objective([x]) for x in inputs]
    draw_plot(inputs, results, True)

# explore temperature vs algorithm iteration for simulated annealing
def temp_vs_algo():
    iterations = 100
    initial_temp = 10
    iterations = [i for i in range(iterations)]
    temperatures = [initial_temp / float(i + 1) for i in iterations]
    differences = [1e-2, 1e-1, 1.0]

    for d in differences:
        metropolis = [exp(-d / t) for t in temperatures]
        label = 'diff = %.2f' % d
        plt.plot(iterations, metropolis, label = label)

    plt.xlabel("Iteration")
    plt.ylabel("Temperature")
    plt.legend()
    plt.show()

def simulated_annealing(objective, bounds, n_itr, step_size, temp):
    best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    best_eval = objective(best)
    curr, curr_eval = best, best_eval
    scores = list()

    for i in range(n_itr):
        candidate = curr + randn(len(bounds)) * step_size
        candidate_eval = objective(candidate)

        if candidate_eval < best_eval:
            best, best_eval = candidate, candidate_eval
            scores.append(best_eval)
            print('>%d f(%s) = %.5f' % (i, best, best_eval))
        
        diff = candidate_eval - curr_eval
        t = temp / float(i + 1)
        metropolis = exp(-diff / t)

        if diff < 0 or rand() < metropolis:
            curr, curr_eval = candidate, candidate_eval

    return [best, best_eval, scores]

def main2():
    seed(1)
    bounds = asarray([[-5.0, 5.0]])
    n_iterations = 1000
    step_size = 1e-1
    temp = 10
    best, score, scores = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
    print('Done!')
    print('f(%s) = %f' % (best, score))

    plt.plot(scores, '.-')
    plt.xlabel('Improvement Number')
    plt.ylabel('Evaluation f(x)')
    plt.show()

if __name__ == '__main__':
    main()
    print("Leaving main, entering temp vs algo")
    temp_vs_algo()
    main2()