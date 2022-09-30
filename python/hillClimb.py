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

# hill climbing local search algorithm
def hillclimbing(objective, bounds, n_iterations, step_size):
	# generate an initial point
	solution = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# evaluate the initial point
	solution_eval = objective(solution)
	# run the hill climb
	solutions = list()
	solutions.append(solution)
	for i in range(n_iterations):
		# take a step
		candidate = solution + randn(len(bounds)) * step_size
		# evaluate candidate point
		candidte_eval = objective(candidate)
		# check if we should keep the new point
		if candidte_eval <= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidte_eval
			# keep track of solutions
			solutions.append(solution)
			# report progress
			print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
	return [solution, solution_eval, solutions]

def main():
    seed(5)
    bounds = asarray([[-5.0, 5.0]])
    n_iterations = 1000
    step_size = 1e-1
    best, score, scores = hillclimbing(objective, bounds, n_iterations, step_size)
    print('Done!')
    print('f(%s) = %f' % (best, score))

    plt.plot(scores, '.-')
    plt.xlabel('Improvement Number')
    plt.ylabel('Evaluation f(x)')
    plt.show()

def main2():
    seed(5)
    bounds = asarray([[-5.0, 5.0]])
    n_iterations = 1000
    step_size = 1e-1
    best, score, solutions = hillclimbing(objective, bounds, n_iterations, step_size)
    print('Done!')
    print('f(%s) = %f' % (best, score))
    
    # sample input range uniformly at 0.1 increments
    inputs = arange(bounds[0,0], bounds[0,1], 0.1)
    # create a line plot of input vs result
    plt.plot(inputs, [objective([x]) for x in inputs], '--')
    # draw a vertical line at the optimal input
    plt.axvline(x=[0.0], ls='--', color='red')
    # plot the sample as black circles
    plt.plot(solutions, [objective(x) for x in solutions], 'o', color='black')
    plt.show()

if __name__ == '__main__':
    #plot_curve()
    #main()
    main2()
