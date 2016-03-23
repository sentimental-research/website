from flask import Flask, request, render_template, url_for, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':
        return redirect(url_for('show_project_profile',
                                project=request.form['project']))
    return render_template('index.html')

@app.route('/package/<project>/')
def show_project_profile(project):
    # calculate the output (with a wheel..?)
    # show the user profile for that user
    color = ['green', 'orange', 'red']
    status = [':)', ':|', ':(', '%E2%98%A0']
    session = {'color': color[2],
               'status': status[3]}

    df2 = pd.DataFrame({ 'date' : pd.Timestamp('20130102'),
                         'text' : ['this is my  tweet',
                                   'I hate this'] })


    tweetslist = [{'date':'Jun 2012', 'text':'this is my twet'},
                  {'date':'July 2010', 'text': 'I hate this'}]
    tweetlist = df2.to_dict(orient='records')
    print(tweetlist)
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
