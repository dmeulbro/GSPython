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

#class Project:
#   def __init__(myProject, projNum, pList, numMems, maxSize, memList):
#        myProject.projNum = projNum
#        myProject.pList = array.array('i')
#        myProject.numMems =numMems
#        myProject.maxSize = maxSize

# generate student list with all parameters
def genStudents(numStudents, numProjects):
    studList = []
    for i in range(0,numStudents):
        rList = genRankedlist(numProjects);
        studList.append(Student(i+1, rList, 0, None, None))
    printStudents(studList)

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
        newNum = random.randint(1,5)
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



#Test function calls
genStudents(20, 5)

