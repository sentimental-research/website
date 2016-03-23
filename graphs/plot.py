from twitter_graph import twitterData
from random import random
from bokeh.charts import TimeSeries
from bokeh.models import CustomJS, ColumnDataSource
from bokeh.plotting import figure, output_file, show

td = twitterData.twitterData("../../twitter_client/twitter_client/data/output_got.csv")

#output_file("callback.html")

TOOLS="resize,pan,wheel_zoom,box_zoom,reset,previewsave"


import pandas as pd
from bokeh.charts import TimeSeries, output_file, show

AAPL = pd.read_csv(
        "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",
        parse_dates=['Date'])

output_file("timeseries.html")

data = dict(AAPL=AAPL['Adj Close'], Date=AAPL['Date'])

p = TimeSeries(data, title="APPL", ylabel='Stock Prices')

show(p)



#p.line(data[])
#p.circle('x', 'y', color='color', size=8, source=s, alpha=0.4)
#
#s2 = ColumnDataSource(data=dict(ym=[0.5, 0.5]))
#p.line(x=[0, 1], y='ym', color="orange", line_width=5, alpha=0.6, source=s2)
##p.text(x=[0, 1], y='ym', text="some label", souce=s1)
#
#s.callback = CustomJS(args=dict(s2=s2), code="""
#        var inds = cb_obj.get('selected')['1d'].indices;
#        var d = cb_obj.get('data');
#        var ym = 0
#
#        if (inds.length == 0) { return; }
#
#        for (i = 0; i < d['color'].length; i++) {
#            d['color'][i] = "navy"
#        }
#        for (i = 0; i < inds.length; i++) {
#            d['color'][inds[i]] = "firebrick"
#            ym += d['y'][inds[i]]
#        }
#
#        ym /= inds.length
#        s2.get('data')['ym'] = [ym, ym]
#
#        cb_obj.trigger('change');
#        s2.trigger('change');
#    """)

#show(ts)
