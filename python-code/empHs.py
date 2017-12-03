import xml.etree.ElementTree as ET

class HistoryFinder(object):
	def __init__(self, number):
		self.number = number
		self.indices = []
		with open("../found-bad-people/{0}-common-people".format(str(number))) as f:
			for line in f:
				self.indices.append(int((line.strip('\n').split(' ')[-1])))
		self.root = ET.parse('../IAPD/IA_Indvl_Feeds{0}.xml'.format(str(number))).getroot()

	def save_employers(self):
		employers = []
		for i in self.root[0]:
			for e in i[6]:
				employers.append(e.attrib['orgNm'])

		with open("./{0}-employers".format(self.number), 'wt', encoding='utf-8') as f:
			for e in employers:
				f.write(e + "\n")

		return employers

