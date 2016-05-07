import re
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_toolkits.basemap import Basemap
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
def main():
    rawChampStatList = getStats("prerework.txt")
    c,p,w,b,r = createProfiles(rawChampStatList)
    #outFile('LoLChampDataPRW.txt',c,p,w,b,r)
    print 'file created'
    popularGraph(p,c,w)
    roleBanGraph(c,b,r)
    roleWinGraph(c,w,r)


def sortRoles(champions,rate,role,div):
    topLane = []
    midLane = []
    adCarry = []
    support = []
    jungler = []

    for i in range(0,len(champions)):
        if(role[i] == 'Top Lane'):
            topLane.append(float(rate[i]))
        if(role[i] == 'Middle Lane'):
            midLane.append(float(rate[i]))
        if(role[i] == 'AD Carry'):
            adCarry.append(float(rate[i]))
        if(role[i] == 'Support'):
            support.append(float(rate[i]))
        if(role[i] == 'Jungler'):
            jungler.append(float(rate[i]))
    ta = 0
    for i in topLane:
        ta+=i
    ma = 0
    for i in midLane:
        ma+=i
    aa = 0
    for i in adCarry:
        aa+=i
    sa = 0
    for i in support:
        sa+=i
    ja = 0
    for i in jungler:
        ja+=i
    return ta/div,ma/div,aa/div,sa/div,ja/div
    


def roleWinGraph(c,w,r):
    print 'TOP WIN RATE ROLES'
    roles = ['Top Lane','Middle Lane','AD Carry','Support','Jungler']
    top,mid,adc,sup,jun = sortRoles(c,w,r,100)
    print top,mid,adc,sup,jun

    N = len(roles)
    ind = np.arange(N)  # the x locations for the groups

    width = 1.00      # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, [top,mid,adc,sup,jun], width, color='b')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Role Win Rate')
    ax.set_title('Win Rate by Role')
    ax.set_xticks(ind+0.5)
    ax.set_xticklabels([roles[i] for i in range(0,5)])

    plt.show()
    
def roleBanGraph(c,b,r):
    print 'TOP BAN RATE ROLES'
    roles = ['Top Lane','Middle Lane','AD Carry','Support','Jungler']
    top,mid,adc,sup,jun = sortRoles(c,b,r,5)
    N = len(roles)
    ind = np.arange(N)  # the x locations for the groups

    width = 1.00      # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, [top,mid,adc,sup,jun], width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Cumulative Percentage')
    ax.set_title('Ban Rate by Role')
    ax.set_xticks(ind+0.5)
    ax.set_xticklabels([roles[i] for i in range(0,5)])

    plt.show()





def popularGraph(popularity,champion,winRate):
    print 'MOST POPULAR CHAMPIONS'
    indexPopular = mostStat(popularity,15)
    print indexPopular
    for i in indexPopular:
        print champion[i],winRate[i]
        

    N = len(indexPopular)
    popY = [popularity[i] for i in indexPopular]

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, popY, width, color='r')

    winY = [winRate[i] for i in indexPopular]
    rects2 = ax.bar(ind + width, winY, width, color='b')

# add some text for labels, title and axes ticks
    ax.set_ylabel('Percentage')
    ax.set_title('Highest Play Rate Champions w/ Popularity')
    ax.set_xticks(ind + width)
    ax.set_xticklabels([champion[i] for i in indexPopular])

    ax.legend((rects1[0], rects2[0]), ('Popularity', 'Win Rate'))
    plt.show()

def mostStat(aList,threshold):
    index = []
    for i,j in enumerate(aList):
        if(float(j)>=threshold):
            index.append(i)
    return index

                        
def createProfiles(aList):
    champion = []
    popularity = []
    winRate = []
    banRate = []
    role = []

    for i in range(0,len(aList)):
        if(i%7==0):
            champion.append(aList[i])

        if(i%7==3):
            popularity.append(aList[i])

        if(i%7==4):
            winRate.append(aList[i])

        if(i%7==5):
            banRate.append(aList[i])

        if(i%7==6):
            role.append(aList[i])

    return champion,popularity,winRate,banRate,role
                        
        

def getStats(aFile):
    page = open(aFile,'r')
    data = page.read()
    rawStats = re.findall(r'>\w+</|>\d+\.\d+%<|>\w+%<|>\w+ \w+</|>\w+\W+\w+</',data)
    cleanStats=[]
    for i in rawStats:
        c = i.find('>')
        cleanStats.append(i[c+1:-2])
    return cleanStats

def outFile(aFile,champion,popularity,winRate,banRate,role):
    f = open(aFile,'w')
    for i in range(0,len(champion)):
	    f.write(champion[i]
                            +', '
                            + popularity[i]
                            +', '
                            + winRate[i]
                            +', '
                            + banRate[i]
                            +', '
                            + role[i]
                            +'\n')
    f.close()        

main()

