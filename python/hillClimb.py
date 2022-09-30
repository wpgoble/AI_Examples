# Objective function
from numpy import asarray, arange
from numpy.random import randn, rand, seed
from matplotlib import pyplot as plt

def objective(x):
    return x[0]**2.0

def plot_curve():
    r_min, r_max = -5.0, 5.0
    inputs = arange(r_min, r_max, 0.1)
    results = [objective([x]) for x in inputs]
    plt.plot(inputs, results)
    x_optima = 0.0
    plt.axvline(x = x_optima, ls='--', color = 'red')
    plt.show()

def hillClimbing(objective, bounds, n_itr, step_size):
    # generate an initial point
    solution = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    solution_eval = objective(solution)
    # Run the hill climb algorithm
    scores = list()
    scores.append(solution_eval)

    for i in range(n_itr):
        # take a step
        candidate = solution + randn(len(bounds)) * step_size
        # evaluate the candidate
        candidate_eval = objective(candidate)
        # check if we should keep the new point
        if candidate_eval <= solution_eval:
            # store the new point
            solution, solution_eval = candidate, candidate_eval
            # keep track of scores
            scores.append(solution_eval)
            # report progress
            print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
    return [solution, solution_eval, scores]

def main():
    seed(5)
    bounds = asarray([[-5.0, 5.0]])
    n_iterations = 1000
    step_size = 1e-1
    best, score, scores = hillClimbing(objective, bounds, n_iterations, step_size)
    print('Done!')
    print('f(%s) = %f' % (best, score))

    plt.plot(scores, '.-')
    plt.xlabel('Improvement Number')
    plt.ylabel('Evaluation f(x)')
    plt.show()

if __name__ == '__main__':
    plot_curve()
    #main()
