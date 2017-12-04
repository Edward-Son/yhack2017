import xml.etree.ElementTree as ET

peoplecount = 0
totalDRP = 0

list = ['hasRegAction', 'hasTermination']

for x in range (1, 21):
	exams = open('numofdrps'+ str(x), 'w')
	tree = ET.parse('/Users/li-tigre/Desktop/FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds'+ str(x)+'.xml')
	root = tree.getroot()

	# list = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']

	for f in root[0]:
		peoplecount += 1
		# print(f[8])
		badCount = 0
		for n in f[8]:
			for x in range (0, 1):
				# write(str(n.attrib[list[x]]) + '\n')
				# print(n.attrib[str(list[x])])
				if str(n.attrib[str(list[x])]) == 'Y':
					badCount += 1
					totalDRP += 1
		exams.write(str(badCount) + '\n')
			# for i in n.attrib:
			# 	print(i)
			# print(n.attrib['type'])
			# for a in  :
			# 	print(a)

average = open('averageDRP1', 'w')
average.write(str(totalDRP/peoplecount))