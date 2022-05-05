# Imports
from tkinter import *
import numpy as np
from tkcalendar import DateEntry
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

'''
Funzione per visualizzare le azioni
usando la formattazione a candela
'''
def visualize():
    
    # Logo 
    plt.Figure()
    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_iconbitmap("icon.ico")
    
    # Prendo in input i dati sulle date e li converto
    from_date = cal_from.get_date()
    to_date = cal_to.get_date()

    start = dt.datetime(from_date.year, from_date.month, from_date.day)
    end = dt.datetime(to_date.year, to_date.month, to_date.day)

    # Leggo il ticker e scarico i dati
    ticker = text_ticker.get()
    data = web.DataReader(ticker, 'yahoo', start, end)

    # Ricreo i dati nel Formato OHLC
    data = data[['Open', 'High', 'Low', 'Close']]

    # Resetto e converto i dati in numeri
    data.reset_index(inplace=True)
    data['Date'] = data['Date'].map(mdates.date2num)

    # Stile del plot
    ax = plt.subplot()
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_title('{} Share Price'.format(ticker), color='white')
    ax.figure.canvas.set_window_title('Stock tracker')
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.xaxis_date()

    # Creo il grafico a candela
    candlestick_ohlc(ax, data.values, width=0.5, colorup='#00ff00')
    
    plt.show()

# Definisco la finestra
root = Tk()
root.title("Stock tracker Menu")
root.iconbitmap("icon.ico")

# Aggiungo le componenti
label_from = Label(root, text="From:")
label_from.pack()
cal_from = DateEntry(root, width=50, year=2019, month=1, day=1)
cal_from.pack(padx=10, pady=10)

label_to = Label(root, text="To:")
label_to.pack()
cal_to = DateEntry(root, width=50)
cal_to.pack(padx=10, pady=10)

label_ticker = Label(root, text="Simbolo Azienda:")
label_ticker.pack()
text_ticker = Entry(root)
text_ticker.pack()

btn_visualize = Button(root, text="Visualizza Grafico", command=visualize)
btn_visualize.pack()

root.mainloop()