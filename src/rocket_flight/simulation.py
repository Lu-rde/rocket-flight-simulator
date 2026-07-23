from atmospheric_model import Atmosphere

from . import constants
from .forces import drag, weight
from .state import State

class Simulation:
    def __init__(self, rocket):
        self.rocket = rocket
        self.state = State ()

        self.dt = 0.1

    def net_force(self):
        atmosphere = Atmosphere (self.state.altitude)
        thrust = self.rocket.engine.thrust

        drag_force=drag (
            atmosphere.density,
            self.state.velocity,
            self.rocket.drag_coefficient,
            self.rocket.frontal_area,
        )

        weight_force = weight (self.rocket.dry_mass)
        
        return thrust - drag_force - weight_force

    def acceleration(self):

        return self.net_force() / self.rocket.dry_mass

    def step(self):
        self.state.acceleration = self.acceleration()

        self.state.velocity += (
            self.state.acceleration * self.dt
        )

        self.state.altitude += (
        self.state.velocity * self.dt
        )

        self.state.time += self.dt

    def run(self, duration):
        while self.state.time < duration:
            
            self.step()

            self.state.summary()

            print("-" * 35)