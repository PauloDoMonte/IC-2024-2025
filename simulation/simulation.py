import rebound
import csv
import numpy as np
import pandas as pd
import os
from typing import Any
from .particula import Particula
from .propulsao import propulsao

def create_simulation(sol: Particula, terra: Particula) -> rebound.Simulation:
    sim = rebound.Simulation()
    sim.units = ("kg", "km", "s")
    sim.integrator = "IAS15"
    sim.additional_forces = propulsao
    sim.force_is_velocity_dependent = False

    sim.add(m=sol.m, r=sol.r)
    sim.add(m=terra.m, r=terra.r, a=terra.a, e=terra.e, inc=terra.inc, omega=terra.omega, Omega=terra.Omega, f=terra.f * 0.0174533)
    
    # Parâmetros para uma órbita MEO
    meo_altitude = 20000  # Altitude de MEO em km
    meo_radius = terra.r + meo_altitude  # Raio da órbita MEO a partir do centro da Terra
    meo_velocity = np.sqrt(sim.G * terra.m / meo_radius)  # Velocidade orbital
    
    # Coordenadas da Terra
    x_terra = sim.particles[1].x
    y_terra = sim.particles[1].y
    z_terra = sim.particles[1].z
    vx_terra = sim.particles[1].vx
    vy_terra = sim.particles[1].vy
    vz_terra = sim.particles[1].vz
    
    # Adicionar a partícula em órbita MEO ao redor da Terra
    sim.add(m=1000, r=0.01, 
            x=x_terra + meo_radius, y=y_terra, z=z_terra, 
            vx=vx_terra, vy=vy_terra + meo_velocity, vz=vz_terra)

    return sim

def run_simulation(sim: rebound.Simulation, csv_file_path: str, tempo_maximo: float, tamanho: int) -> None:
    # Apagar o arquivo CSV antigo se existir
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)

    times = np.linspace(0, tempo_maximo, tamanho)
    distancias = pd.DataFrame(columns=["time", "x_sat", "y_sat", "z_sat", "x_terra", "y_terra", "z_terra"])

    for u, time in enumerate(times):
        sim.move_to_com()
        sim.integrate(time)

        x_sat = sim.particles[2].x
        y_sat = sim.particles[2].y
        z_sat = sim.particles[2].z

        x_terra = sim.particles[1].x
        y_terra = sim.particles[1].y
        z_terra = sim.particles[1].z

        new_row = pd.DataFrame([{
            "time": time,
            "x_sat": x_sat,
            "y_sat": y_sat,
            "z_sat": z_sat,
            "x_terra": x_terra,
            "y_terra": y_terra,
            "z_terra": z_terra
        }])

        if new_row.empty:
            print("DEU RUIM")
            print(new_row)

        if not new_row.empty:
            distancias = pd.concat([distancias, new_row], ignore_index=True)


        if len(distancias) > 100:
            distancias.to_csv(csv_file_path, sep=",", header=False, mode='a', index=False)
            distancias = pd.DataFrame(columns=["time", "x_sat", "y_sat", "z_sat", "x_terra", "y_terra", "z_terra"])

            print(f"Progress: {u+1}/{len(times)}")

    # Save any remaining data
    if not distancias.empty:
        distancias.to_csv(csv_file_path, sep=",", header=False, mode='a', index=False)