from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':
        return redirect(url_for('show_project_profile',
                                project=request.form['project']))
    return render_template('index.html')

@app.route('/<project>/')
def show_project_profile(project):
    # calculate the output (with a wheel..?)
    # show the user profile for that user
    return render_template('project.html', project=project)
# what to do when twitter does not return anything?


@app.route('/about')
def about():
    return 'Here we show who we are and what we do' # add pictures and descriptions of ourselves.

# 404 page?

# with app.test_request_context():
#     print url_for('show_project_profile', project='sunpy')
# url_for('static', filename='style.css')
if __name__ == '__main__':
    app.run()
