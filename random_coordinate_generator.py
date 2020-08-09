"""Generates a DataFrame of random longitude & latitude coordinates in Berkeley to use for our simulation data"""

import random
import pandas as pd

def test_generator():
    coordinates = {'City': [], 'Longitude': [], 'Latitude': []}
    for i in range(0, 100):
        longitude = round(random.uniform(-122.296263,-122.251257), 6)
        latitude = round(random.uniform(37.858049,37.876750), 6)
        coordinates['City'].append('Berkeley')
        coordinates['Longitude'].append(longitude)
        coordinates['Latitude'].append(latitude)
    coor_df = pd.DataFrame(coordinates, columns=['City', 'Longitude', 'Latitude'])
    return coor_df

if __name__ == '__main__':
    x = test_generator()
    print(x)