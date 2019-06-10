import classDecs
import GSMatch
import analysis
import copy
import csv
import math

def main():
#    j = 0
    countList   = []
    percList    = []
#    while j < 1000:
    projList    = classDecs.genProjects(62,10)
    studList    = classDecs.genStudents(62,10)
#    studListCP  = copy.deepcopy(studList)

    for i in range(len(studList)):
        print str(studList[i].studID) + ":"
        print studList[i].rList
#        print studListCP[i].rList

    max_size = math.floor(62/10)
    print max_size

    projList = GSMatch.matchProj(studList, projList, max_size)


    for i in range(len(projList)):
        proj = i+1
        print "\n"
        print proj
        print "=-=-=-=-=-=-=-=-="
        for j in range(len(projList[i].memList)):
            print projList[i].memList[j].studID
        print "=-=-=-=-=-=-=-=-="

        
#    countList.append(analysis.numAnalysis(studListCP, projList))
#    percList.append(analysis.percentMatch(countList[j], 70))
#        j += 1

#    with open('countdata7.csv', 'wb') as myfile:
#        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#        for i in range(len(countList)):
#            wr.writerow(countList[i])
#    with open('percdata7.csv', 'wb') as myfile:
#        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#        for i in range(len(percList)):
#            wr.writerow(percList[i])


if __name__=='__main__':
    main()
