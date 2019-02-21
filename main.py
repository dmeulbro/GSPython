import GSMatch.py
import array
import sys

class Student:
    def __init__(myStudent, studID, rList, paired, pProject, currRank):
        myStudent.studID = studID
        myStudent.rList = array.array('b')
        myStudent.paired = paired
        myStudent.pProject = pProject
        myStudent.currRank = currRank

class Project:
    def __init__(myProject, projNum, pList, numMems, maxSize, memList):
        myProject.projNum = projNum
        myProject.pList = array.array('i')
        myProject.numMems =numMems
        myProject.maxSize = maxSize




if __name__=="__main__"
    studList = []
    for i in range(0,20):
        studList.append(Student(i))
    

