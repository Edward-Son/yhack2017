import xml.etree.ElementTree as ET

peoplecount = 0
totalDRP = 0

list = ['hasRegAction', 'hasTermination']

for x in range (1, 21):
	bad = open('/Users/li-tigre/Downloads/found-bad-people/' + str(x) + '-common-people', 'r')
	exams = open('numofdrps'+ str(x), 'w')
	tree = ET.parse('/Users/li-tigre/Desktop/FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds'+ str(x)+'.xml')
	root = tree.getroot()

	# list = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']

	with bad as fp:
		for line in fp:
			peoplecount += 1
			listindex = line.split()
			index = int(listindex[-1])
			badCount = 0
			for drp in root[0][index][8]:
				for x in range (0, 1):
				# write(str(n.attrib[list[x]]) + '\n')
				# print(n.attrib[str(list[x])])
					if str(drp.attrib[str(list[x])]) == 'Y':
						badCount += 1
						totalDRP += 1
				exams.write(str(badCount) + '\n')


average = open('averageDRP1', 'w')
average.write(str(totalDRP/peoplecount))