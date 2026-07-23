from atmospheric_model import Atmosphere

from . import constants
from .forces import drag, weight
from .state import State

class Simulation:
    def __init__(self, rocket):
        self.rocket = rocket
        self.state = State ()

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