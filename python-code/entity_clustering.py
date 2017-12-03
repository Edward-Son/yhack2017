from collections import Counter
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

class Clusterer(object):
	def __init__(self, filename):
		self.entities = {}
		with open(filename) as f:
			for line in f:
				self.entities[line.strip('\n')] = {}

	def tokenize_all(self):
		"""
		lower case and tokenize
		"""
		for e in self.entities:
			self.entities[e]["tokens"] = e.replace(',', '').lower().split(' ')

	def tf_idf(self):
		self.word_to_int = {}
		self.int_to_word = {}
		doc_frqcy = Counter()
		#get freq of every word across all docs (posts)
		for e in self.entities:
			word_set = set()

			for w in self.entities[e]["tokens"]:
				word_set.add(w)
				if w not in self.word_to_int:
					number = len(self.word_to_int)
					self.word_to_int[w] = number
					self.int_to_word[number] = w
			for w in word_set:
				doc_frqcy[w] += 1

		for e in self.entities:
			tf_idf_words = {}
			w_count = Counter()

			for w in self.entities[e]["tokens"]:
				w_count[w] += 1

			for w in w_count:
				tf_idf_words[self.word_to_int[w]] = w_count[w] * np.log10(np.divide(len(self.entities), doc_frqcy[w]))

			self.entities[e]["tf-idf-scores"] = tf_idf_words

		self.doc_frqcy = doc_frqcy

	def similar_entities(self, treshold=0.75):
		self.int_to_entities = {}
		A = np.zeros((len(self.entities), len(self.word_to_int)))
		for i,e in enumerate(self.entities):
			self.int_to_entities[i] = e
			for w in self.entities[e]["tf-idf-scores"]:
				A[i][w] = self.entities[e]["tf-idf-scores"][w]
		A_sparse = sparse.csr_matrix(A)
		pairs = set()
		results = cosine_similarity(A_sparse)
		for i,e in enumerate(results):
			print(i)  
			for j,e2 in enumerate(results[i]):
				if i != j:
					if results[i][j] > treshold:                                                            
						pairs.add((i, j))   

		return pairs


