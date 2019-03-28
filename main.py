import classDecs
import GSMatch
import analysis
import copy
import csv

def main():
    j = 0
    countList   = []
    percList    = []
    while j < 1000:
        projList    = classDecs.genProjects(50,10)
        studList    = classDecs.genStudents(50,10)
        studListCP  = copy.deepcopy(studList)

 #       for i in range(len(studList)):
    #        print str(studList[i].studID) + ":"
    #        print studList[i].rList
    #        print studListCP[i].rList
        projList = GSMatch.matchProj(studList, projList)


#        for i in range(len(projList)):
#            proj = i+1
#            print "\n"
#            print proj
#            print "=-=-=-=-=-=-=-=-="
#            for j in range(len(projList[i].memList)):
#                print projList[i].memList[j].studID
#    
#            print "=-=-=-=-=-=-=-=-="

        
        countList.append(analysis.numAnalysis(studListCP, projList))
        percList.append(analysis.percentMatch(countList[j], 50))
        j += 1

    with open('countdata.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for i in range(len(countList)):
            wr.writerow(countList[i])
    with open('percdata.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for i in range(len(percList)):
            wr.writerow(percList[i])


if __name__=='__main__':
    main()
