import os
import subprocess
from random import random

from flask import Flask, request, render_template, url_for, redirect
import pandas as pd
from bokeh.charts import TimeSeries, Line
from bokeh.models import CustomJS, ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_file, show, vplot

from TwitterClient import TwitterClient
from twitter_graph import twitterData

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':
        return redirect(url_for('show_project_profile',
                                project=request.form['project']))
    return render_template('index.html')


def query_twitter(project):
    pass
    # client = TwitterClient()
    # results = client.get_tweets(project)
    # client.write_results(results)

def calculate_sentiment():
    subprocess.call(['java', '-version']) #'-jar', 'sentiment...jar','input', 'output'])

def generate_plot(inputfile):
    td = twitterData.twitterData(inputfile)
    monthly_data = td.aggregate_score()
    final_score = td.final_socre()

    def plot_timeseries(data):
        TOOLS="resize,pan,wheel_zoom,box_zoom,reset,previewsave"
        p = TimeSeries(data, title="satisfaction (weekly)", xlabel="Time")
        return(p)

    def plot_histogram(data):
        return(0)

    output_file(os.path.join('static', "community_satisfaction.html"))
    s1 = plot_timeseries(monthly_data)
    #show(s1)
    return td


@app.route('/package/<project>/')
def show_project_profile(project):
    query_twitter(project)
    calculate_sentiment()
    tweets = generate_plot('output_got.csv')
    # calculate the output (with a wheel..?)
    # show the user profile for that user
    color = ['green', 'orange', 'red']
    status = [':)', ':|', ':(', '%E2%98%A0']
    session = {'color': color[0],
               'status': status[0]}

    # df2 = pd.DataFrame({ 'date' : pd.Timestamp('20130102'),
    #                      'text' : ['this is my  tweet',
    #                                'I hate this'] })

    tweetlist = tweets.data.to_dict(orient='records')

    return render_template('project.html',
                           project=project,
                           badge='community-{status}-{color}.svg'.format(**session),
                           tweets=tweetlist)
# what to do when twitter does not return anything?


@app.route('/about')
def about():
    return 'Here we show who we are and what we do' # add pictures and descriptions of ourselves.

# 404 page?

# with app.test_request_context():
#     print url_for('show_project_profile', project='sunpy')
# url_for('static', filename='style.css')
if __name__ == '__main__':
    app.run(debug=True)
