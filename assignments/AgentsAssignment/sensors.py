class Sensors:

    def get_percept(self, environment):
        """
        Generate percept for the agent.
        """

        agent_location = environment.agent_location
        dirt_status = environment.dirt[agent_location]

        return agent_location, dirt_status
