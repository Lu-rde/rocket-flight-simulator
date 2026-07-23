import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rocket_flight import Engine, Rocket, Simulation


def main():

    engine = Engine(
        name="Aerotech K550",
        thrust=550,
        burn_time=2.4,
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

    print(f"Net force: {simulation.net_force():.2f} N")


if __name__ == "__main__":
    main()