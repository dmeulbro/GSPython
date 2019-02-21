import array
import sys
import random

class Student:
    def __init__(myStudent, studID):#, rList, paired, pProject, currRank):
        myStudent.studID = studID
#        myStudent.rList = rList
#        myStudent.paired = paired
#        myStudent.pProject = pProject
#        myStudent.currRank = currRank

#class Project:
#   def __init__(myProject, projNum, pList, numMems, maxSize, memList):
#        myProject.projNum = projNum
#        myProject.pList = array.array('i')
#        myProject.numMems =numMems
#        myProject.maxSize = maxSize


def genStudents():
    studList = []
    for i in range(0,20):
        studList.append(Student(i+1)) 


def genRankedlist():
    for i in range(1,6):
        print random.randint(1,5)
        
    

genStudents()
genRankedlist()
