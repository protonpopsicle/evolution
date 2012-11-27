from random import randint

SEQ_LEN = 5
SEQ_MAX = 100
POP_SIZE = 4

def rand_sequence():
    return [randint(0, SEQ_MAX) for i in range(0, SEQ_LEN)]

def mutate(sequence):
    rand_index= randint(0, SEQ_LEN - 1)
    sequence[rand_index] = randint(0, SEQ_MAX)
    return sequence

def one_point_xover(father, mother, mutation_fn):
    xover_point = randint(0, SEQ_LEN - 1)
    sequence = mother[:xover_point] + father[xover_point:]
    return mutation_fn(sequence)

def offspring(mother, father, xover_fn):
    return xover_fn(father, mother, mutate)

def eval_divisible_by_10_fitness(sequence):
    return sum([x % 10 == 0 for x in sequence])

def eval_sum_fitness(sequence):
    return reduce(lambda x, y: x + y, sequence)

def lifecycle(population):
    sorted_population = sorted(population, key=eval_divisible_by_10_fitness, reverse=True)
    print sorted_population
    raw_input()

    mother, father = sorted_population[0], sorted_population[1]
    new_population = [offspring(mother, father, one_point_xover) for i in range(0, SEQ_LEN - 1)]
    return lifecycle(new_population + [mother])

population = [rand_sequence() for i in range(0, POP_SIZE)]
lifecycle(population)
