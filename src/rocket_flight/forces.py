from . import constants

def weight(mass:float)->float:
    return mass*constants.GRAVITY

def drag(
        density:float,
        velocity:float,
        drag_coefficient:float,
        area:float,
) -> float:

    return (
        0.5
        *density
        *velocity**2
        *drag_coefficient
        *area
    )