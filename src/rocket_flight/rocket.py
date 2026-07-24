import math 
from .engine import Engine

class Rocket:
    def __init__(
            self,
            name: str,
            dry_mass: float,
            diameter: float,
            length: float,
            drag_coefficient: float,
            engine: Engine,

    ) -> None:
        self.name = name 

        self.dry_mass = dry_mass

        self.diameter = diameter

        self.length = length

        self.drag_coefficient = drag_coefficient

        self.engine = engine

    @property
    def frontal_area(self) -> float:
        radius =self.diameter / 2
        return math.pi*radius**2

    @property
    def initial_mass(self):
        return (
            self.dry_mass
            + self.engine.propellant_mass
    )

    @property
    def propellant_mass(self):

        return self.engine.propellant_mass

    def summary (self) -> None:
        print(f"Rocket: {self.name}")
        print(f"Dry mass: {self.dry_mass:.2f} kg")
        print(f"Diameter: {self.diameter:.3f} m")
        print(f"Length: {self.length:.2f} m")
        print(f"Cd: {self.drag_coefficient:.2f}")
        print(f"Frontal area: {self.frontal_area:.4f} m²")
        print(f"Engine: {self.engine.name}")
        print(f"Initial mass: {self.initial_mass:.2f} kg")