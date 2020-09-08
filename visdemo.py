# OSeMOSYS Visualization Demo
# Chang Su
# 2020-09-05

import geopandas as gpd
import matplotlib.pyplot as plt

name = input('Please type in the country name: ')

globe_file = './ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp'

countries = gpd.read_file(globe_file)

while name.title() not in countries['ADMIN'].values:
    print('Please retype the correct name \n(perhaps the full name of the country).')
    name = input('Please type in the country name: ')

geometry = countries[countries['ADMIN'] == name.title()]['geometry']

shape = geometry.plot()
shape.set_axis_off()

plt.show()
