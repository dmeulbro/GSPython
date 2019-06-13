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

    projList    = classDecs.genProjects(50,10)
    studList    = classDecs.genStudents(50,10)
    while j < 10:
        print(j)
        studList_ref[j] = copy.deepcopy(studList)
        projList_ref[j] = copy.deepcopy(projList)
        j += 1 

    max_size = math.floor(50/10)

    j = 0
    while j < 10:
        projList_ref[j] = GSMatch.matchProj(studList_ref[j], projList_ref[j], max_size)
        j += 1

    for i in range(len(projList_ref)):
        print ("\n")
        print (j+1)
        print
        
#    for i in range(len(projList_1)):
#        proj = i+1
#        # proj 1
#        print ("\n")
#        print (proj)
#        print ("=-=-=-=-=-=-=-=-=")
#        for j in range(len(projList_1[i].memList)):
#           print (projList_1[i].memList[j].studID)
#        print ("=-=-=-=-=-=-=-=-=")
#        # proj 2
#        print ("\n")
#        print (proj)
#        print ("=-=-=-=-=-=-=-=-=")
#        for j in range(len(projList_2[i].memList)):
#           print (projList_2[i].memList[j].studID)
#        print ("=-=-=-=-=-=-=-=-=")
#        # proj 3
#        print ("\n")
#        print (proj)
#        print ("=-=-=-=-=-=-=-=-=")
#        for j in range(len(projList_3[i].memList)):
#           print (projList_3[i].memList[j].studID)
#        print ("=-=-=-=-=-=-=-=-=")
 
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
