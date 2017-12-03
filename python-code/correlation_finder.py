class Finder(object):
	def __init__(self):
		companies = []
		with open('./common_companies') as f:
			for line in f:
				companies.append(line.strip('\n').lower())

		companies_to_percent = {}
		with open('./bad_percentage_raw') as f:
			for line in f:
				data = line.strip('\n').lower().split('\t')
				companies_to_percent[data[0]] = data[1]
		companies_to_infractions = {}
		with open('./company_infractions') as f:
			for line in f:
				data = line.strip('\n').lower().split('\t')
				companies_to_infractions[data[0]] = data[1]

		self.pairs = []
		for c in companies:
			try:
				self.pairs.append((companies_to_infractions[c], companies_to_percent[c]))
			except:
				print(c)


	def get_pairs(self):
		return self.pairs