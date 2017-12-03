import xml.etree.ElementTree as ET

class Matcher(object):
	def __init__(self, filename, savefile):
		self.root = ET.parse(filename).getroot()
		self.savefile = savefile

	def save_names(self):
		with open(self.savefile, 'wt', encoding='utf-8') as f:
			for j,i in enumerate(self.root[0]):
				name = '{0} {1} {2}\n'.format(i[0].attrib['firstNm'], i[0].attrib['lastNm'], str(j))
				f.write(name)
