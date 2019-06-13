import classDecs
import GSMatch
import analysis
import copy
import csv
import math
import random

def main():
    j = 0
    countList   = []
    percList    = []
    studList_ref = [None] * 10
    projList_ref = [None] * 10
#    while j < 1000:
    projList    = classDecs.genProjects(50,10)
    studList    = classDecs.genStudents(50,10)
    while j < 2:
        studList_ref[j] = studList.copy()
        projList_ref[j] = projList.copy()
#    print str(studList_ref

    
#    while j< 10:
#        studList_ref[j] = copy.deepcopy(studList);
#        projList_ref[j] = copy.deepcopy(projList);

##    for i in range(len(studList)):
#        print str(studList[i].studID) + ":"
#        print studList[i].rList
#        print str(studListCpy[i].studID) + ":"
#        print studListCpy[i].rList 
#        print "\n"
#
#    max_size = math.floor(50/10)
#    print max_size
#
#    j = 0
#    projList_1 = GSMatch.matchProj(studList, projList, max_size)
#    projList_2 = GSMatch.matchProj(studListCpy, projListCpy, max_size)
#
##    while j < 10:
##        projList_ref[j] = GSMatch.matchProj(studList_ref[j], projList_ref[j], max_size)
##
##
#    for i in range(len(projList_1)):
#        proj = i+1
#        # proj 1
#        print "\n"
#        print proj
#        print "=-=-=-=-=-=-=-=-="
#        for j in range(len(projList_1[i].memList)):
#           print projList_1[i].memList[j].studID
#        print "=-=-=-=-=-=-=-=-="
#        # proj 2
#        print "\n"
#        print proj
#        print "=-=-=-=-=-=-=-=-="
#        for j in range(len(projList_2[i].memList)):
#           print projList_2[i].memList[j].studID
#        print "=-=-=-=-=-=-=-=-="
#
#for i in range(len(projList_2)):
#        proj = i+1
#        print "\n"
#        print proj
#        print "=-=-=-=-=-=-=-=-="
#        for j in range(len(projList_1[i].memList)):
#           print projList_2[i].memList[j].studID
#        print "=-=-=-=-=-=-=-=-="

        
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
