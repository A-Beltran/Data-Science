import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import matplotlib.patches as mpatches
import csv
def main():
    
    plot()


def plot():    

    #LowerLeftCorner,UpperRightCorner
    map = Basemap(llcrnrlat=40.4961,
                  llcrnrlon=-74.2559,
                  urcrnrlat=40.9556,
                  urcrnrlon=-73.6677,
                  resolution = 'h',
                  epsg=2260)
    patchesBK = []
    patchesBX = []
    patchesMN = []
    patchesQN = []
    patchesSI = []

    map.drawmapboundary(fill_color='aqua')
    
    #Fill the continents with the land color
    map.fillcontinents(color='green',lake_color='aqua')
    map.drawcoastlines()
    
    
    # load the shapefile, use the name 'states'
    map.readshapefile('geo_export_5d40c3f0-4e17-4f62-b896-8938f11c233f', name='districts', drawbounds=False)
    ax = plt.gca() # get current axes instance
    
    for info, shape in zip(map.districts_info, map.districts):
        if info['boro'] == 'BK':
            patchesBK.append( Polygon(np.array(shape), True) )
        if info['boro'] == 'BX':
            patchesBX.append( Polygon(np.array(shape), True) )
        if info['boro'] == 'QN':
            patchesQN.append( Polygon(np.array(shape), True) )
        if info['boro'] == 'MN':
            patchesMN.append( Polygon(np.array(shape), True) )
        if info['boro'] == 'SI':
            patchesSI.append( Polygon(np.array(shape), True) )
        

    ax.add_collection(PatchCollection(patchesBK, facecolor= 'm', edgecolor='k', linewidths=1., zorder=2))
    ax.add_collection(PatchCollection(patchesBX, facecolor= 'r', edgecolor='k', linewidths=1., zorder=2))
    ax.add_collection(PatchCollection(patchesQN, facecolor= 'b', edgecolor='k', linewidths=1., zorder=2))
    ax.add_collection(PatchCollection(patchesMN, facecolor= 'y', edgecolor='k', linewidths=1., zorder=2))
    ax.add_collection(PatchCollection(patchesSI, facecolor= 'grey', edgecolor='k', linewidths=1., zorder=2))
    
    Bronx     = mpatches.Patch(color='red', label='Bronx')
    Manhattan = mpatches.Patch(color='yellow', label='Manhattan')
    Queens    = mpatches.Patch(color='blue', label='Queens')
    Staten_Is = mpatches.Patch(color='grey', label='Staten Is.')
    Brooklyn  = mpatches.Patch(color='magenta', label='Brooklyn')
    
    plt.legend(handles=[Bronx,Manhattan,Queens,Brooklyn,Staten_Is],loc=2)
    plt.title("NYC School Districts by Borough")
    plt.show()

main()
