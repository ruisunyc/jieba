# -*- coding: utf-8 -*-
from distutils.core import setup
LONGDOC = """
jieba
=====
“结巴”中文分词：做最好的 Python 中文分词组件
"Jieba" (Chinese for "to stutter") Chinese text segmentation: built to
be the best Python Chinese word segmentation module.
GitHub: https://github.com/ruisunyc/jieba
特点
====
-  支持三种分词模式：
   -  精确模式，试图将句子最精确地切开，适合文本分析；
   -  全模式，把句子中所有的可以成词的词语都扫描出来,
      速度非常快，但是不能解决歧义；
   -  搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
-  支持繁体分词
-  支持自定义词典
-  MIT 授权协议
安装说明
========
   python setup.py install
-  手动安装：将 jieba 目录放置于当前目录或者 site-packages 目录
-  通过 ``import jieba`` 来引用
"""

setup(name='jieba',
      version='1.0',
      description='Chinese Words Segmentation Utilities',
      long_description=LONGDOC,
      author='rui',
      author_email='1527717978@qq.com',
      url='https://github.com/ruisunyc/jieba',
      license="MIT",
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='NLP,tokenizing,Chinese word segementation',
      packages=['jieba'],
      package_dir={'jieba':'jieba'},
      package_data={'jieba':['*.*','finalseg/*','analyse/*','posseg/*', 'lac_small/*.py','lac_small/*.dic', 'lac_small/model_baseline/*']}
)