import random
from enum import Enum


class Frame(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

    @classmethod
    def select_frame(cls):
        values = [i for i in cls]
        random.shuffle(values)
        return values[0]

    def get_file_name(self):
        if self.value == 1:
            color = "red"
        elif self.value == 2:
            color = "blue"
        elif self.value == 3:
            color = "yellow"
        else:
            raise RuntimeError
        return f"frame_{color}.png"

    def get_shadow_color(self):
        if self.value == 1:
            color = (255, 0, 0, 255)
        elif self.value == 2:
            color = (0, 0, 255, 255)
        elif self.value == 3:
            color = (255, 255, 0, 255)
        else:
            raise RuntimeError
        return color
