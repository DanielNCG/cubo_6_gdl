# Declarando um dicionário para guardar os valores para os parâmetros utilizados na simulação.
parametros = {
    "Kx": 1,   # Constante de elasticidade equivalente na direção x [N/m]
    "Ky": 1,   # Constante de elasticidade equivalente na direção y [N/m]
    "Kz": 5,   # Constante de elasticidade equivalente na direção z [N/m]
    "m": 20,    # Massa total do cubo [kg]
    "a": 1,    # Comprimento da aresta do cubo [m]
    "tf": 180  # Instante final de tempo da simulação [s]
}

# Declarando um vetor para guardar os valores para as condições iniciais da simulação.
cond_iniciais = [
    1,  # posição inicial em x [m]
    0,  # velocidade inicial em x [m/s]
    1,  # posição inicial em y [m]
    0,  # velocidade inicial em y [m/s]
    1,  # posição inicial em z [m]
    0,  # velocidade inicial em z [m/s]
    0,  # posição angular inicial em θ [rad]
    0,  # velocidade angular inicial em θ [rad/s]
    0,  # posição angular inicial em ϕ [rad]
    0,  # velocidade angular inicial em ϕ [rad/s]
    0.015,  # posição angular inicial em ψ [rad]
    0   # velocidade angular inicial em ψ [rad/s]
]
