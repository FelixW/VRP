import csv
import itertools
import numpy as np

from model import VRP



run_name = 'heuristic_test'

''' HYPERPARAMETERS'''

test_heuristic = {
    'scenario': [1, 2],
    'heuristic': [False, True],
    'pop_size': [12],
    'selection_size': [2],
    'aco_iterations': [10],
    'beta': [1],
    'evap_rate': [.1],
    'beta_evap': [0],
    'crossover_prob': [0.05, 0.2],
    'mutation_prob': [0.05, 0.1],
    'reduce_clusters': [0],
    'kmeans_iterations': [10],
    'squared_dist': [True],
    'time_limit': [600]
}

test_other = {
    'scenario': [1, 2],
    'heuristic': [True],
    'pop_size': [10, 14],
    'selection_size': [2, 4],
    'aco_iterations': [15, 25],
    'crossover_prob': [0.1, 0.2],
    'mutation_prob': [0.05, 0.1],
    'reduce_clusters': [0, 4],
    'kmeans_iterations': [10, 20]
}

def gridsearch(dict):

    # creating cartesian product of the dictionary as 2D-list
    iteration = []
    for i, entry in enumerate(dict):
        values = []
        for value in dict[entry]:
            values.append(value)
        iteration.append(values)

    # init saving-lists
    best = []
    mean = []

    # deploying all permutations
    print('All permutations of test-parameters:')
    nr_of_perms = 0
    with open('./results/' + run_name + '_params.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for v in (itertools.product(*iteration)):
            print(v)
            writer.writerow(v)
            nr_of_perms += 1

    count = 0
    for v in (itertools.product(*iteration)):
        count += 1
        print('Test', count, 'of', nr_of_perms, ':')
        print('scenario:', v[0], 'heuristic:', v[1], 'pop_size:', v[2], 'selection_size:', v[3], 'aco_iterations:', v[4], 'beta:', v[5], 'evap_rate:', v[6], 'beta_evap:', v[7], 'crossover_prob:', v[8], 'mutation_prob:', v[9], 'reduce_clusters:', v[10], 'kmeans_iterations:', v[11], 'squared_dist:', v[12], 'time_limit:', v[13])
        best_run, mean_run = VRP(scenario=v[0], heuristic=v[1], pop_size=v[2], selection_size=v[3], aco_iterations=v[4], beta=v[5], evap_rate=v[6], beta_evap=v[7], crossover_prob=v[8], mutation_prob=v[9], reduce_clusters=v[10], kmeans_iterations=v[11], squared_dist=v[12], time_limit=v[13])

        # saving results
        best.append(best_run)
        mean.append(mean_run)

    # persisting
    print('Endresults for best:')
    with open('./results/' + run_name + '_best.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for i in best:
            print(i)
            writer.writerow(i)
    print('Endresults for mean:')
    with open('./results/' + run_name + '_mean.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for i in mean:
            print(i)
            writer.writerow(i)

if __name__ == '__main__':
    gridsearch(test_heuristic)