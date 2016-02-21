#Katherine St. John
#Data Science, Spring 2016
#Simple example of scaling vectors using list comprehensions

import matplotlib.pyplot as plt
import urllib2
import re

means= [40,38,42,27,22,35,40,41,44,51,35,36,28,32,43,47,38,27,24,34,33,26,27,30,34,42,41,37,37,35,47]
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
##def getTempFromWeb(kind,url):
##     page = urllib2.urlopen(url)
##     lines = page.readlines()
##     for i in range(len(lines)):
##          if lines[i].find(kind+" Temperature") >= 0:
##               m = i
##     searchObj = re.search('\d+', lines[m+2])
##     return int(searchObj.group(0))
##
##def main():
##     #The url is made up of the prefix, day, and suffix:
##     prefix = "http://www.wunderground.com/history/airport/KLGA/2016/01/"
##     suffix = "/DailyHistory"
##     days = []          #Sets up a list to store days
##     means = []           #Sets up a list to store mean values
##     for day in range(1,32): #For each year
##          days.append(day)       #Add the year to the list
##          url = prefix+str(day)+suffix      #Make the url
##          Mean = getTempFromWeb("Mean",url) 
##          means.append(Mean) 

#We'll do the same operations for each state, so put in a function:
def scale(dList, plt, lab,col):
     """
     Takes a list, label, and color and creates a scatter plot
     of the percentage change with respect to the first entry
     in the list.
     """
     avg = (sum(dList))/len (dList)
     print avg
     scaled= [i*100/avg-100 for i in dList]
   
     plt.scatter(days, scaled, label=lab, c = col, s=75)


#Create scatter plots for each state:
scale(means,plt,"NY", "blue")


#Set up title, axis labels, and legend, and then show:
plt.title("NY Temp Deviation From Average Jan 2016")
plt.xlabel('Day')
plt.ylabel('Percent Change')
plt.legend()
plt.show()

