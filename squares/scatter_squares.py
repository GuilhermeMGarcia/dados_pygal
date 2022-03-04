import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# Define o titulo do grafico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of values", fontsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

# Define o tamanho dos rotulos das marcaçoes
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')