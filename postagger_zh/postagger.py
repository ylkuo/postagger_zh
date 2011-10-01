# -*- coding: utf-8 -*

import os, pickle
from segmenter import Segmenter

class POSTagger():
	def __init__(self, tagger_pickle = None):
		if tagger_pickle == None:
			path = os.path.abspath(__file__)\
					.replace(os.path.basename(__file__), '')
        	tagger_pickle = \
				'%smodels/sinica_treebank_brill_aubt.pickle' % (path)
		self.tagger = pickle.load(open(tagger_pickle))
		self.segmenter = Segmenter()

	def tag(self, text):
		tokens = self.segmenter.segmentation(text)
		return self.tagger.tag(tokens)

if __name__ == '__main__':
	tagger = POSTagger()
	text = u'英國明年也開放台灣青年前往打工度假，且可打工兩年，\
			不少在學的年輕人認為，因為英國物價及生活費太高，\
			擔心打工甚至無法維持生活費，興趣缺缺；\
			但幾位三十歲以下的上班族則表示心動，有機會不排除前往。'
	for token, tag in tagger.tag(text):
		print token, tag
