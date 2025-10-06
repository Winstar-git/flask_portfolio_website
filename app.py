from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    person = {
        'name': 'James Starwin Canoy',
        'role': 'Student at Polytechnic University of the Philippines'
    }
    return render_template('profile.html', person=person)

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        result = text.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', '0'))
            area = 3.1416 * (radius ** 2)
        except Exception:
            area = "Invalid input"
    return render_template('circle.html', area=area)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', '0'))
            height = float(request.form.get('height', '0'))
            area = 0.5 * base * height
        except Exception:
            area = "Invalid input"
    return render_template('triangle.html', area=area)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/projects')
def projects():
    data_file = os.path.join(app.root_path, 'data', 'projects.json')
    projects = []
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            projects = json.load(f)
    except Exception:
        projects = []
    return render_template('projects.html', projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
