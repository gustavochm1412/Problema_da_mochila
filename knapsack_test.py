from genetic2020 import *
from matplotlib import pyplot as plt

def rodar_teste(pesos_e_valores, peso_maximo, n_de_cromossomos, geracoes):
    n_de_itens = len(pesos_e_valores) # Análogo aos pesos e valores

    # Execução dos procedimentos
    populacao = population(n_de_cromossomos, n_de_itens)
    historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]
    for i in range(geracoes):
        populacao = evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)
        historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

    # Prints do terminal
    print(f"Teste com peso_maximo={peso_maximo}, n_de_cromossomos={n_de_cromossomos}, geracoes={geracoes}")
    for indice, dados in enumerate(historico_de_fitness):
        print("Geracao: ", indice, " | Media de valor na mochila: ", dados)

    print("\nPeso máximo:", peso_maximo, "g\n\nItens disponíveis:")
    for indice, i in enumerate(pesos_e_valores):
        print("Item ", indice + 1, ": ", i[0], "g | R$", i[1])

    print("\nExemplos de boas solucoes: ")
    for i in range(5):
        print(populacao[i])

    # Gerador de gráfico
    plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
    plt.grid(True, zorder=0)
    plt.title("Problema da mochila")
    plt.xlabel("Geracao")
    plt.ylabel("Valor medio da mochila")
    plt.show()

# Teste 1: Peso máximo reduzido
rodar_teste([[4, 30], [8, 10], [8, 30], [25, 75], [2, 10], [50, 100], [6, 300], [12, 50], [100, 400], [8, 300]], 50, 150, 80)

# Teste 2: Número reduzido de cromossomos
rodar_teste([[4, 30], [8, 10], [8, 30], [25, 75], [2, 10], [50, 100], [6, 300], [12, 50], [100, 400], [8, 300]], 100, 50, 80)

# Teste 3: Número reduzido de gerações
rodar_teste([[4, 30], [8, 10], [8, 30], [25, 75], [2, 10], [50, 100], [6, 300], [12, 50], [100, 400], [8, 300]], 100, 150, 30)

# Teste 4: Itens de diferentes pesos e valores
rodar_teste([[3, 25], [7, 15], [9, 35], [20, 60], [1, 5], [45, 90], [5, 250], [10, 40], [95, 350], [7, 250]], 100, 150, 80)

# Teste 5: Aumento do número de itens
rodar_teste([[4, 30], [8, 10], [8, 30], [25, 75], [2, 10], [50, 100], [6, 300], [12, 50], [100, 400], [8, 300], [15, 150], [3, 20], [10, 60], [20, 200]], 100, 150, 80)

# Teste 6: Peso máximo aumentado
rodar_teste([[4, 30], [8, 10], [8, 30], [25, 75], [2, 10], [50, 100], [6, 300], [12, 50], [100, 400], [8, 300]], 200, 150, 80)
