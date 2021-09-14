import numpy as numpy
import pandas as pd

import yfinance as yf
import plotly.graph_objs as go

data = []

startingBalance = 25000.00

with open('tickers.txt') as tickerDoc:
	tickers = tickerDoc.read()
	tickerList = tickers.split()
for i in range(len(tickerList)):
	data.append(yf.download(tickers= tickerList[i], period = '1d', interval = '5m')) 

#declare figure
fig = go.Figure()

#Candlestick
for i in range(len(data)):
	fig.add_trace(go.Candlestick(x=data[i].index,
	                open=data[i]['Open'],
	                high=data[i]['High'],
	                low=data[i]['Low'],
	                close=data[i]['Close'], name = tickerList[i]))

# Add titles
fig.update_layout(
    title='Live share price evolution',
    yaxis_title='Stock Price (USD per Shares)')

# X-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#Show
fig.show()