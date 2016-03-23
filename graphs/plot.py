import numpy as np

from bokeh.models import BoxSelectTool, LassoSelectTool, Paragraph
from bokeh.plotting import figure, hplot, vplot

# create three normal population samples with different parameters
x1 = np.random.normal(loc=5.0, size=400) * 100
y1 = np.random.normal(loc=10.0, size=400) * 10

x2 = np.random.normal(loc=5.0, size=800) * 50
y2 = np.random.normal(loc=5.0, size=800) * 10

x3 = np.random.normal(loc=55.0, size=200) * 10
y3 = np.random.normal(loc=4.0, size=200) * 10

x = np.concatenate((x1, x2, x3))
y = np.concatenate((y1, y2, y3))

TOOLS="pan,wheel_zoom,box_select,lasso_select"

# create the scatter plot
p = figure(tools=TOOLS, plot_width=600, plot_height=600, title=None, min_border=10, min_border_left=50)
#r = p.line(x, y, size=3, color="#3A5785", alpha=0.6)
r = p.line(x, y)

p.select(BoxSelectTool).select_every_mousemove = False
p.select(LassoSelectTool).select_every_mousemove = False

# create the horizontal histogram
#hhist, hedges = np.histogram(x, bins=20)
#hzeros = np.zeros(len(hedges)-1)
#hmax = max(hhist)*1.1
#
#LINE_ARGS = dict(color="#3A5785", line_color=None)
#
#ph = figure(toolbar_location=None, plot_width=p.plot_width, plot_height=200, x_range=p.x_range,
#            y_range=(-hmax, hmax), title=None, min_border=10, min_border_left=50)
#ph.xgrid.grid_line_color = None

def update(attr, old, new):
    print("something")
#    inds = np.array(new['1d']['indices'])
#    if len(inds) == 0 or len(inds) == len(x):
#        hhist1, hhist2 = hzeros, hzeros
#        vhist1, vhist2 = vzeros, vzeros
#    else:
#        neg_inds = np.ones_like(x, dtype=np.bool)
#        neg_inds[inds] = False
#        hhist1, _ = np.histogram(x[inds], bins=hedges)
#        vhist1, _ = np.histogram(y[inds], bins=vedges)
#        hhist2, _ = np.histogram(x[neg_inds], bins=hedges)
#        vhist2, _ = np.histogram(y[neg_inds], bins=vedges)
#
#    hh1.data_source.data["top"]   =  hhist1
#    hh2.data_source.data["top"]   = -hhist2
#    vh1.data_source.data["right"] =  vhist1
#    vh2.data_source.data["right"] = -vhist2

r.data_source.on_change('selected', update)

