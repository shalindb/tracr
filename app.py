from flask import Flask, redirect, url_for, request, render_template, make_response, jsonify
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon

app = Flask(__name__)

"""
NOTE: @app.route('/test'), ('/login'), and ('/success) are all for TESTING
They will not go into the final product
TODO:
- Create requirements.txt
- Create basic working pages with HTML/CSS from Bootsnip

"""
@app.route('/test')
def test():
    return render_template('test_login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))

@app.route('/success/<name>')
def success(name):
    return f'Welcome, {name}'



@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080)
