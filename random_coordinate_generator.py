"""Generates a DataFrame of random longitude & latitude coordinates in Berkeley to use for our simulation data"""

import random
import pandas as pd
from geopy.geocoders import Nominatim

def random_coor_generator():
    coordinates = {'City': [], 'Longitude': [], 'Latitude': [], 'Address': []}
    geolocator = Nominatim(user_agent='Tracr')
    for i in range(0, 20):
        # Downtown Berkeley Hotspots
        """User lives in north berkeley, works at cal, goes to DT berkeley"""
        longitude = round(random.uniform(-122.272843,-122.266315), 6)
        latitude = round(random.uniform(37.865639,37.872618), 6)
        coor_lat_long = f"{str(latitude)}, {str(longitude)}"
        coor_address = geolocator.reverse(coor_lat_long)
        coordinates['Address'].append(coor_address)
        coordinates['City'].append('Berkeley')
        coordinates['Longitude'].append(longitude)
        coordinates['Latitude'].append(latitude)
    for i in range(0, 10):
        # Front of UC Berkeley hotspot
        """User lives in north berkeley, works at cal, goes to DT berkeley"""
        longitude = round(random.uniform(-122.261677, -122.256868), 6)
        latitude = round(random.uniform(37.866723, 37.869975), 6)
        coor_lat_long = f"{str(latitude)}, {str(longitude)}"
        coor_address = geolocator.reverse(coor_lat_long)
        coordinates['Address'].append(coor_address)
        coordinates['City'].append('Berkeley')
        coordinates['Longitude'].append(longitude)
        coordinates['Latitude'].append(latitude)
    for i in range(0, 10):
        # north berkeley
        """User lives in north berkeley, works at cal, goes to DT berkeley"""
        longitude = round(random.uniform(-122.260733,-122.256524), 6)
        latitude = round(random.uniform(37.873092,37.875870), 6)
        coor_lat_long = f"{str(latitude)}, {str(longitude)}"
        coor_address = geolocator.reverse(coor_lat_long)
        coordinates['Address'].append(coor_address)
        coordinates['City'].append('Berkeley')
        coordinates['Longitude'].append(longitude)
        coordinates['Latitude'].append(latitude)
    for i in range(0, 20):
        # random throughout berkeley
        """User lives in north berkeley, works at cal, goes to DT berkeley"""
        longitude = round(random.uniform(-122.300998,-122.252901), 6)
        latitude = round(random.uniform(37.850188,37.884067), 6)
        coor_lat_long = f"{str(latitude)}, {str(longitude)}"
        coor_address = geolocator.reverse(coor_lat_long)
        coordinates['Address'].append(coor_address)
        coordinates['City'].append('Berkeley')
        coordinates['Longitude'].append(longitude)
        coordinates['Latitude'].append(latitude)
    coor_df = pd.DataFrame(coordinates, columns=['City', 'Longitude', 'Latitude', 'Address'])
    coor_df.to_csv('random_coors_final.csv')

    return coor_df


def john_doe_simulator():
    coordinates = {'City': [], 'Longitude': [], 'Latitude': [], 'Address': []}
    geolocator = Nominatim(user_agent='JohnDoe')
    #North Berkeley -> Downtown Berkeley
    coordinates['Latitude'].append(37.873024)
    coordinates['Longitude'].append(-122.283492)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.873024)}, {str(-122.283492)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.870382)
    coordinates['Longitude'].append(-122.281688)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.870382)}, {str(-122.281688)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.871466)
    coordinates['Longitude'].append(-122.268891)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.871466)}, {str(-122.268891)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.870043)
    coordinates['Longitude'].append(-122.267431)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.870043)}, {str(-122.267431)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.869433)
    coordinates['Longitude'].append(-122.267431)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.869433)}, {str(-122.267431)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.870246)
    coordinates['Longitude'].append(-122.265971)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.870246)}, {str(-122.265971)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.870517)
    coordinates['Longitude'].append(-122.264339)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.870517)}, {str(-122.264339)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.872008)
    coordinates['Longitude'].append(-122.259443)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.872008)}, {str(-122.259443)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.873227)
    coordinates['Longitude'].append(-122.257640)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.873227)}, {str(-122.257640)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coordinates['Latitude'].append(37.875463)
    coordinates['Longitude'].append(-122.259959)
    coordinates['City'].append('Berkeley')
    coor_lat_long = f"{str(37.875463)}, {str(-122.259959)}"
    coordinates['Address'].append(geolocator.reverse(coor_lat_long))

    coor_df = pd.DataFrame(coordinates, columns=['City', 'Longitude', 'Latitude', 'Address'])
    coor_df.to_csv('john_doe_movement.csv')
if __name__ == '__main__':
    john_doe_simulator()