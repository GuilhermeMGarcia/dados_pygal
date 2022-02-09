import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=200)

# Define o titulo do grafico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of values", fontsize=14)

# Define o tamanho dos rotulos das marcaçoes
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()