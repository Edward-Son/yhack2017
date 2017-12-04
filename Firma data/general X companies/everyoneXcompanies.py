import xml.etree.ElementTree as ET


totalPeopleCount = 0
totalPeopleInBadCompaniesATM = 0
totalPeopleInBadCompaniesPast = 0
hasBeen = 0
badCompanies = open('/Users/li-tigre/Downloads/500companies', 'r')
hasBeencompaniesTotal = 0

for x in range(1, 21):
	tree = ET.parse('/Users/li-tigre/Desktop/FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds'+ str(x)+'.xml')
	root = tree.getroot()
	writeFile = open('badCompaniesCount' + str(x), 'w')

	for f in root[0]:
		totalPeopleCount += 1
		count = 0
		for currEmps in f[2]:
			with open('/Users/li-tigre/Downloads/500companies', 'r') as fpbad:
				for names in fpbad:
					if str(currEmps.attrib['orgNm']) == names[:-3]:
						totalPeopleInBadCompaniesATM += 1
						count += 1
						break
		for pastEmps in f[6]:
			# print(pastEmps)
			with open('/Users/li-tigre/Downloads/500companies', 'r') as fbad:
				for cnames in fbad:
					if str(pastEmps.attrib['orgNm']) == cnames[:-3]:
						totalPeopleInBadCompaniesPast += 1
						count += 1
						break
		writeFile.write(str(count)+ '\n')
		if count:
			hasBeen += 1
			hasBeencompaniesTotal += count

averageBadCompanies = open('averageBadCompanies', 'w')
averageBadCompanies.write('been in bad companie: ' + str(hasBeen/totalPeopleCount) + '\n')
averageBadCompanies.write('average # of bad companies in the past/present: ' + str((totalPeopleInBadCompaniesPast + totalPeopleInBadCompaniesATM)/totalPeopleCount) + '\n')
averageBadCompanies.write('average# oc bad companies someone has worked for if they have worked for a bad company' + str(hasBeencompaniesTotal/hasBeen))

				
				

