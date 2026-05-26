import random
from actuators import Actuators

def reflex_agent(percept):
    """
    Deterministic reflex agent.

    """

    location, status = percept
    if status:
        return "Suck"

    if location == "A":
        return "Right"
    if location == "B":
        return "Left"

    return "NoOp"

def random_agent(percept):
    location, status = percept
    """
    Random agent that perceives location and status.
    """
    if status:
        return "Suck"

    return random.choice(Actuators().ACTIONS)

def truerandom_agent(percept):
    """
    Deterministic truerandom agent.
    """
    return random.choice(Actuators().ACTIONS)