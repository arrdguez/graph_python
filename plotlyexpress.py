#!/usr/bin/python3

import os


import pandas as pd
import plotly.express as px

#For some extra features
import plotly.graph_objects as go


if not os.path.exists("images"):
    os.mkdir("images")


#df = px.data.gapminder().query("country=='Canada'")
df = pd.read_csv("./BTCUSDT_1h.csv")
print(df)


#Genneral default picture
fig = px.line(df, x="date", y="close", title='BTCUSDT - Binance close price', width=2400, height=1200)
fig.write_image("images/first_fig1.png")

#Genneral default picture
fig = px.line(df, x="date", y="close", title='BTCUSDT - Binance close price', range_x=['2021-08-01','2021-08-23'])
fig.write_image("images/first_xrange_fig1.png")


#
fig = px.line(df, x="date", y="close", title='BTCUSDT - Binance close price', text='close', range_y=[46500,50000], range_x=['2021-08-20','2021-08-23'])
fig.update_traces(textposition="bottom right")
fig.write_image("images/first_fig2.png")

#
fig = go.Figure()
fig.add_trace(go.Scatter( x=df['date'], y=df['close'],
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter( x=df['date'], y=df['close']+30000,
                    mode='lines',
                    name='lines'))
fig.write_image("images/first_fig3.png")

#
fig = go.Figure()
fig.add_trace(go.Scatter( x=df['date'], y=df['volume'],
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter( x=df['date'], y=df['volume'] + 34,
                    mode='markers',
                    name='markers'))
fig.write_image("images/first_fig4.png")


#
fig = go.Figure()
fig.add_trace(go.Scatter( x=df['date'], y=df['close'],
                    xperiod="M2",
                    mode='lines',
                    name='close'))
fig.add_trace(go.Scatter( x=df['date'], y=df['open'],
                    xperiod="M2",
                    mode='lines',
                    name='close+34'))
fig.write_image("images/first_fig5.png")

def main():
  pass
  #



if __name__ == "__main__":
    main()