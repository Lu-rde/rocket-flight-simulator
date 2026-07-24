class State:

    def __init__(self):

        self.time = 0.0

        self.x = 0.0
        self.y = 0.0

        self.vx = 0.0
        self.vy = 0.0

        self.ax = 0.0
        self.ay = 0.0

    @property
    def altitude(self):
        return self.y

    @altitude.setter
    def altitude(self, value):
        self.y = value

    @property
    def velocity(self):
        return self.vy

    @velocity.setter
    def velocity(self, value):
        self.vy = value

    @property
    def acceleration(self):
        return self.ay

    @acceleration.setter
    def acceleration(self, value):
        self.ay = value

    def summary (self):
        print(f"Time: {self.time:.2f} s")
        print(f"Altitude: {self.altitude:.2f} m")
        print(f"Velocity: {self.velocity:.2f} m/s")
        print(f"Acceleration: {self.acceleration:.2f} m/s²")