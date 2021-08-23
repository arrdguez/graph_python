#!/usr/bin/python3


import pandas as pd
import plotly.express as px



#df = px.data.gapminder().query("country=='Canada'")
df = pd.read_csv("./BTCUSDT_1h.csv")
print(df)
fig = px.line(df, x="i", y="close", title='BTCUSDT close price')
fig.write_image("fig1.png")
#fig.show()




def main():
  pass



if __name__ == "__main__":
    main()