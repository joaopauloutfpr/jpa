import matplotlib.pyplot as plt

#eixo x
meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI','JUN', 'JUL']

#eixo Y
consumo1 = [215,300,285,305,307,205,270]
consumo2 = [229,281,315,305,258,205,300]
plt.title("Gráfico de consumo de energia")

plt.plot(meses,consumo1, label="Meu consumo")
plt.plot(meses,consumo2, label="Consumo do Vizinho")
plt.legend(loc = "upper right")
plt.show()