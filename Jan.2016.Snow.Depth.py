"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
import urllib2
import re

#A function that takes the kind of temperature ("Max", "Min", "Ave") and
#a URL and returns the temperature from that line.
def getTempFromWeb(kind,url):
     page = urllib2.urlopen(url)
     lines = page.readlines()
     for i in range(len(lines)):
          if lines[i].find(kind+" Temperature") >= 0:
               m = i
     searchObj = re.search('\d+', lines[m+2])
     return int(searchObj.group(0))
def getDepthFromWeb(kind,url):
     
     page = urllib2.urlopen(url)
     lines = page.readlines()
     for i in range(len(lines)):
          if lines[i].find(kind+" Depth") >= 0:
               m = i
     
     searchObj = re.search('\d+', lines[m+2])
     if(searchObj == None):
          return 0
     else:
          return int(searchObj.group(0))

def main():
   
     prefix = "http://www.wunderground.com/history/airport/KLGA/2016/01/"
     suffix = "/DailyHistory"
     days = []          #Sets up a list to store days
     mins = []           #Sets up a list so store min values
     depths = []
     areas = []
     for day in range(1,32): #For each day
          days.append(day)       #Add the day to the list
          url = prefix+str(day)+suffix      #Make the url
          Min = getTempFromWeb("Min",url) 
          mins.append(Min)
          Depth = getDepthFromWeb("Snow",url)
          depths.append(Depth) 
          area= np.pi * (1+1 * (Depth*3))
          areas.append(area)

          print "Jan",day, "Min", Min
          print "Jan",day, "Snow Depth", Depth
          print "Area will be",area

     plt.xlim([0,35])
     plt.ylim([0,80])
     plt.title("Snow Depth to Temp Relation, NYC January 1-31")
     plt.ylabel("Temperatures")
     plt.xlabel("Days")
     plt.scatter(days, mins, s=areas, c="blue",alpha=0.5)

     plt.show()
main()
