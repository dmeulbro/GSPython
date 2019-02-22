import array
import sys
import random

class Student:
    def __init__(myStudent, studID, rList, paired, pProject, currRank):#, rList, paired, pProject, currRank):
        myStudent.studID = studID
        myStudent.rList = rList
        myStudent.paired = paired
        myStudent.pProject = pProject
        myStudent.currRank = currRank

class Project:
   def __init__(myProject, projNum, pList, numMems, maxSize, memList):
        myProject.projNum = projNum
        myProject.pList = pList
        myProject.numMems =numMems
        myProject.maxSize = maxSize
        myProject.memList = memList

# generate project list with all parameters
def genProjects(numStudents, numProjects):
    projList = []
    for i in range(0,numProjects):
        pList = genRankedlist(numProjects)
        projList.append(Project(i+1, pList, None, (int(numStudents)/int(numProjects)), None))
    printProjects(projList)

# generate student list with all parameters
def genStudents(numStudents, numProjects):
    studList = []
    for i in range(0,numStudents):
        rList = genRankedlist(numProjects);
        studList.append(Student(i+1, rList, 0, None, None))
#    printStudents(studList)

# generate ranked list for students
def checkNum(num, projList):
    flag = 0
    for i in range (0,len(projList)):
        if(projList[i] == num):
            flag = 1
    return flag

def genRankedlist(numProjects):
    projList = []
    while(len(projList) < numProjects):
        newNum = random.randint(1,numProjects)
        if(checkNum(newNum, projList) == 0):
            projList.append(newNum);
    return projList

#test functions
def printStudents(studList):
    for i in range(0,len(studList)):
        print studList[i].studID
        print studList[i].rList
        print studList[i].paired
        print studList[i].pProject
        print studList[i].currRank
        print "\n"


def printProjects(projList):
    for i in range(0,len(projList)):
        print projList[i].projNum
        print projList[i].pList
        print projList[i].numMems
        print projList[i].maxSize
        print projList[i].memList
        print "\n"


#Test function calls
#genStudents(50, 10)
#genProjects(50, 10)

