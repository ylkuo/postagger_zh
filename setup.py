#!/usr/bin/env python
from setuptools import setup

version_str = '1.0a1'

setup(
    name = 'POSTagger_Zh',
    version = version_str,
    description = 'A libirary for Chinese word segmentation and pos tagging.',
    author = "Yen-Ling Kuo, NTU iAgents Lab",
    author_email = 'r98922037@csie.ntu.edu.tw',
    packages=['postagger_zh'],
    package_data={'postagger_zh': ['models/*', 'lib/*']},
    install_requires=['nltk'],
)
