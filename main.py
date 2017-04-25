from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

@app.route('/about', methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method=='POST':
        course, professor, http, description = request.form['course'], request.form['professor'], request.form['http'], request.form['description']
        dbHandler.insertLink(course, professor, http, description)
        links, courses = dbHandler.retrieveLinks(), []
        for course in links:
            courses.append(course[0])
        courses = sorted(list(set(courses)))
        return render_template('upload.html', links=links, courses=courses)
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')
