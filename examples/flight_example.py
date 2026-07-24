import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rocket_flight import (
    Engine,
    Rocket,
    Simulation,
    plot_altitude,
    plot_velocity,
    plot_acceleration,
    export_csv,
)


def main():

   engine = Engine(
      name="Aerotech K550",
      thrust=550,
      burn_time=2.4,
      propellant_mass=3.0,
    )
   rocket = Rocket(
        name="Demo Rocket",
        dry_mass=18.5,
        diameter=0.15,
        length=2.1,
        drag_coefficient=0.55,
        engine=engine,
    )

   simulation = Simulation(rocket)

   simulation.run(20)

   simulation.summary()

   plot_altitude(simulation.history)

   plot_velocity(simulation.history)

   plot_acceleration(simulation.history)

   export_csv(simulation.history)



if __name__ == "__main__":
    main()