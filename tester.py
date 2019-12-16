import os
import sys

wrong=0

def areSame(test, correct):
	if test=="":
		return 0
	if test[-1] == '\n':
		test = test[:-1]

	if test == correct:
		return 1

	return 0

for mapNo in range(10):
	for ruleNo in range(5):
		for genNo in range(20):
			print "Progress: " + str(mapNo*100 + ruleNo*20 + genNo) + "/1000 testcases"
			sys.stdout.write("\033[F")
			mapDir = "testcases/maps/map"+str(mapNo+1)+".txt"
			ruleDir = "testcases/rules/rules"+str(ruleNo+1)+".txt"


			cmd = "python the3.py " + mapDir + " " + ruleDir + " " + str(genNo); 
			stream = os.popen(cmd)
			output = stream.read()

			outputDir = "testcases/outputs/output"+str(mapNo+1)+str(ruleNo+1)+str(genNo)+".txt";
			
			f = open(outputDir,"r")
			correctOut = f.read()
			# I added
			#print output
			if areSame(output,correctOut) == 0:
				print "You failed at "+str(mapNo+1) + ".th map with " + str(ruleNo+1)+".th rule at "+str(genNo)+".th generation\n"
				print "Correct Output:\n"+correctOut
				print "\nYour Output:\n"+output
				wrong+=1


print "You failed " + str(wrong) + " times on 1000 testcases."
