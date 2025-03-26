import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from db_conn import connect_db

connection = connect_db()

df = pd.read_sql('SELECT * FROM dados', connection)

# funcao para grafico de barras de uma unica moeda
def bars(tempo=30):
    datas = df['DIA_COTACAO'][tempo]
    valores = df['valor_cotacao'][tempo]  
    plt.figure(figsize=(7, 7))
    plt.bar(datas, valores)
    plt.title("Cotacao de dolar ao longo do tempo x")
    plt.xlabel("Linha do tempo")
    plt.ylabel("Valores em $")
    plt.show()


def media(tempo=30):
    valores = df['valores'][tempo]
    valores_filtrados = []
    
    # adicionando valores numa lista
    [valores_filtrados.append(valor) for valor in valores]
    
    media = np.mean(valores_filtrados)

    return media
    

