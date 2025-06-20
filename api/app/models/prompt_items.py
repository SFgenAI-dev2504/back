from dataclasses import dataclass


@dataclass
class PromptItems:
    diameter: int
    gravity: float
    distance: int
    temperature: int
    atmosphere: int
    water: int
    terrain: int
    volcano: int
    aurora: int
