from pathlib import Path
import matplotlib.pyplot as plt


def plot_altitude(history):

    plt.figure(figsize=(8, 5))

    plt.plot(
        history["time"],
        history["altitude"],
        linewidth=2,
    )

    plt.title("Rocket Altitude")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.grid(True)

    images_dir = Path(__file__).resolve().parents[2] / "images"
    images_dir.mkdir(exist_ok=True)

    output_file = images_dir / "altitude_profile.png"

    plt.savefig(output_file, dpi=300, bbox_inches="tight")

    print(f"Figure saved to: {output_file}")

    plt.show()

    plt.close()

def plot_velocity(history):

    plt.figure(figsize=(8,5))

    plt.plot(
        history["time"],
        history["velocity"],
        linewidth=2,
    )

    plt.title("Rocket Velocity")

    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.grid(True)

    images_dir = Path(__file__).resolve().parents[2] / "images"
    output = images_dir / "velocity_profile.png"

    plt.savefig(output, dpi=300, bbox_inches="tight")

    plt.show()
    plt.close()

def plot_acceleration(history):

    plt.figure(figsize=(8,5))

    plt.plot(
        history["time"],
        history["acceleration"],
        linewidth=2,
    )

    plt.title("Rocket Acceleration")

    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s²)")
    plt.grid(True)

    images_dir = Path(__file__).resolve().parents[2] / "images"
    output = images_dir / "acceleration_profile.png"

    plt.savefig(output, dpi=300, bbox_inches="tight")

    plt.show()
    plt.close()

