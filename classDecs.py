import array
import sys
import random
from math import ceil

class Student:
    def __init__(myStudent, studID, rList, paired, pProject, currRank):
        myStudent.studID = studID       # student ID
        myStudent.rList = rList         # ranked list
        myStudent.paired = paired       # paired (TRUE OR FALSE)
        myStudent.pProject = pProject   # paired project number
        myStudent.currRank = currRank   # current rank in placed proj

class Project:
   def __init__(myProject, projNum, pList, numMems, maxSize, memList):
        myProject.projNum = projNum     # project ID
        myProject.pList = pList         # preference list of studs
        myProject.numMems =numMems      # number of current mems
        myProject.maxSize = maxSize     # self-explanatory
        myProject.memList = memList     # List of members

# generate project list with all parameters
def genProjects(numStudents, numProjects):
    projList = []
    for i in range(0,numProjects):
        pList = genRankedlist(numStudents)
        projList.append(Project(i+1, pList, int(0), ceil(float(numStudents)/float(numProjects)), None))
    return projList

# generate student list with all parameters
def genStudents(numStudents, numProjects):
    studList = []
    for i in range(0,numStudents):
        rList = genRankedlist(numProjects);
        studList.append(Student(i+1, rList, False, None, None))
    return studList

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

