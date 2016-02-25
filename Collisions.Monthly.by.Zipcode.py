#Anthony Beltran

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import csv

def main():
        monthNum = getMonths('NYPD_Motor_Vehicle_Collisions_10454.csv')
        month, collisionPerMonth = countMonths(monthNum)
        plot(month,collisionPerMonth, "10454")
        

def getMonths(aFile):
        f=open(aFile) 
        reader = csv.DictReader(f)
        d = [row['DATE'] for row in reader]
        monthNum = [int(d[:2]) for d in d]
        return monthNum
        

def countMonths(aList):
        count = Counter(aList)
        sCount = sorted(count.items())
        print sCount
        M,fCount = zip(*sCount)
        return M,fCount
        
        
def plot(x,y,zipCode):
        plt.bar(x,y)
        plt.title("Collisions in Zip Code " + zipCode + " Per Month (2012-2016)")
        plt.xlim(1,13)
        plt.ylim(0,400)
        plt.xlabel("Month")
        plt.ylabel("Amount of Collisions")
        plt.show()
main()
