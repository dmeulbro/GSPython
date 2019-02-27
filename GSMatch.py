import random
import array
import sys

def matchProj (studList, projList):
    for i in range(0,len(studList)):
        studList[i].paired = False
        studList[i].currRank = None
        studList[i].pProject = None

    while(studList != None):
        currentStud = studList.pop(random.randint(1,len(studList)));
        while(currentStud.rList != None):
            topProj = int(currentStud.rList.pop(0)) - 1
            currentStud.currRank = projList[topProj].pList.index(currentStud.studID)
            if(projList[topProj].numMems != projList[topProj].maxSize):
                currentStud.pProject = topProj + 1
                currentStud.paired = True
                projList[topProj].memList.append(currentStud)
            else:
                lowestStud = findLowest(projList[topProj].memList)
                if(lowestStud.currRank < currentStud.currRank):
                    # place new student
                    currentStud.pProject = topProj + 1
                    currentStud.paired = True
                    projList[topProj].memList.append(currentStud)

                    # add old paired student to studlist
                    lowestStud.currRank = None
                    lowestStud.paired = False
                    lowestStud.pProject = None
                    studList.append(lowestStud)
                    break
                else:
                    currentStud.currRank = None
                    projList[topProj].memList.append(lowestStud)

def findLowest(proj):
    lowestRank = 0;
    rankIndex = None;
    for i in len(proj.memList):
        if(proj.memList[i].currRank < lowestRank):
            rankIndex = i;
            lowestRank = proj.memList[i].currRank
    return proj.memList.pop(rankIndex)



                
            

            


