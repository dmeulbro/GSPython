import classDecs
import GSMatch

def main():
    projList = classDecs.genProjects(50,10)
    studList = classDecs.genStudents(50,10)

    GSMatch.matchProj(studList, projList)




if __name__=='__main__':
    main()
