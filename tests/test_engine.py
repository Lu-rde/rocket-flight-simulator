import sys
from pathlib import Path 

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rocket_flight import Engine

def test_engine_creation():
    engine=Engine(
        name="Test Engine",
        thrust=500,
        burn_time=3.5,
    )

    assert engine.name=="Test Engine"
    assert engine.thrust==500
    assert engine.burn_time==3.5
