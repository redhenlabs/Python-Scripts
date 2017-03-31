# -*- coding: utf-8 -*-
"""

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
from time import gmtime, strftime
#import enchant
 
from bs4 import BeautifulSoup  as BSHTML
 
 
dirname='C:/Your directory name/all_inbox/in/test'
outdirname='C:/Your directory name/all_inbox/out'
csvfilename='test.csv'
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
    writer.writerow(('Inbox','MailBox','From_Name','Manual_Date','UPD_Date','tagline'))
    for filename in self.emailfiles:
        emailfile = self.dirname + "/" + filename
        #csvfile = self.outdirname + "/" + self.csvfilename
        print(emailfile)
 
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
                ib = ib.replace('Inbox-ID:', '')
                print (ib)
            if re.search('^MAIL-BOX:', line):
                lth2= len(line)
                mb = line[0:lth2]
                mb = mb.replace('MAIL-BOX:','')
                print (mb)
            if re.search('^From_Name:', line):
                frmnmlth= len(line)
                frmnm = line[0:frmnmlth]
                frmnm = frmnm.replace('From_Name:','')
                print (frmnm)
               
            if re.search('^Manual_Date:', line):
                mandtlnt= len(line)
                mandt = line[0:mandtlnt]
                mandt = mandt.replace('Manual_Date: ','')
                print (mandt)
                mandt= time.strptime(mandt,'%a %b %d %H:%M:%S %Y')
                mandt= time.strftime("%m/%d/%Y",mandt)
                print (mandt)
                   
            if re.search('^Date: ', line):
                tt=line.rfind('Date:')
                print (tt)
                #.group()
                line = line.replace('Creation Date : ','')
                lth= len(line)
                print (line[0:lth])
                epochDT = line[5:16]
                epochDT = epochDT.replace(' ','')
                if (epochDT.isdigit() ):
                    epochDT = float(epochDT)
                    dtt=time.strftime('%m/%d/%Y',time.gmtime(epochDT))
                else:
                    dtt = line.replace('Date:','')
                    dtt = parse(dtt).date()
                    dtt = dtt.strftime("%m/%d/%Y")
              
                print (dtt)
         
        r = open(emailfile)
       
        raw = r.read()
#        rep_spl =['\n','\t','\r']
      
        
        dd =raw.find('HEADER-END: YES')
#        dd = dd.replace('HEADER-END: YES','')
        print (i)
        print (dd)
        PT = raw[dd:1200]
      
        PT = PT.replace('HEADER-END: YES','')
        if  (PT not in 'boundary="alt'):
            PT =PT
        PT = PT.strip()
        if PT.find("word") == 0:
            PT = PT
        if not PT in 'boundary="alt':
            PT =PT
#        PT = BSHTML(PT)
#        PT = PT.getText()
       
       # PT = PT.font.contents[0].strip()
       # PT = PT.getText()
        PT = PT.replace('fontfamily','')
        PT = PT.replace('span','')
        PT = PT.replace('charset','')
        PT = PT.replace('Calibri','')
        PT = PT.replace('sansserif','')
        PT = PT.replace('Tahoma','')
        PT = PT.replace('fontsize','')
        PT = PT.replace('class=','')
        PT = PT.replace('style=','')
        PT = PT.replace('MsoNormalo','')
        PT = PT.replace('^[A-Za-z0-9_-]*$','')
        PT = PT.replace('^[{font-family:]*$','')
        PT = PT.replace('^[panose-]*$','')
        #PT = PT.replace('boundary','')
        PT = PT.replace('^boundary="alt','')
        PT = PT.replace('LibPST','')
        PT = PT.replace('/','')
        #PT = PT.replace('-','')
        PT = PT.replace('AAAAAAA','')
        PT = PT.replace('unique','')
        PT = PT.replace('iam','')
        PT = PT.replace('mso-style-type:','')
        PT = PT.replace('export-only','')
        PT = PT.replace('font-size','')
        PT = PT.replace('color:','')
        PT = PT.replace('purple','')
        PT = PT.replace('text-decoration','')
        PT = PT.replace('underline','')
        PT = PT.replace('font-family','')
        PT = PT.replace('texthtml','')
        PT = PT.replace('us-ascii','')
        PT = PT.replace('Font','')
        PT = PT.replace('Content-Type:','')
        #PT = PT.replace('\n','')
        PT = PT.replace('\t','')
        PT = PT.replace('\r','')
        PT = PT.rstrip()
        PT = PT.replace('<','')
        PT = PT.replace('>','')
#        PT = PT.replace('"','')
        PT=re.sub('<[^>]*>', '', PT)
        cleanr =re.compile('<.*?>')
        PT = re.sub(cleanr,'', PT)
        #print PT
        #PT = raw[dd:i]
#        PT = PT.strip() 
        
        writer.writerow((ib,mb,frmnm,mandt,dtt,PT) )
        #writer.writerow(('\n') )
       
        f.close()
        r.close()   
   
            
            
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
 
