# -*- coding: utf-8 -*-

"""

"""

 

import nltk

import os,sys

import io

import csv

import numpy as np

import matplotlib.pyplot as plt

from matplotlib import style

from nltk import pos_tag

from nltk.tag import StanfordNERTagger

from nltk.tokenize import word_tokenize

from nltk.chunk import conlltags2tree

from nltk.tree import Tree

import codecs

import fnmatch

 

os.environ["JAVA_HOME"] = "C:/Program Files (x86)/Java/jdk1.6.0_45/bin"

os.environ["CLASSPATH"] = "C:/BigData/PII_Finder/stanford-ner"

os.environ["JAVAHOME"] = "C:/Program Files (x86)/Java/jdk1.6.0_45/bin"

 

style.use('fivethirtyeight')

 

 

dirname="C:/BigData/PII_Finder/xxxx/SFO/dlewin"

output_file="C:/BigData/PII_Finder/xxxx/SFO/out/xxxx.csv"

 

 

def process_text(txt_file):

               #raw_text = open("/usr/share/news_article.txt").read()

      print ("dirname File Name=",txt_file)

      #raw_text = open(dirname +'/'+ txt_file).read()

      #fl = open(dirname +'/'+ txt_file,'r')

#      with io.open(dirname +'/'+ txt_file,'r',encoding='utf-8',errors='ignore') as fl:

      with io.open( txt_file,'r',encoding='utf-8',errors='ignore') as fl:

         

          raw_text = fl.read()

          token_text = word_tokenize(raw_text)

      return token_text

 

# Stanford NER tagger   

def stanford_tagger(token_text):

               #st = StanfordNERTagger('/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', '/usr/share/stanford-ner/stanford-ner.jar', encoding='utf-8')

      st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz','stanford-ner.jar',encoding='utf-8')

      ne_tagged = st.tag(token_text)

      return(ne_tagged)


# NLTK POS and NER taggers  

def nltk_tagger(token_text):

               tagged_words = nltk.pos_tag(token_text)

               ne_tagged = nltk.ne_chunk(tagged_words)

               return(ne_tagged)

 

# Tag tokens with standard NLP BIO tags

def bio_tagger(ne_tagged):

                              bio_tagged = []

                              prev_tag = "O"

                              for token, tag in ne_tagged:

                                             if tag == "O": #O

                                                            bio_tagged.append((token, tag))

                                                            prev_tag = tag

                                                            continue

                                             if tag != "O" and prev_tag == "O": # Begin NE

                                                            bio_tagged.append((token, "B-"+tag))

                                                            prev_tag = tag

                                             elif prev_tag != "O" and prev_tag == tag: # Inside NE

                                                            bio_tagged.append((token, "I-"+tag))

                                                            prev_tag = tag

                                             elif prev_tag != "O" and prev_tag != tag: # Adjacent NE

                                                            bio_tagged.append((token, "B-"+tag))

                                                            prev_tag = tag

                              return bio_tagged

   

# Create tree      

def stanford_tree(bio_tagged):

               tokens, ne_tags = zip(*bio_tagged)

               pos_tags = [pos for token, pos in pos_tag(tokens)]

 

               conlltags = [(token, pos, ne) for token, pos, ne in zip(tokens, pos_tags, ne_tags)]

               ne_tree = conlltags2tree(conlltags)

               return ne_tree


 # Parse named entities from tree

def structure_ne(ne_tree):

               ne = []

               for subtree in ne_tree:

                              if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"

                                             ne_label = subtree.label()

                                             ne_string = " ".join([token for token, pos in subtree.leaves()])

                                             ne.append((ne_string, ne_label))

               return ne


def stanford_main():

   

    #print(structure_ne(stanford_tree(bio_tagger(stanford_tagger(process_text(txt_file))))))

    with io.open(output_file,'wb') as out_file:   

 

      writer = csv.writer(out_file)

      writer.writerow(['Document name','List of Person name in Document','List of Organization Name in document','List Of Location Name in Document','Uidentified yet important'])   

      for path, dirs, files in os.walk(dirname):

          for filename in files:

              if fnmatch.fnmatch(filename, '*.txt'):

                  """ CHECK IF THE FILE SIZE IS GREATER THAN ZERO OR ELSE IT WILL

                  FAIL AT stanford_tree"""

                 

                  

                  txt_file = os.path.abspath(os.path.join(path, filename))   

                  b = os.path.getsize(txt_file)

                  if b > 1 :

                   try:

#                 fileNames = os.listdir(dirname)

#                 for process_file in fileNames:

                        print (txt_file)

                        #txt_file = process_file

                        output = structure_ne(stanford_tree(bio_tagger(stanford_tagger(process_text(txt_file)))))

                       

                        per = []

                        person_name =''

                       

                        org = []

                        organization = ''

                       

                        loc =[]

                        location = ''   

                        

                        unid = []

                        unidentified = ''

                        #print(len(output))

                       

                        for i in range(len(output)):

                            if 'PERSON' in output[i]:

                                 """ Remove repeate words """

                                 if  output[i] not in per:

                                     per.append(output[i])

                            person_name = ''.join(map(str, per))

                           

                          

                              

                        #for i in range(len(output)):

                            if 'ORGANIZATION' in output[i]:

                                #print  output[i]

                                 """ Remove repeate words """

                                 if  output[i] not in org:

                                     org.append(output[i])               

                            organization = ''.join(map(str, org))

                               

                                

                                

                                

                        #for i in range(len(output)):

                            if 'LOCATION' in output[i]:

                                #print  output[i] 

                                 """ Remove repeate words """

                                 if  output[i] not in loc:               

                                     loc.append(output[i])

                            location = ''.join(map(str, loc))

                               

                            if ('LOCATION','ORGANIZATION','PERSON')  in output[i]:

                                unid.append(output[i])

                            unidentified = ''.join(map(str, unid))

                               

            #            print ('------------Persons-----------')       

                        person_name =   person_name.replace("u'",'')

                        person_name = person_name.replace('(','')    

                        person_name = person_name.replace(')','') 

                        person_name = person_name.replace('PERSON','')

                        person_name = person_name.replace("'",'')

                        person_name = person_name.replace('"','')

                        #print person_name

            #           

            #            print('')

            #            print('') 

                        

            #            print ('------------Organizations-----------')

                        organization =   organization.replace("u'",'')

                        organization = organization.replace('(','')    

                        organization = organization.replace(')','') 

                        organization = organization.replace('ORGANIZATION','')

                        organization = organization.replace("'",'')

                        person_name = person_name.replace('"','')

                        #print organization

                       

            #            print('')

            #            print('')

            #           

            #            print ('------------Location-----------')      

                        location =   location.replace("u'",'')

                        location = location.replace('(','')    

                        location = location.replace(')','') 

                        location = location.replace('LOCATION','')

                        location = location.replace("'",'')

                        person_name = person_name.replace('"','')

                        #print location

                   

            #            print('')

            #            print('')

            #           

            #            print ('------------Unidentified-----------')      

            #            print  unidentified

                               

                #    with io.open('Analysis.csv','w',encoding='ascii',errors='replace') as out_file:

                        writer.writerow([txt_file,person_name,organization,location,unidentified] )

                   except:

                        print("Bad File ")    

    out_file.close()       

            

def nltk_main():

      txt_file =''

      print(structure_ne(nltk_tagger(process_text(txt_file))))


if __name__ == '__main__':

    stanford_main()

    print('Done')

    #nltk_main()
