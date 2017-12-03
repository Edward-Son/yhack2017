import xml.etree.ElementTree as ET
import numpy as np
from sklearn.externals import joblib
from sklearn import svm

#get the number code for the people / get the samples
indices = []
i = 0
with open("./found-bad-people/1-common-people") as f:
	for line in f:
		
		indices.append(int(line.strip('\n').split(' ')[-1]))

		i += 1

#get the features
root = ET.parse("./FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds1.xml").getroot()

#preset numpy array size ahead of time to improve speed
i = 0
for line in root[0]:
	i += 1
target = np.zeros(shape=(i))
data = np.zeros(shape=(i,5))

#where all the numbers refer to a key
dic = {}
rowCounter = 0
j = 0


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

	#feature 4 : number of exams taken
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

	#feature 5 : has other  business?
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
	data[rowCounter] = [dic[city],dic[orgName],dic[branchCity],dic[exams],dic[otherBus]]

	#update target data
	if indices.count(rowCounter) == 0 :
		target[rowCounter] = 0
	else:
		target[rowCounter] = 1

	rowCounter += 1

#train model with second data set
indices = []
i = 0
with open("./found-bad-people/2-common-people") as f:
	for line in f:
		
		indices.append(int(line.strip('\n').split(' ')[-1]))

		i += 1

root2 = ET.parse("./FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds2.xml").getroot()

#get length of file
l = 0
for line in root2[0]:
	l += 1
#set the size of numpy array
data2 = np.zeros(shape=(l,5))

target2 = np.zeros(shape=(l))

rowCounter = 0

for line in root2[0]:

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
	data2[rowCounter] = [dic[city],dic[orgName],dic[branchCity],dic[exams],dic[otherBus]]

	#update target data
	if indices.count(rowCounter) == 0 :
		target2[rowCounter] = 0
	else:
		target2[rowCounter] = 1

	rowCounter += 1

#train model with first data set
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(data, target)
#train model with the second data set
clf.fit(data2, target2)


root3 = ET.parse("./FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds3.xml").getroot()

m = 0
for line in root3[0]:
	m += 1

data3 = np.zeros(shape=(l,5))

rowCounter = 0

for line in root3[0]:

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
	data3[rowCounter] = [dic[city],dic[orgName],dic[branchCity],dic[exams],dic[otherBus]]

	rowCounter += 1

#predict on sample data set

print("length: " + str(len(data3)))
with open("resultsFinal", 'w') as f :
	results = clf.predict(data3)
	for k in results:
		f.write(str(k) + "\n")

joblib.dump(clf, "finalPersistence.pkl")

# clf = joblib.load('finalPersistence.pkl')

