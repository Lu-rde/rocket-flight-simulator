import math 
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rocket_flight import Rocket, Engine

def test_rocket_creation ():

    engine= Engine (
        name="Test",
        thrust=500,
        burn_time=3,
    )

    rocket=Rocket(
        name="Rocket",
        dry_mass=20,
        diameter=0.20,
        length=2.5,
        drag_coefficient=0.50,
        engine=engine,
    )

    assert rocket.name == "Rocket"
    assert rocket.dry_mass == 20
    assert rocket.diameter == 0.20
    assert rocket.length == 2.5
    assert rocket.drag_coefficient == 0.50

def test_frontal_area():

    engine=Engine(
        name="Test",
        thrust=500,
        burn_time=3,
    )

    rocket=Rocket(
        name="Rocket",
        dry_mass=20,
        diameter=0.20,
        length=2.5,
        drag_coefficient=0.50,
        engine=engine,
    )

    expected = math.pi * (0.10 ** 2)

    assert abs(rocket.frontal_area - expected) < 1e-8