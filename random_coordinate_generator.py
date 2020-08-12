"""Generates a DataFrame of random longitude & latitude coordinates in Berkeley to use for our simulation data"""

import random
import pandas as pd
from geopy.geocoders import Nominatim

def random_coor_generator():
    coordinates = {'City': [], 'Longitude': [], 'Latitude': [], 'Address': []}
    geolocator = Nominatim(user_agent='Tracr')
    for i in range(0, 50):
        # change random coordinate generation to show hotspots
        """User lives in north berkeley, works at cal, goes to DT berkeley"""
        longitude = round(random.uniform(-122.30,-122.255126), 6)
        latitude = round(random.uniform(37.852049,37.881750), 6)
        coor_lat_long = f"{str(latitude)}, {str(longitude)}"
        coor_address = geolocator.reverse(coor_lat_long)
        coordinates['Address'].append(coor_address)
        coordinates['City'].append('Berkeley')
        coordinates['Longitude'].append(longitude)
        coordinates['Latitude'].append(latitude)
    coor_df = pd.DataFrame(coordinates, columns=['City', 'Longitude', 'Latitude', 'Address'])
    coor_df.to_csv('random_coors.csv')
    return coor_df

if __name__ == '__main__':
    x = random_coor_generator()
    print(x)