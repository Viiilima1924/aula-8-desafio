import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_data():
    #  ler CSV file
    data1 = pd.read_csv('loj0a.csv')
   

    # Extrair data
    item = data1['produto']
    quantidade = data1['itensvendidos']


    # # Criar a figura
    fig, grafico = plt.subplots()
    grafico.plot(item, quantidade, marker='o', linestyle='-', color='b')

    # # add as labels
    grafico.set_xlabel('item')
    grafico.set_ylabel('quantidade')
    grafico.set_title('quantidade de produtos vendidos')

    # # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# janela tkinter
janela = tk.Tk()
janela.title('Qual foi o produto mais vendido?')

# button
botao = tk.Button(janela, text='Exibir Gráfico', command=plot_data)
botao.pack(pady=20)

# loop tkinter
janela.mainloop()
