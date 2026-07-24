class Engine: 
    def __init__(
            self,
            name:str,
            thrust:float,
            burn_time:float,
            propellant_mass: float,
    ) -> None:
        self.name=name

        self.thrust=thrust

        self.burn_time=burn_time

        self.propellant_mass = propellant_mass

    @property

    def mass_flow_rate(self) -> float:
        """
        Propellant consumption rate (kg/s).
        """
        return self.propellant_mass / self.burn_time

    def thrust_at_time(self, time: float) -> float:
         """
         Returns the engine thrust at a given time.
         """

         if time >= self.burn_time:
              return 0.0

         progress = time / self.burn_time

         if progress < 0.15:
              return self.thrust * (
                   0.8 + progress / 0.15 * 0.2
            )

         if progress < 0.80:
              return self.thrust

         decay = (
              (progress - 0.80) / 0.20
        )

         return self.thrust * (1.0 - decay)

    def summary(self):
            print(f"Engine: {self.name}")
            print(f"Thrust: {self.thrust:.1f} N")
            print(f"Burn time: {self.burn_time:.2f} s")
            print(f"Propellant: {self.propellant_mass:.2f} kg")
            print(f"Mass flow: {self.mass_flow_rate:.2f} kg/s")