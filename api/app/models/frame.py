import random
from enum import Enum


class Frame(Enum):
    RED = "frame_red.png"
    BLUE = "frame_blue.png"
    YELLOW = "frame_yellow.png"

    @classmethod
    def select_frame(cls):
        values = [i.value for i in cls]
        random.shuffle(values)
        return values[0]
