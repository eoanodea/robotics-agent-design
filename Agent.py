
class KnowledgeBase:
    _database: str

    def __init__(self, database: str):
        self._database = database

    def __repr__(self):
        out = f"{self._database}"
        return out


class Goal:
    _current_goal: str

    def __init__(self, current_goal: str):
        self._current_goal = current_goal

    def __repr__(self):
        out = f"{self._current_goal}"
        return out


class Ability:
    _name: str

    def __init__(self, name: str):
        self._name = name

    def __repr__(self):
        out = f"{self._name}"
        return out


class Agent:
    _abilities: set(Ability)
    _goals: set(Goal)
    _knowledgebase: KnowledgeBase

    def __init__(self, abilities: set, goals: set, knowledgebase: KnowledgeBase):
        self._abilities = abilities
        self._goals = goals
        self._knowledgebase = knowledgebase

    def __repr__(self):
        out = f"{self._abilities} {self._goals}"
        return out
