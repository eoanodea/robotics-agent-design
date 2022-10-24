"""
    Implementation of the Body class of the Agent
"""
import logging


class Body:
    _sensors: set
    _actuators: set
    _perceptions: set
    _name: str

    def __init__(self, name, sens_array, act_array):
        logging.info(f"Agent name: {name} initialized")
        self._name = name
        self._sensors = sens_array
        self._actuators = act_array

    def __repr__(self):
        out = f"I have {len(self._sensors)} sensors and {len(self._actuators)} actuators"
        return out

    def perceive(self, stimuli):
        # transform stimuli from sensors into perceptions
        for s in stimuli:
            self._perceptions.add(...)
        pass

    def step(self, t: int):
        # called by simulator at each simulation step
        logging.info(f"{self._name}: agent body step at time {t}")
        stimuli = [s.get_value() for s in self._sensors]
        logging.info(f"{self._name}: stimuli at time {t} -> {stimuli}")
        self.perceive(stimuli)
        logging.info(f"{self._name}: perceptions at time {t} -> {self._perceptions}")
        # TODO add commands here

    def get_perceptions(self):
        return self._perceptions
