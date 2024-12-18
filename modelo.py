# Importando as bibliotecas usadas
import numpy as np
import scipy.linalg as linalg


# Definindo a função que exporta as equações diferenciais. Ela recebe o tempo t, o vetor r e o dicionário de parâmetros.
def modelo(t, r, params):
    # Associando os valores de r em variáveis.
    x, x_ponto, y, y_ponto, z, z_ponto, theta, theta_ponto, phi, phi_ponto, psi, psi_ponto = r
    # Associando os parâmetros a partir do dicionário.
    kx = params["Kx"]
    ky = params["Ky"]
    kz = params["Kz"]
    m = params["m"]
    a = params["a"]
    # Sabendo que a forma é um cubo, temos o momento de inércia i.
    i = (m * a ** 2) / 6

    # Declarando as equações diferenciais.
    dx = x_ponto
    dx_ponto = (kx / m) * (a * theta - x)
    dy = y_ponto
    dy_ponto = (ky / m) * (a * phi - y)
    dz = z_ponto
    dz_ponto = - (kz / m) * z
    dtheta = theta_ponto
    dtheta_ponto = (a / i) * (kx * x - (kx + kz) * a * theta)
    dphi = phi_ponto
    dphi_ponto = (a / i) * (ky * y - (ky + kz) * a * phi)
    dpsi = psi_ponto
    dpsi_ponto = - ((a ** 2) / i) * (kx + ky) * psi

    # Retorna as equações diferenciais.
    return [dx, dx_ponto, dy, dy_ponto, dz, dz_ponto, dtheta, dtheta_ponto, dphi, dphi_ponto, dpsi, dpsi_ponto]


# Definindo a função que soluciona o problema de autovalor e autovetor da equação matricial para encontrar os parâmetros
# de oscilação.
def parametros_oscilatorios(params):
    # Associando os parâmetros a partir do dicionário.
    kx = params["Kx"]
    ky = params["Ky"]
    kz = params["Kz"]
    m = params["m"]
    a = params["a"]
    # Definindo o momento de inécia i do cubo.
    i = (m * a ** 2) / 6
    # Montando as matrizes a partir da equação matricial.
    M = np.array([
        [m, 0, 0, 0, 0, 0],
        [0, m, 0, 0, 0, 0],
        [0, 0, m, 0, 0, 0],
        [0, 0, 0, i, 0, 0],
        [0, 0, 0, 0, i, 0],
        [0, 0, 0, 0, 0, i]
    ])
    K = np.array([
        [kx, 0, 0, - a * kx, 0, 0],
        [0, ky, 0, 0, - a * ky, 0],
        [0, 0, kz, 0, 0, 0],
        [- a * ky, 0, 0, (a ** 2) * (kx + kz), 0, 0],
        [0, - a * ky, 0, 0, (a ** 2) * (ky + kz), 0],
        [0, 0, 0, 0, 0, (a ** 2) * (kx + ky)]
    ])
    # Invertendo a matriz de massa/inércia.
    M_inv = linalg.inv(M)
    # Multiplicando o inverso de M com K.
    MK = np.matmul(M_inv, K)
    # A partir dessa matriz MK, temos que os quadrados das frequências de ressonância e os modos vibracionais
    # são os autovalores e os autovetores, respectivamente.
    w2, modos_vib = linalg.eig(MK)

    # Calcula-se os valores de w:
    w = []
    for x in w2:
        w.append(np.sqrt(np.absolute(x)))

    # Retorna-se dois vetores: as frequências naturais e os modos vibracionais.
    return [w, modos_vib]
