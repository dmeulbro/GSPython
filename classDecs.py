import array

class Student:
    def __init__(myStudent, studID, rList, paired, pProject, currRank):
        myStudent.studID = studID
        myStudent.rList = array.array('b')
        myStudent.paired = paired
        myStudent.pProject = pProject
        myStudent.currRank = currRank

    def freeStudent(myStudent):
        myStudent.paired = false
        myStudent.pProject = void
        myStudent.rList.pop

class Project:
    def __init__(myProject, projNum, pList, numMems, maxSize, memList):
        myProject.projNum = projNum
        myProject.pList = array.array('i')
        myProject.numMems =numMems
        myProject.maxSize = maxSize
        myProject.memList = #learn to do two dimensional array

    def freeProject(myProject):
        myProject.numMems -= 1
        myProject.memList.pop

def checkPlist(student, project):
    for i in range(0, sizeof(project.memList


def pushStud(student, project, studList):
    studRank = getRank(student, project)
    if(sizeof(project.memList) == 0):
        project.memList.append(student)
        student.currRank = studRank
    else
        for i in range(0,sizeof(project.memList)):
            if(studRank > project.memList[i].currRank):
                project.memList.insert(i, student)
                break
return
                
                

def popStud(studList, project)

def getRank(student, project)

#still need to write checkPlist, popStud, getRank, and functions to generate students and projects
