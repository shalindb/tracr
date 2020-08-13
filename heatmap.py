


import os

import matplotlib.pyplot as plt

import pandas as pd
import mplcursors
import geopandas as gpd
from matplotlib import rcParams
from shapely.geometry import Point, Polygon
from random_coordinate_generator import *

def generate_heatmap():
    street_map = gpd.read_file(os.path.join(os.path.dirname(__file__), 'berkeley-s7wq14-shapefile'
                                                                       '/s7wq14.shp'))
    my_df = pd.read_csv('random_coors_final.csv')
    john_df = pd.read_csv('john_doe_movement.csv')
    location = pd.read_csv('john_doe_location.csv')
    crs = {'init': 'epsg:4326'}
    geometry = [Point(xy) for xy in zip(my_df['Longitude'], my_df['Latitude'])]
    johnmetry = [Point(xy) for xy in zip(john_df['Longitude'], john_df['Latitude'])]
    locationetry = [Point(xy) for xy in zip(location['Longitude'], location['Latitude'])]
    geo_df = gpd.GeoDataFrame(my_df,  # specify our data
                              crs=crs,  # specify our coordinate reference system
                              geometry=geometry  # specify the geometry list we created
                              )

    geo_john_df = gpd.GeoDataFrame(john_df,  # specify our data
                              crs=crs,  # specify our coordinate reference system
                              geometry=johnmetry  # specify the geometry list we created
                              )

    geo_loc_df= gpd.GeoDataFrame(location,  # specify our data
                              crs=crs,  # specify our coordinate reference system
                              geometry=locationetry  # specify the geometry list we created
                              )

    fig, ax = plt.subplots(figsize=(10, 10))
    street_map.plot(ax=ax, alpha=0.4, color='black')
    geo_df.plot(ax=ax, markersize=10, color='#FDB515', marker=',')
    geo_john_df.plot(ax=ax, markersize=10, color='red', marker='^')
    geo_loc_df.plot(ax=ax, markersize=20, color='purple', marker='o')
    # ax.set_title('Interactions in Berkeley as noted by Tracr',
    #              fontdict={'fontsize': 20,
    #                        'fontweight': rcParams['axes.titleweight'],
    #                        'verticalalignment': 'baseline',
    #                        'horizontalalignment': 'center'})
    ax.set_axis_off()
    ax.legend(['Hotspots in Berkeley, CA', 'Your 10 Most Recent Interactions', 'Your Current Location'])
    long_to_address = dict(zip(my_df['Longitude'], my_df['Address']))
    # mplcursors.cursor(hover=True)
    mplcursors.cursor(hover=True).connect('add', lambda sel: sel.annotation.set_text(
        f'{long_to_address[sel.target[0]][:-26]}'
    ))
    #plt.show()
    plt.savefig('berkeley_dotmap.png')

if __name__ == '__main__':
    generate_heatmap()
