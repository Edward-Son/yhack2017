import xml.etree.ElementTree as ET

badPeopleCount = 0
badPeopleExamTakenCount = 0

peopleCount = 0
examTakenCount = 0

results = open('Results', 'w')

#everyone
for x in range (1, 21):
	# bad = open('../found-bad-people/'+ x + 'common-people', 'r')
	# f = open('/Users/li-tigre/Desktop/FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds1.xml')
	exams = open('data/examNotTaken' + str(x), 'w')
	tree = ET.parse('../../FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds' + str(x) +'.xml')
	root = tree.getroot()

	list = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']

	for f in root[0]:
		list = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']
		peopleCount += 1
		for n in f[3]:
			examTakenCount += 1
			list.remove(n.attrib['exmNm'])
			# print(n.attrib['exmNm'])

		for item in list:
			exams.write(str(item) + '\n')
		# exams.write(str(list) + '\n')


results.write('examtaken/people: ' + str(examTakenCount/peopleCount) + '\n')


#bad people
for x in range (1, 21):
	bad = open('../found-bad-people/'+ str(x) + '-common-people', 'r')
	tree2 = ET.parse('../../FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds'+str(x)+'.xml')
	root2 = tree2.getroot()

	examsBad = open('data/examNotTakenFromBadPeople' + str(x), 'w')

	list = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']

	with bad as fp1:
		for line1 in fp1:
			list = ['Uniform Combined State Law Examination', 'Uniform Investment Adviser Law Examination', 'Uniform Securities Agent State Law Examination']
			badPeopleCount += 1
			array1 = line1.split()
			index1 = int(array1[-1])
			for exam1 in root2[0][index1][3]:
				badPeopleExamTakenCount += 1
				# if exam1.attrib['exmNm'] in list:
				list.remove(exam1.attrib['exmNm'])

			for item1 in list:
				examsBad.write(str(item1) + '\n')


results.write('examtaken by bad people/ bad people: ' + str(badPeopleExamTakenCount/badPeopleCount) + '\n')




##for bad people
# with bad as fp:
# 	for line in fp:
# 		list = line.split()
# 		# for n in root[0]:
# 			# print(list[2])
# 			# number = int(list[2])
# 		index = int(list[-1])
# 		# print(root[0][index][3].attrib['exmNm'])
# 		for exam in root[0][index][3]:
# 			exams.write(exam.attrib['exmNm'] + '\n')
		


