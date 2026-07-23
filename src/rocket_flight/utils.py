import matplotlib.pyplot as plt


def plot_altitude(history):

    plt.figure(figsize=(8, 5))

    plt.plot(
        history["time"],
        history["altitude"],
    )

    plt.title("Rocket Altitude")

    plt.xlabel("Time (s)")

    plt.ylabel("Altitude (m)")

    plt.grid(True)

    plt.show()