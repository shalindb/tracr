import os

import loc as loc
from flask import Flask, redirect, url_for, request, render_template, make_response, jsonify
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import descartes
import mplcursors
import geopandas as gpd
from matplotlib import rcParams
from shapely.geometry import Point, Polygon
from random_coordinate_generator import *

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
    # x = os.path.join(os.path.dirname(__file__), 'berkeley_shapefile_data/Berkeley_councildistricts_2015.shp')
    # print(x)
    street_map = gpd.read_file(os.path.join(os.path.dirname(__file__), 'berkeley-s7wq14-shapefile'
                                                                       '/s7wq14.shp'))
    my_test_df = test_generator()
    crs = {'init': 'epsg:4326'}
    geometry = [Point(xy) for xy in zip(my_test_df['Longitude'], my_test_df['Latitude'])]
    geo_df = gpd.GeoDataFrame(my_test_df,  # specify our data
                              crs=crs,  # specify our coordinate reference system
                              geometry=geometry  # specify the geometry list we created
                              )

    fig, ax = plt.subplots(figsize=(25, 25))
    street_map.plot(ax=ax, alpha=0.4, color='grey')
    geo_df.plot(ax=ax, markersize=30, color='blue', marker='o')
    ax.set_title('Interactions in Berkeley as noted by Tracr',
                 fontdict={'fontsize': 50,
                           'fontweight': rcParams['axes.titleweight'],
                           'verticalalignment': 'baseline',
                           'horizontalalignment': 'center'})
    ax.set_axis_off()
    mplcursors.cursor(ax).connect(
        "add", lambda sel: sel.annotation.set_text('Heulo')
    )
    #plt.show()
    plt.savefig('test_1.png')
    return render_template('heatmap.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
