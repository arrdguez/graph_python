#!/usr/bin/python3


import pandas as pd
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()

def main():
  pass



if __name__ == "__main__":
    main()