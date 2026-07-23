class Engine: 
    def __init__(
            self,
            name:str,
            thrust:float,
            burn_time:float,
    ) -> None:
        self.name=name

        self.thrust=thrust

        self.burn_time=burn_time

    def summary(self):
        print(f"Engine: {self.name}")
        print(f"Thrust: {self.thrust:.1f} N")
        print(f"Burn time: {self.burn_time:.2f} s")