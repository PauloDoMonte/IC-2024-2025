import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_simulation_data(csv_file_path: str) -> None:
    # Ler os dados do arquivo CSV
    data = pd.read_csv(csv_file_path, header=None, names=["time", "x_sat", "y_sat", "z_sat", "x_terra", "y_terra", "z_terra"])

    # Calcular a distância entre o satélite e a Terra
    data["distance"] = np.sqrt((data["x_sat"] - data["x_terra"])**2 + 
                               (data["y_sat"] - data["y_terra"])**2 + 
                               (data["z_sat"] - data["z_terra"])**2)

    # Plotar a distância ao longo do tempo
    plt.figure(figsize=(10, 6))
    plt.plot(data["time"], data["distance"], label="Distance")
    plt.xlabel("Time (days)")
    plt.ylabel("Distance (km)")
    plt.title("Distance Between Satellite and Earth Over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("data/satellite_earth_distance.png")
    plt.show()

if __name__ == "__main__":
    plot_simulation_data("data/simulation_data.csv")