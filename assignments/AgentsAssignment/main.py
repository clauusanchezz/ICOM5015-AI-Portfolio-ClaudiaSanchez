from statistics import mean

from agents import *
from simulator import Simulator

if __name__ == "__main__":

    def run_experiment(agent_program,trials=100):
        scores = []

        for trial in range(trials):
            simulator = Simulator(agent_program)
            score = simulator.run()
            scores.append(score)

        return mean(scores)

    reflex_score = run_experiment(reflex_agent)
    random_score = run_experiment(random_agent)
    truerandom_score = run_experiment(truerandom_agent)

    print("Reflex Agent Average Score:", reflex_score)
    print("Random Agent Average Score:", random_score)
    print("True Random Agent Average Score:", truerandom_score)