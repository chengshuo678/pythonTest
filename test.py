# print("hello,world")
# class MyClass(object):
#     common = 10
#     def __init__(self,arg):
#         self.myvariable = arg
#     def myfunction(self,arg1,arg2):
#         return self.myvariable
# classInstance = MyClass(123)
# result = classInstance.myfunction(1,1)
# print(result)
# print(classInstance.common)

# def myFunction():
#     try:
#         10/0
#     except ZeroDivisionError:
#         print("error")
#     else:
#         pass
#     finally:
#         print("We are done with that")
# myFunction()

# import random
# from time import clock
#
# randomint = random.randint(1,100)
# print(type(clock()))
# print(randomint)

import pickle
# mylist = ["This","is",4,13327]
# mylist = "11111"
# myfile = open(r"C:\\test.bat","wb")
# pickle.dump(mylist,myfile)
# myfile.close()
#
# myfile = open(r"C:\\test.bat","w")
# myfile.write(mylist)
# myfile.close();

# myfile = open(r"C:\\test.bat")
# loadRes = pickle.load(myfile, "rb")
# print(loadRes)

#导入pymysql的包
# import pymysql
# try:
# #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#   conn=pymysql.connect(host='localhost',user='root',passwd='root',db='mytest',port=3306,charset='utf8')
#   cur=conn.cursor()#获取一个游标
#   cur.execute('select * from test')
#   data=cur.fetchall()
#   print(data)
#
#   for d in data :
#     #注意int类型需要使用str函数转义
#     print(d)
#     print(d[0])
#     print(d[1])
#     print(d[2])
#     print(d[3])
#     print("ID: "+str(d[0])+"  username： "+str(d[1])+"  password： "+str(d[2])+"  uuid： "+str(d[3]))
#
#   cur.close()#关闭游标
#   conn.close()#释放数据库资源
# except  Exception :print("发生异常")

# coding=UTF-8
import nltk
nltk.download()
# from nltk.corpus import brown
#
# # This is a fast and simple noun phrase extractor (based on NLTK)
# # Feel free to use it, just keep a link back to this post
# # http://thetokenizer.com/2013/05/09/efficient-way-to-extract-the-main-topics-of-a-sentence/
# # Create by Shlomi Babluki
# # May, 2013
#
# # This is our fast Part of Speech tagger
# #############################################################################
# brown_train = brown.tagged_sents(categories='news')
# regexp_tagger = nltk.RegexpTagger(
#   [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
#    (r'(-|:|;)$', ':'),
#    (r'\'*$', 'MD'),
#    (r'(The|the|A|a|An|an)$', 'AT'),
#    (r'.*able$', 'JJ'),
#    (r'^[A-Z].*$', 'NNP'),
#    (r'.*ness$', 'NN'),
#    (r'.*ly$', 'RB'),
#    (r'.*s$', 'NNS'),
#    (r'.*ing$', 'VBG'),
#    (r'.*ed$', 'VBD'),
#    (r'.*', 'NN')
#    ])
# unigram_tagger = nltk.UnigramTagger(brown_train, backoff=regexp_tagger)
# bigram_tagger = nltk.BigramTagger(brown_train, backoff=unigram_tagger)
# #############################################################################
# # This is our semi-CFG; Extend it according to your own needs
# #############################################################################
# cfg = {}
# cfg["NNP+NNP"] = "NNP"
# cfg["NN+NN"] = "NNI"
# cfg["NNI+NN"] = "NNI"
# cfg["JJ+JJ"] = "JJ"
# cfg["JJ+NN"] = "NNI"
#
#
# #############################################################################
# class NPExtractor(object):
#   def __init__(self, sentence):
#     self.sentence = sentence
#
#   # Split the sentence into singlw words/tokens
#   def tokenize_sentence(self, sentence):
#     tokens = nltk.word_tokenize(sentence)
#     return tokens
#
#   # Normalize brown corpus' tags ("NN", "NN-PL", "NNS" > "NN")
#   def normalize_tags(self, tagged):
#     n_tagged = []
#     for t in tagged:
#       if t[1] == "NP-TL" or t[1] == "NP":
#         n_tagged.append((t[0], "NNP"))
#         continue
#       if t[1].endswith("-TL"):
#         n_tagged.append((t[0], t[1][:-3]))
#         continue
#       if t[1].endswith("S"):
#         n_tagged.append((t[0], t[1][:-1]))
#         continue
#       n_tagged.append((t[0], t[1]))
#     return n_tagged
#
#   # Extract the main topics from the sentence
#   def extract(self):
#     tokens = self.tokenize_sentence(self.sentence)
#     tags = self.normalize_tags(bigram_tagger.tag(tokens))
#     merge = True
#     while merge:
#       merge = False
#       for x in range(0, len(tags) - 1):
#         t1 = tags[x]
#         t2 = tags[x + 1]
#         key = "%s+%s" % (t1[1], t2[1])
#         value = cfg.get(key, '')
#         if value:
#           merge = True
#           tags.pop(x)
#           tags.pop(x)
#           match = "%s %s" % (t1[0], t2[0])
#           pos = value
#           tags.insert(x, (match, pos))
#           break
#     matches = []
#     for t in tags:
#       if t[1] == "NNP" or t[1] == "NNI":
#         # if t[1] == "NNP" or t[1] == "NNI" or t[1] == "NN":
#         matches.append(t[0])
#     return matches
#
#
# # Main method, just run "python np_extractor.py"
# def main():
#   sentence = "Swayy is a beautiful new dashboard for discovering and curating online content."
#   np_extractor = NPExtractor(sentence)
#   result = np_extractor.extract()
#   print
#   "This sentence is about: %s" % ", ".join(result)
#
#
# if __name__ == '__main__':
#   main()