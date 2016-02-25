#Anthony Beltran

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import csv


def main():
        hoursList = getHours('NYPD_Motor_Vehicle_Collisions_10152015.csv')
        hour, collisionPerHour = countHours(hoursList)
        plot(hour,collisionPerHour,"10/15/15")

def getHours(aFile):
        f=open(aFile) 
        reader = csv.DictReader(f)
        collisionTime = []
        for row in reader:    
                t = row['TIME']     
                c = t.find(":") 
                collisionTime.append(int(t[:c]))
        return collisionTime

def countHours(aList):
        count = Counter(aList)
        sortedCount = sorted(count.items())
        print sortedCount
        H,finalCount = zip(*sortedCount)
        return H,finalCount

def plot(x,y,date):
        plt.bar(x,y)
        plt.title("Collisions in NYC By Hour (" + date + ")")
        plt.xlim(1,24)
        plt.ylim(0,70)
        plt.xlabel("Hour")
        plt.ylabel("Amount of Collisions")
        plt.show()

main()
