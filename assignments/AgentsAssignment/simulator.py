from environment import VacuumEnvironment
from sensors import Sensors
from actuators import Actuators
from performance import PerformanceMeasure

class Simulator:

    def __init__(self, agent_program, steps=20):

        self.environment = VacuumEnvironment()
        self.sensors = Sensors()
        self.actuators = Actuators()
        self.performance = PerformanceMeasure()

        self.agent_program = agent_program
        self.steps = steps

    def run(self):

        self.environment.initialize()

        for step in range(self.steps):

            # 1 generate percept
            percept = self.sensors.get_percept(self.environment)

            # 2 agent decides action
            action = self.agent_program(percept)

            # 3 execute action
            self.actuators.execute(self.environment, action)

            # 4 update performance
            self.performance.update(self.environment, action)

        return self.performance.get_score()
