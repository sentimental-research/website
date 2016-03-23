import subprocess

from flask import Flask, request, render_template, url_for, redirect
import pandas as pd

from TwitterClient import TwitterClient

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

@app.route('/package/<project>/')
def show_project_profile(project):
    query_twitter(project)
    calculate_sentiment()
    # calculate the output (with a wheel..?)
    # show the user profile for that user
    color = ['green', 'orange', 'red']
    status = [':)', ':|', ':(', '%E2%98%A0']
    session = {'color': color[2],
               'status': status[3]}

    df2 = pd.DataFrame({ 'date' : pd.Timestamp('20130102'),
                         'text' : ['this is my  tweet',
                                   'I hate this'] })

    tweetlist = df2.to_dict(orient='records')

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
