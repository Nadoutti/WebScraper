import matplotlib.pyplot as plt
import pandas as pd

# df = pd.DataFrame('dados.csv')

# funcao para grafico de barras de uma unica moeda
def bars():
    datas = [1, 2, 3, 4, 5 ,6, 7, 8]
    valores = [5, 7, 8, 7, 8, 8, 11, 30]
    plt.figure(figsize=(7, 7))
    plt.bar(datas, valores)
    plt.title("Cotacao de dolar ao longo do tempo x")
    plt.xlabel("Linha do tempo")
    plt.ylabel("Valores em $")
    plt.show()

bars()
