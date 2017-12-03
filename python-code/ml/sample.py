import xml.etree.ElementTree as ET
import numpy as np
from sklearn.externals import joblib
from sklearn import svm

clf = joblib.load('persistenceTests.pkl')

root = ET.parse("./FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds2.xml").getroot()

count = 0

testdata = np.zeros(shape=(10,5))

for line in root[0]:
	#feature 1 : city
	try:
		city = line[2][0].attrib['city']
	except:
		city = 'NAcity'

	#if the key doesnt exist, add to dictionnary
	if not dic.has_key(city):
		dic[city] = j
		j += 1

	#feature 2 : organisation name
	try:
		orgName = line[2][0].attrib['orgNm']
	except:
		orgName = 'NAorg'

	#if the key doesnt exist, add to dictionnary
	if not dic.has_key(orgName):
		dic[orgName] = j
		j += 1

	#feature 3 : branch location
	try:
		branchCity = line[2][0][1][0].attrib['city']
	except:
		branchCity = 'NAbranchcity'

	#if the key doesnt exist, add to dictionnary
	if not dic.has_key(branchCity):
		dic[branchCity] = j
		j += 1

	#feature 4: number of exams taken
	try:
		numExams = 0
		for exam in line[3]:
			numExams += 1
		exams = str(numExams) + 'examsTaken'
	except:
		exams = 'NAexams'

	#if the key doesnt exist, add to dictionnary
	if not dic.has_key(exams):
		dic[exams] = j
		j += 1


	#feature 5 : has other business?
	try:
		otherBus = line[7][0].attrib['desc']
		otherBus = 'YesOtherBusiness'
	except:
		otherBus = 'NAOtherBusiness'

	#if the key doesnt exist, add to dictionnary
	if not dic.has_key(otherBus):
		dic[otherBus] = j
		j += 1

	#update the image data
	testdata[count] = [dic[city],dic[orgName],dic[branchCity],dic[exams],dic[otherBus]]

	count += 1

	if count >= 10 :
		break


print("length: " + str(len(testdata)))
with open("sampleResults", 'w') as f :
	results = clf.predict(testdata)
	for i in results:
		f.write(str(i) + "\n")

joblib.dump(clf, "sampleResultsPersistence.pkl")




