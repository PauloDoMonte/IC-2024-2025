from simulation.particula import Particula
from simulation.simulation import create_simulation, run_simulation
from plot_simulation import plot_simulation_data

def main() -> None:
    sol = Particula('sol', 1.989e+30, 696340, 0, 0, 0, 0, 0, 0)
    terra = Particula('terra', 5.973332e+24, 6378.1366, 149.60e6, 0.01671022, 0.00005, -11.26064, 102.94719, 0)

    sim = create_simulation(sol, terra)
    run_simulation(sim, 'data/simulation_data.csv', tempo_maximo=2592000, tamanho=86400)
    
    # Chamar o script de plotagem após a simulação
    plot_simulation_data('data/simulation_data.csv')

if __name__ == "__main__":
    main()