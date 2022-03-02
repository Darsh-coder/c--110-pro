
import statistics
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("newdata.csv")
series_data = df["temp"]
data = series_data.tolist()
population_mean = statistics.mean(data)
fig = ff.create_distplot([data],["temp"],show_hist = False)
fig.show()
