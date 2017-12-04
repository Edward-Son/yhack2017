import xml.etree.ElementTree as ET


totalPeopleCount = 0
totalPeopleInBadCompaniesATM = 0
totalPeopleInBadCompaniesPast = 0
hasBeen = 0
badCompanies = open('/Users/li-tigre/Downloads/500companies', 'r')
hasBeencompaniesTotal = 0


for x in range(1, 21):
	bad = open('/Users/li-tigre/Downloads/found-bad-people/' + str(x) + '-common-people', 'r')
	tree = ET.parse('/Users/li-tigre/Desktop/FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds'+ str(x)+'.xml')
	root = tree.getroot()
	writeFile = open('badCompaniesCount' + str(x), 'w')

	with bad as fp:
		for line in fp:
			totalPeopleCount += 1
			people = line.split()
			index = int(people[-1])
			count = 0
			for currEmps in root[0][index][2]:
				with open('/Users/li-tigre/Downloads/500companies', 'r') as fpbad:
					for names in fpbad:
						if str(currEmps.attrib['orgNm']) == names[:-3]:
							totalPeopleInBadCompaniesATM += 1
							count += 1
						# fullCompname = names.split()
							# print(names[:-3])
							# print(currEmps.attrib['orgNm'])
						# if str(currEmps.attrib['orgNm']) == 
			for pastEmps in root[0][index][6]:
				# print(pastEmps)
				with open('/Users/li-tigre/Downloads/500companies', 'r') as fbad:
					for cnames in fbad:
						if str(pastEmps.attrib['orgNm']) == cnames[:-3]:
							totalPeopleInBadCompaniesPast += 1
							count += 1
			writeFile.write(str(count)+ '\n')
			if count:
				hasBeen += 1
				hasBeencompaniesTotal += count

averageBadCompanies = open('averageBadCompanies', 'w')
averageBadCompanies.write('been in bad companie: ' + str(hasBeen/totalPeopleCount) + '\n')
averageBadCompanies.write('average # of bad companies in the past/present: ' + str((totalPeopleInBadCompaniesPast + totalPeopleInBadCompaniesATM)/totalPeopleCount) + '\n')
averageBadCompanies.write('average# oc bad companies someone has worked for if they have worked for a bad company' + str(hasBeencompaniesTotal/hasBeen))


				
				

