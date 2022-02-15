import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Cria um passeio aleatorio e plota os pontos
    rw = RandomWalk(60000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem
    plt.figure(dpi=115 ,figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)

    # Enfatiza o primeiro e o ultimo ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100)

    # Remove os eixos
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_runing = input("Make another walk? (y/n): ")
    if keep_runing == 'n':
        break
