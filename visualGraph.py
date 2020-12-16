import pandas
import plotly.express as px


lol = pandas.read_csv("https://raw.githubusercontent.com/pogman96/covidschooldata/main/parsed/cali.csv")
fig = px.line(lol, x='Date', y='Case increase (per 100,000)', title='Data plotting of California Coronavirus Cases')
fig.show()