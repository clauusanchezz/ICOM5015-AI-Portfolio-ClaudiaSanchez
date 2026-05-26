import sensors


class Actuators:

    def __init__(self):

        self.ACTIONS = ["Left", "Right", "Suck", "NoOp"]

    def execute(self, environment, action):
        """
        Apply action to the environment.

        TODO:
        Implement how each action modifies the environment state.
        """

        if action == "Left":
            environment.agent_location = "A"
        elif action == "Right":
            environment.agent_location = "B"
        elif action == "Suck":
            environment.dirt[environment.agent_location] = False
        elif action == "NoOp":
            pass
