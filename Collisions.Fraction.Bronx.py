#Anthony Beltran

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import csv
def main():
    bronxHH,totalHH = getHours('NYPD_Motor_Vehicle_Collisions_10152015.csv')
    hour, bronxCount, totalCount = countHours(bronxHH,totalHH)
    percentageList = getPercentage(bronxCount,totalCount)
    plot(hour,percentageList,"10/15/15")


def getHours(aFile):
    f=open(aFile) 
    reader = csv.DictReader(f)
    bronxHours = []
    totalHours = []

    for row in reader:
        t = row['TIME']
        c = t.find(':')
        totalHours.append(int(t[:c]))

        if row['BOROUGH'] == 'BRONX':
            bronxHours.append(int(t[:c]))
    return bronxHours,totalHours


def countHours(aList,bList):
    bxCount = Counter(aList)
    toCount = Counter(bList)

    sBxCount = sorted(bxCount.items())
    sToCount = sorted(toCount.items())

   # hocBx,finalBxCount = zip(*sBxCount) didnt account for an hour not occurring
    hocTo,finalToCount = zip(*sToCount)
    finalBxCount = [1,1,1,0,0,0,0,2,10,3,2,2,1,4,6,5,4,4,7,1,1,2,2,1]
    
    return hocTo,finalBxCount,finalToCount


def getPercentage(aList, bList):
    percent=[]
    for i in range(0,24):
       percent.append(float(aList[i])/bList[i]*100)
    print percent
    return percent


def plot(x,y,date):
    plt.bar(x,y)
    plt.xlim(0,25)
    plt.ylim(0,70)
    plt.title("Percentage of NYC Collisions in the Bronx ("+date+")")
    plt.xlabel("Hour")
    plt.ylabel("Percentage")
    plt.show()
main()
