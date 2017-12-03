import xml.etree.ElementTree as ET
import numpy as np
from sklearn.externals import joblib
from sklearn import svm

clf = joblib.load('persistenceTests.pkl')

root = ET.parse("./FINRAChallengeData/IAPD/IA_INDVL_Feed_10_11_2017.xml/IA_Indvl_Feeds2.xml").getroot()

count = 0

for line in root[0]:
	