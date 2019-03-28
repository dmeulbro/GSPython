from math import *

def numAnalysis(studList, projList):
    placeList = []
    for i in range(len(projList)):
        for j in range(len(projList[i].memList)):
            currStudID = int(projList[i].memList[j].studID) - 1
            k = 0
 
            for l in range(len(studList[currStudID].rList)):
                k += 1
                if(i + 1 == studList[currStudID].rList[l]):
                    placeList.append(k)
                    break

    countList = countMatch(placeList)
    return countList

def percentMatch(countList, num):
    percList = []
    for i in range(len(countList)):
        percList.append(float(countList[i])/num)
    return percList

def countMatch(placeList):
    one     = placeList.count(1)
    two     = placeList.count(2)
    three   = placeList.count(3)
    four    = placeList.count(4)
    five    = placeList.count(5)
    six     = placeList.count(6)
    seven   = placeList.count(7)
    eight   = placeList.count(8)
    nine    = placeList.count(9)
    ten     = placeList.count(10)

    countList = [one, two, three, four, five, six, seven, eight, nine, ten]

#    print "Percent in Top Choice: " + str(float(one)/float(len(placeList)))
#    print "Percent in 2nd Choice: " + str(float(two)/float(len(placeList)))
#    print "Percent in 3rd Choice: " + str(float(three)/float(len(placeList)))
#    print "Percent in 4th Choice: " + str(float(four)/float(len(placeList)))
#    print "Percent in 5th Choice: " + str(float(five)/float(len(placeList)))
#    print "Percent in 6th Choice: " + str(float(six)/float(len(placeList)))
#    print "Percent in 7th Choice: " + str(float(seven)/float(len(placeList)))
#    print "Percent in 8th Choice: " + str(float(eight)/float(len(placeList)))
#    print "Percent in 9th Choice: " + str(float(nine)/float(len(placeList)))
#    print "Percent in 10th Choice: " + str(float(ten)/float(len(placeList)))


    return countList
