# Importando as bibliotecas usadas
import scipy.integrate as sp
import numpy as np
from params_e_CIs import parametros
from params_e_CIs import cond_iniciais
from modelo import modelo
from modelo import parametros_oscilatorios
from plotter import Plotter

# Criando pontos (instantes de tempo) nos quais os valores são armazenados.
dt = 0.0001
t_eval = np.arange(0, parametros["tf"], dt)

# Usando scipy.integrate.solve_ivp para resolver o conjunto de equações utilizando Runge-Kutta de quarta/quinta ordem.
sol = sp.solve_ivp(modelo, (0, parametros["tf"]), cond_iniciais, args=(parametros,),
                   t_eval=t_eval, atol=1e-12, rtol=1e-10)

# Instanciando a classe que será usada para construir os gráficos.
plot = Plotter(sol)
plot.plot_graficos_2d()
plot.plot_grafico_3d()

# Usando os parâmetros físicos, tiramos os parâmetros oscilatórios do sistema.
param_osci = parametros_oscilatorios(parametros)

# Escrevemos os parâmetros oscilatórios no console.
for i in range(6):
    print("Frequência de ressonância " + str(i) + ": " + str(param_osci[0][i]))
    print("Modo vibracional " + str(i) + ": " + str(param_osci[1][i]))
