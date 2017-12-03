
class Cleaner(object):
	def __init__(self, filename):
		self.data ={}
		with open(filename) as f:
			for line in f:
				r = line.strip('\n').split('\t')
				self.data[r[0]] = int(r[1])

	def clean_save(self, newfile):
		newData = {}
		for k in self.data:
			newK = k.lower().replace(',', '')
			newK = newK.replace('.', '')
			newK = newK.replace('llc', '')
			if newK in newData:
				newData[newK] += self.data[k]
			else:
				newData[newK] = self.data[k]

		with open(newfile, 'wt', encoding='utf-8') as f:
			for k in newData:
				f.write('{0}\t{1}\n'.format(k, newData[k]))

