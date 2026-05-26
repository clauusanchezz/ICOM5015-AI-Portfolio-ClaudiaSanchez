import random

class VacuumEnvironment:

    def __init__(self):

        # define spatial structure
        self.locations = ["A", "B"]

        # initialize agent location
        self.agent_location = None

        # initialize dirt distribution
        self.dirt = {}

    def initialize(self):
        """
        Randomly initialize environment state.
        """

        self.agent_location = random.choice(self.locations)

        self.dirt = {"A" : random.choice([True,False]), "B" : random.choice([True,False])}

    def get_state(self):
        """
        Return full environment state (for debugging/logging).
        """

        return {
            "agent_location":self.agent_location,
            "dirt":self.dirt
        }