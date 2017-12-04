import xml.etree.ElementTree as ET


# bad = open('/Users/li-tigre/Downloads/found-bad-people/20-common-people', 'r')
# f = open('/Users/li-tigre/Desktop/FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds1.xml')
peoplecount = 0
examcount = 0

##----------------------
# for x in range (1, 21):
# 	exams = open('noExam'+ str(x), 'w')
# 	tree = ET.parse('/Users/li-tigre/Desktop/FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds'+ str(x)+'.xml')
# 	root = tree.getroot()

# 	# list = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']

# 	for f in root[0]:
# 		list = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']
# 		peoplecount += 1
# 		for n in f[3]:
# 			if n.attrib['exmNm'] in list:
# 				examcount += 1
# 				list.remove(n.attrib['exmNm'])
# 			# print(n.attrib['exmNm'])

# 		for item in list:
# 			exams.write(str(item) + '\n')
# 		# exams.write(str(list) + '\n')

# 	# exams.write(str(examcount/peoplecount))

# average = open('averageExamTaken', 'w')
# average.write(str(examcount/peoplecount))
##------------------------


##for bad people
for x in range (1, 21):
	bad = open('/Users/li-tigre/Downloads/found-bad-people/' + str(x) + '-common-people', 'r')
	exams = open('noExam'+ str(x), 'w')
	tree = ET.parse('/Users/li-tigre/Desktop/FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds'+ str(x)+'.xml')
	root = tree.getroot()


	with bad as fp:
		for line in fp:
			examList = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']
			peoplecount += 1
			list = line.split()
			index = int(list[-1])
			# print(root[0][index][3].attrib['exmNm'])
			for exam in root[0][index][3]:
				# print(exam.attrib['exmNm'])
				if exam.attrib['exmNm'] in examList:
					examcount += 1
					examList.remove(exam.attrib['exmNm'])
			for item in examList:
				exams.write(str(item) + '\n')

average = open('averageExamTaken', 'w')
average.write(str(examcount/peoplecount))


