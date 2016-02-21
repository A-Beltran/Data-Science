#Anthony Beltran
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


def main():
     #The url is made up of the prefix, day, and suffix:
     prefix = "http://www.wunderground.com/history/airport/KLGA/2016/01/"
     suffix = "/DailyHistory"
     days = []          #Sets up a list to store days
     mins = []           #Sets up a list so store min values
     for day in range(1,32): #For each year
          days.append(day)       #Add the year to the list
          url = prefix+str(day)+suffix      #Make the url
          Min = getTempFromWeb("Min",url) 
          mins.append(Min)  
          print "Min on Jan", day, Min  
  

     #Makea a histogram of the minimum temps:
     plt.hist(mins)
     plt.title("Histogram for NYC Temps, January 1-31")
     plt.xlabel("Temperatures")
     plt.ylabel("Amount of Days") 
     plt.show()

     

main()
