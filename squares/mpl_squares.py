import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]
plt.plot(input_values, square, linewidth=5)

# Define o titulo do grafico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of values", fontsize=14)

# Define o tamanho dos rotulos das marcaçoes
plt.tick_params(axis='both', labelsize=14)

plt.show()

