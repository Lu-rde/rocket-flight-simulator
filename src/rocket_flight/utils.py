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