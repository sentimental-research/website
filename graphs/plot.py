from twitter_graph import twitterData
from random import random
from bokeh.charts import TimeSeries, Line
from bokeh.models import CustomJS, ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_file, show, vplot

td = twitterData.twitterData("../../twitter_client/twitter_client/data/output_got.csv")
monthly_data = td.aggregate_score()
final_score = td.final_socre()

def plot_timeseries(data):
    TOOLS="resize,pan,wheel_zoom,box_zoom,reset,previewsave"
    p = TimeSeries(data, title="satisfaction (weekly)", xlabel="Time")
    return(p)

def plot_histogram(data):
    return(0)


output_file("community_satisfaction.html")
s1 = plot_timeseries(monthly_data)
show(s1)
