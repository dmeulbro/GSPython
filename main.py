import classDecs
import GSMatch

def main():
    projList = classDecs.genProjects(60,11)
    studList = classDecs.genStudents(60,11)

    for i in range(len(studList)):
        print str(studList[i].studID) + ":"
        print studList[i].rList
    projList = GSMatch.matchProj(studList, projList)


    for i in range(len(projList)):
        proj = i+1
        print "\n"
        print proj
        print "=-=-=-=-=-=-=-=-="
        for j in range(len(projList[i].memList)):
            print projList[i].memList[j].studID
    
        print "=-=-=-=-=-=-=-=-="




if __name__=='__main__':
    main()
