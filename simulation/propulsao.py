from typing import Any
import math

vex, vey, vez = 0.1, 0.1, 0.1
gamma = 1e-2
chi = 10
e = math.e

def propulsao(simp: Any) -> None:
    sim = simp.contents
    particles = sim.particles

    particles[2].ax += ((-vex * gamma * pow(e, (-1 * gamma) * (-sim.t))) / (chi + pow(e, (-1 * gamma) * (-sim.t))))
    particles[2].ay += ((-vey * gamma * pow(e, (-1 * gamma) * (-sim.t))) / (chi + pow(e, (-1 * gamma) * (-sim.t))))
    particles[2].az += ((-vez * gamma * pow(e, (-1 * gamma) * (-sim.t))) / (chi + pow(e, (-1 * gamma) * (-sim.t))))