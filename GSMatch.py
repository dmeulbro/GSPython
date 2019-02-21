def matchProj (studList, projList):
    for i in range(0,sizeof(studList)):
        studList[i].paired = false
        studList[i].pProject = void
    for i in range(0, sizeof(projList)):
        projList[i].numMems = 0
    
    while len(studList != 0):
        currentStud = studList.pop
        prefProj = currentStud.rList.pop - 1
        if( sizeof(projList[prefProj].numMems) != projList[prefProj].maxSize):
            currentStud.paired = true
            currentStud.pProject = prefProj
            projList[prefProj].numMems += 1
            #put student in list in ranked order
            pushStud(currentStud, projList[prefProf])
        else:
            #checkPlist returns true if currStud is ranked higher than a current team mem 
            if(checkPlist(currStud, projList[prefProj])):  
                currentStud.paired = true
                currentStud.pProject = prefProj
                pushStud(currentStud, projList[prefProj])
                lastStud = projList[prefProj].memList.pop
                studList.append(lastStud)
            else:
                studList.append(currentStud)



