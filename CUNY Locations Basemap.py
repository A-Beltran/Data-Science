import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import csv
def main():
    lat,lon = getCoords(
        "City_University_of_New_York__CUNY__University_Campus_Locations_Map.csv")
    print lat
    print lon
    plot(lat,lon)


def plot(lat,lon):    

    #LowerLeftCorner,UpperRightCorner
    map = Basemap(llcrnrlat=40.4961,
                  llcrnrlon=-74.2559,
                  urcrnrlat=40.9556,
                  urcrnrlon=-73.6677,
                  resolution = 'h',
                  epsg=2260)

    map.drawmapboundary(fill_color='aqua')
    #Fill the continents with the land color
    map.fillcontinents(color='green',lake_color='aqua')

    map.drawcoastlines()
    map.drawcounties(linewidth=0.5)
    
    x, y = map(lon, lat)

    map.plot(x, y, "rd")
    plt.title("CUNY University Campus Locations")
    plt.show()

    

def getCoords(aFile):
        f=open(aFile) 
        reader = csv.DictReader(f)
        latitudes = []
        longitudes = []
        for row in reader:    
                lat = row['Latitude']
                lon = row['Longitude']
                
                latitudes.append(float(lat))
                longitudes.append(float(lon))
        return latitudes,longitudes

main()
