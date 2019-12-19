#!/usr/bin/env python3
from generate_non_stillborn import generate_non_stillborn
import os

class evolver:
    def __init__(self, mars, population_dir, population_seed=None):
        self.mars = mars
        self.population_dir = population_dir
        self.params = {"popsize": 1000, "elitesize": 10, "numrounds": 1000}
        self.population = population_seed
        self.random_repopulation()
    
    def random_repopulation(self):
        i = 0
        while len(self.population) < self.params["popsize"]:
            while os.path.isfile(os.path.join(self.population_dir, str(i))):
                i += 1
            warrior_name = os.path.join(self.population_dir, str(i))
            generate_non_stillborn(warrior_name, self.mars)
            self.population.append(warrior_name)

    def _run_round(self):
        pass
        # precondition we have popsize in the population
        # first assign fitness to each individual
        # assign elitesize as elites, which both presist and reproduce
        # then make weighted choice of parents and crossover
        # do this until we have popsize new or elites
        # clean up and return

    def evolve(self):
        for i in range(self.params['numrounds']):
            fitness = self._run_round()
            print("Ran round %d, with average fitness %s" % (i, str(fitness))) 
