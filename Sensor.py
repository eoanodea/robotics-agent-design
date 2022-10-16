from tkinter import Image


class Sonar:
    _value: Image

    def __init__(self, value: Image):
        self._value = value

    def __repr__(self):
        out = f"{self._value}"
        return out


class Camera:
    _value: Image

    def __init__(self, value: Image):
        self._value = value

    def __repr__(self):
        out = f"{self._value}"
        return out


class Sensor:
    _value: any

    def __init__(self, value: any):
        self._value = value

    def __repr__(self):
        out = f"{self._value}"
        return out
