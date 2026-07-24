from atmospheric_model import Atmosphere

from . import constants
from .forces import drag, weight
from .state import State

class Simulation:
    def __init__(self, rocket):
        self.rocket = rocket
        self.state = State ()
        self.dt = 0.1
        
        self.history = {
            "time": [],
            "altitude": [],
            "velocity": [],
            "acceleration": [],
        }


    def net_force(self):
        atmosphere = Atmosphere (self.state.altitude)
        thrust = self.thrust()

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

        if self.state.altitude < 0:

            self.state.altitude = 0

            self.state.velocity = 0

        self.history["time"].append(self.state.time)

        self.history["altitude"].append(self.state.altitude)

        self.history["velocity"].append(self.state.velocity)

        self.history["acceleration"].append(self.state.acceleration)

    def run(self, duration):
        while self.state.time < duration:
            
            self.step()

            self.state.summary()

            print("-" * 35)

    def thrust(self):

        if self.state.time <= self.rocket.engine.burn_time:
            return self.rocket.engine.thrust

        return 0.0

    def summary(self):

        print("\nFlight Summary")
        print("=" * 35)

        print(f"Maximum altitude: {max(self.history['altitude']):.2f} m")

        print(f"Maximum velocity: {max(self.history['velocity']):.2f} m/s")

        print(

            f"Maximum acceleration: "
            f"{max(self.history['acceleration']):.2f} m/s²"
        )

        index = self.history["altitude"].index(

            max(self.history["altitude"])
        )

        print(
            f"Time to apogee: "
            "{self.history['time'][index]:.2f} s"
        )