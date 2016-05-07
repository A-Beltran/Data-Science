import re
import matplotlib.pyplot as plt
import numpy as np

def main():
    rawChampStatList = getStats("prerework.txt")
    c,p,w,b,r = createProfiles(rawChampStatList)
    createProfiles(rawChampStatList)
    outFile('LoLChampDataPRW.txt',c,p,w,b,r)
    print 'file created'
    popularGraph(p,c,w)



def winBanGraph(popularity,champion,winRate):
    print 'TOP WIN RATE CHAMPIONS'
    indexWin = mostStat(winRate,)
    print indexPopular
    for i in indexPopular:
        print champion[i]

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
    rects2 = ax.bar(ind + width, winY, width, color='y')

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

