# Importando as bibliotecas usadas

import numpy as np
import matplotlib.pyplot as plt


# Declarando a classe que será utilizada para construir os gráficos necessários.
class Plotter:

    # Inicializando a classe.
    def __init__(self, sol):
        # Separando a matriz de soluções e o tempo.
        self.r = sol.y
        self.t = sol.t
        # Inserindo os títulos dos gráficos
        self.titulo = [
            "Posição do C.M. em x",
            "Velocidade do C.M. em x",
            "Posição do C.M. em y",
            "Velocidade do C.M. em y",
            "Posição do C.M. em z",
            "Velocidade do C.M. em z",
            "Posição angular θ",
            "Velocidade angular relativa à θ",
            "Posição angular ϕ",
            "Velocidade angular relativa à ϕ",
            "Posição angular ψ",
            "Velocidade angular relativa à ψ"
        ]
        # Inserindo os nomes e diretórios dos arquivos a ser salvos.
        self.arquivos = [
            f"./graficos/x.png",
            f"./graficos/x_ponto.png",
            f"./graficos/y.png",
            f"./graficos/y_ponto.png",
            f"./graficos/z.png",
            f"./graficos/z_ponto.png",
            f"./graficos/theta.png",
            f"./graficos/theta_ponto.png",
            f"./graficos/phi.png",
            f"./graficos/phi_ponto.png",
            f"./graficos/psi.png",
            f"./graficos/psi_ponto.png"
        ]
        # Inserindo o título dos eixos verticais dos gráficos. É necessário apenas 4.
        self.eixos = [
            "Posição",
            "Velocidade",
            "Posição angular",
            "Velocidade angular"
        ]

    # Definindo o método que vai construir todos os gráficos 2D.
    def plot_graficos_2d(self):
        # Esse loop percorre entre 0 e 11, construindo os gráficos em função do tempo na ordem do vetor r.
        for i in range(12):
            plt.plot(self.t, self.r[i])
            plt.title(self.titulo[i])
            plt.xlabel("Tempo [s]")
            # Esse bloco de código verifica a posição dos dados a serem construídos e associa a cada um a posição no
            # vetor de eixos.
            if i <= 5:
                if i % 2 == 0:
                    j = 0
                else:
                    j = 1
            else:
                if i % 2 == 0:
                    j = 2
                else:
                    j = 3
            plt.ylabel(self.eixos[j])
            # Salva-se a figura e limpa-se a memória para construir mais um gráfico.
            plt.savefig(self.arquivos[i], transparent=False, dpi=1000, format="png",
                        bbox_inches='tight')
            plt.clf()

    # Definindo o método que vai construir o gráfico em 3D da posição do centro de massa.
    def plot_grafico_3d(self):
        # Definindo que o modo de plot será em 3 dimensões.
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        # Construindo o gráfico:
        ax.plot(self.r[0], self.r[2], self.r[4])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_title("Posição do centro de massa do cubo")
        # Salva-se a figura.
        fig.savefig(f"./graficos/pos_CM.png", transparent=False, dpi=1000, format="png")