from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html.jinja')

@app.route('/extract')
def extract():
    return render_template('extraction.html.jinja')

@app.route('/products')
def products():
    return render_template('productlist.html.jinja')

@app.route('/product')
def product():
    return render_template('product.html.jinja')

@app.route('/charts')
def charts():
    return render_template('charts.html.jinja')

@app.route('/author')
def author():
    return render_template('author.html.jinja')



@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}!"