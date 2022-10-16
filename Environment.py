
class Environment2D:
    _map: {}

    def __init__(self, map: set):
        self._map = map

    def __repr__(self):
        out = f"{self._map}"
        return out


class Environment:
    _map: list

    def __init__(self, _map: list):
        self._map = map

    def __repr__(self):
        out = f"{self._map}"
        return out

