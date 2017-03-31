# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 21:43:34 2015
 
@author: shuchowdhury
"""
 
 
from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import csv
import itertools
import re
import time
from dateutil.parser import parse
from datetime import datetime
import sys
import os
import re
 
 
dirname='C:/Your directory name/email/xx'
outdirname='C:/Your directory name/textanalysis'
csvfilename='ABBY_S_CHANCEY.csv'
headerline=re.compile("^([^:]+):\s+(.*)")
 
 
class parse_emails:
   
  def __init__(self, dirname, outdirname, csvfilename):
    self.dirname = dirname
    self.outdirname = outdirname
    self.csvfilename = csvfilename
    self.emailfiles = os.listdir(self.dirname)
    #with open(csvfile, 'w') as out_file:
   
    out_file = open(outdirname + "/" + csvfilename, 'w')
    writer = csv.writer(out_file)
    writer.writerow(('Inbox','MailBox','Date','tagline'))
    for filename in self.emailfiles:
        emailfile = self.dirname + "/" + filename
        #csvfile = self.outdirname + "/" + self.csvfilename
        print (emailfile)
 
        i =0
        f = open(emailfile)
       
        for line in f:
           
            i = i+len(line)
            line = line.rstrip()
            line = line.replace('<','')
            line = line.replace('>','')
            line = line.replace('"','')
            line=re.sub('<[^>]*>', '', line)
            #print line
            if re.search('^Inbox-ID:', line):
                lth1= len(line)
                ib = line[0:lth1]
                print (ib)
            if re.search('^MAIL-BOX:', line):
                lth2= len(line)
                mb = line[0:lth2]
                print (mb)
#            if re.search('^Content-Type:', line):
#                lth2= len(line)
#                ct = line[0:lth2]
#                print 'CT'
#                print ct
            s = re.search(r'^Date: ', line)
            #if re.search('^Date: ', line):
            if s:
#                print (s.group())
                tt=line.rfind('Date:')
#                print tt
                #.group()
                line = line.replace('Creation Date : ','')
                lth= len(line)
#                print line[0:lth]
                epochDT = line[5:16]
                epochDT = epochDT.replace(' ','')
                if (epochDT.isdigit() ):
                    epochDT = float(epochDT)
                    dtt=time.strftime('%m/%d/%Y',time.gmtime(epochDT))
                else:
                    dtt = line.replace('Date:','')
                    dtt = parse(dtt).date()
                    dtt = dtt.strftime("%m/%d/%Y")
              
#                print dtt
           
          
        r = open(emailfile)
        raw = r.read()
        dd =raw.find('Content-Type:')
#        print i
        PT = raw[dd:i] 
        writer.writerow((ib,mb,dtt,PT) )
        #writer.writerow(('\n') )
       
        f.close()
        r.close()   
        break
           
            
                 #j=j+1
    out_file.close()    
#   
                  
    
if __name__ == '__main__':
#  args = sys.argv[1:]
#  if (len(args) != 3):
#    print("Usage: python arrange_headers.py <Directory for the E-mail files> <Output Directory> <csvfilename>")
#    sys.exit(1)
#  dirname = args[0]
#  outdirname = args[1]
#  csvfilename = args[2]
  ah = parse_emails(dirname, outdirname, csvfilename)
 
