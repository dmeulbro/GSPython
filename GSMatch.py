import random
import array
import sys

def matchProj (studList, projList):
    if(len(projList) == 0):
        print "ERROR: NO PROJECTS"
        return
    if(len(studList) == 0):
        print "ERROR: NO STUDENTS"
        return 

    for i in range(0,len(studList)):
        studList[i].paired = False
        studList[i].currRank = None
        studList[i].pProject = None

    for i in range(0,len(projList)):
        projList[i].memList = []

    while(len(studList) != 0):
        currStud = studList.pop(0)                                              #get new student
        
        while(len(currStud.rList) != 0):
            topProj = currStud.rList.pop(0) - 1                                 #get top project 
            currStud.currRank = projList[topProj].pList.index(currStud.studID)  #get students rank in the project
            if(projList[topProj].numMems != projList[topProj].maxSize):         #project not full
                #assign to project
                projList[topProj].numMems += 1
                addStud(projList[topProj],currStud,topProj)
                break
            else:                                                               #project full
                lowestStud = findLowest(projList[topProj])
                if(currStud.currRank < lowestStud.currRank):                    #lowest ranked->move onto next proj
                    projList[topProj].memList.append(lowestStud)
                    currStud.currRank = 0
                else:                                                           #not lowest ranked
                    #got matched
                    addStud(projList[topProj], currStud, topProj)

                    #unmatched
                    unMatch(studList, lowestStud)
                    break
    return projList

def addStud(proj, currStud, topProj):
    currStud.paired = True
    currStud.pProject = topProj + 1
    proj.memList.append(currStud)

def unMatch(studList,lowestStud):
    lowestStud.paired = False
    lowestStud.currRank = 0
    lowestStud.pProject = None
    studList.append(lowestStud)
     

def findLowest(proj):
    lowestRank = 50000
    rankIndex = None
    for i in range(len(proj.memList)):
        if(proj.memList[i].currRank < lowestRank):
            rankIndex = int(i);
            lowestRank = proj.memList[i].currRank
    return proj.memList.pop(rankIndex)



                
            

            


