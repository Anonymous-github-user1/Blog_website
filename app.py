import jinja2
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/example')
def example():
    return render_template('example.html')

if __name__ == '__main__':
    app.run(debug=True)