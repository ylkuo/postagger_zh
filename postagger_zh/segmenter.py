# -*- coding: utf-8 -*

import os
from xml.dom.minidom import parseString

class Segmenter():
	def segmentation(self, text):
		path = \
			os.path.abspath(__file__).replace(os.path.basename(__file__), '')
		cmd = 'echo "%s" | sh %slib/cmd_word_zh_as.sh %s' % (text, path, path)
		f = os.popen(cmd.encode('utf-8'))
		output_xml = f.readline()
		return self.parse_xml(output_xml)

	def parse_xml(self, xml_text):
		dom = parseString(xml_text)
		output_tokens = []
		for token in dom.getElementsByTagName('tok'):
			output_tokens.append(\
				token.toxml().replace('<tok>', '')\
				.replace('</tok>', '').encode('utf-8'))
		return output_tokens

if __name__ == '__main__':
	seg = Segmenter()
	text = u'今天天氣真好'
	for token in seg.segmentation(text):
		print token
