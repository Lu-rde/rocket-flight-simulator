from pathlib import Path
import csv


def export_csv(history):
    """
    Exports the flight history to a CSV file.
    """

    output_dir = Path(__file__).resolve().parents[2] / "results"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "flight_data.csv"

    with open(output_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Time (s)",
            "Altitude (m)",
            "Velocity (m/s)",
            "Acceleration (m/s²)",
        ])

        for row in zip(
            history["time"],
            history["altitude"],
            history["velocity"],
            history["acceleration"],
        ):
            writer.writerow(row)

    print(f"CSV exported to: {output_file}")