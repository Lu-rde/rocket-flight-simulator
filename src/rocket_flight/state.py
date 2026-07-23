class State:

    def __init__(self):
        self.time=0.0
        self.altitude=0.0
        self.velocity=0.0
        self.acceleration=0.0

    def summary (self):
        print(f"Time: {self.time:.2f} s")
        print(f"Altitude: {self.altitude:.2f} m")
        print(f"Velocity: {self.velocity:.2f} m/s")
        print(f"Acceleration: {self.acceleration:.2f} m/s²")