import random
import array
import sys

def matchProj (studList, projList):
    if(len(projList) == 0):
        return "ERROR: NO PROJECTS"
    if(len(studList) == 0):
        return "ERROR: NO STUDENTS"
    for i in range(0,len(studList)):
        studList[i].paired = False
        studList[i].currRank = None
        studList[i].pProject = None

    for i in range(0,len(projList)):
        projList[i].memList = []

    while(len(studList) != 0):
        currStud = studList.pop(0)
        
        while(len(currStud.rList) != 0):
            topProj = currStud.rList.pop(0) - 1
            currStud.currRank = projList[topProj].pList.index(currStud.studID)
            if(projList[topProj].numMems != projList[topProj].maxSize):
                projList[topProj].numMems += 1
                currStud.paired = True
                currStud.pProject = topProj + 1
                projList[topProj].memList.append(currStud)
                break
            else:
                lowestStud = findLowest(projList[topProj])
                if(currStud.currRank < lowestStud.currRank):
                    projList[topProj].memList.append(lowestStud)
                    currStud.currRank = 0
                else:
                    #got matched
                    currStud.paired = True
                    currStud.pProject = topProj + 1
                    projList[topProj].memList.append(currStud)

                    #unmatched
                    lowestStud.paired = False
                    lowestStud.currRank = 0
                    lowestStud.pProject = None
                    studList.append(lowestStud)
                    break

    return projList

def findLowest(proj):
    lowestRank = 50000;
    rankIndex = None;
    for i in range(len(proj.memList)):
        if(proj.memList[i].currRank < lowestRank):
            rankIndex = int(i);
            lowestRank = proj.memList[i].currRank
    return proj.memList.pop(rankIndex)



                
            

            


