class Particula:
    def __init__(self, nome: str, massa: float, raio: float, a: float, e: float, inc: float, omega: float, Omega: float, f: float) -> None:
        self.nome = nome
        self.m = massa
        self.r = raio
        self.a = a
        self.e = e
        self.inc = inc * 0.0174533
        self.omega = omega * 0.0174533    # argumento do perigeu
        self.Omega = Omega * 0.0174533    # Longitude do no ascendente
        self.f = f * 0.0174533