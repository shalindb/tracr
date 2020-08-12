


import os

import matplotlib.pyplot as plt

import mplcursors
import geopandas as gpd
from matplotlib import rcParams
from shapely.geometry import Point, Polygon
from random_coordinate_generator import *

def generate_heatmap():
    street_map = gpd.read_file(os.path.join(os.path.dirname(__file__), 'berkeley-s7wq14-shapefile'
                                                                       '/s7wq14.shp'))
    my_df = random_coor_generator()
    crs = {'init': 'epsg:4326'}
    geometry = [Point(xy) for xy in zip(my_df['Longitude'], my_df['Latitude'])]
    geo_df = gpd.GeoDataFrame(my_df,  # specify our data
                              crs=crs,  # specify our coordinate reference system
                              geometry=geometry  # specify the geometry list we created
                              )

    fig, ax = plt.subplots(figsize=(25, 25))
    street_map.plot(ax=ax, alpha=0.4, color='grey')
    geo_df.plot(ax=ax, markersize=50, color='blue', marker='o')
    ax.set_title('Interactions in Berkeley as noted by Tracr',
                 fontdict={'fontsize': 50,
                           'fontweight': rcParams['axes.titleweight'],
                           'verticalalignment': 'baseline',
                           'horizontalalignment': 'center'})
    ax.set_axis_off()

    plt.savefig('berkeley_heatmap.png')