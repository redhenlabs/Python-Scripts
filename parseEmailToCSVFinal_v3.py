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
import codecs
import io
 
 
from bs4 import BeautifulSoup  as BSHTML
 
 

headerline=re.compile("^([^:]+):\s+(.*)")
 
 
class parse_emails:
   
  def __init__(self, dirname, outdirname, csvfilename):
   self.dirname = dirname
   self.outdirname = outdirname
   self.csvfilename = csvfilename
   self.emailfiles = os.listdir(self.dirname)
    #with open(csvfile, 'w') as out_file:
 
   with io.open(outdirname + "/" + csvfilename,'w',encoding='ascii',errors='replace') as out_file:   
      writer = csv.writer(out_file)
      writer.writerow(('Inbox','MailBox','From_Name','Manual_Date','date','day','month','year','MMYYYY','tagline'))    
      for filename in self.emailfiles:
        emailfile = self.dirname + "/" + filename
        #csvfile = self.outdirname + "/" + self.csvfilename
        #emailfile =self.dirname + "/" +'1006'
        print(emailfile)
 
        i =0
        k =0
        #codecs.EncodedFile(emailfile, input, output,  errors='ignore')
        #f = codecs.open(emailfile, mode='r', errors='ignore')
        #l1= f.encode('utf-8').decode('utf-8','ignore').encode("utf-8")
        with io.open(emailfile,'r',encoding='utf-8',errors='ignore') as f:
        #f =f.replace("+\\","")
            for line in f:
                #print (line)
                i = i+len(line)
                line = line.rstrip()
                line = line.replace('<','')
                line = line.replace('>','')
                line = line.replace('"','')
                line=re.sub('<[^>]*>', '', line)
 
                if re.search('^Inbox-ID:', line):
                    lth1= len(line)
                    ib = line[0:lth1]
                    ib = ib.replace('Inbox-ID:', '')
#                    print (ib)
                               
                if re.search('^MAIL-BOX:', line):
                    lth2= len(line)
                    mb = line[0:lth2]
                    mb = mb.replace('MAIL-BOX:','')
#                    print (mb)
                    
                if re.search('^From_Name:', line):
                    frmnmlth= len(line)
                    frmnm = line[0:frmnmlth]
                    frmnm = frmnm.replace('From_Name:','')
#                    print (frmnm)
                   
                    
                if re.search('^Manual_Date:', line):
                    mandtlnt= len(line)
                    mandt = line[0:mandtlnt]
                    mandt = mandt.replace('Manual_Date: ','')
    #                print (mandt)
                    #mandt1= time.strptime(mandt,'%m %b %d %H:%M:%S %Y')
                    mandt1= time.strptime(mandt,'%m/%d/%Y %H:%M:%S')
 
                    DT = time.strftime("%m/%d/%Y",mandt1)
                    DD= time.strftime("%d",mandt1)
                    MM = time.strftime("%m",mandt1)
                    year = time.strftime("%Y",mandt1)
                    MMYYYY =time.strftime("%Y%m",mandt1)
                    #mandt= time.strftime("%m/%d/%Y",mandt1)
#                    print (mandt)
                   
#                if re.search('^Date: ', line):
#                    tt=line.rfind('Date:')
#    #                print (tt)
#                    #.group()
#                    line = line.replace('Creation Date : ','')
#                    lth= len(line)
#    #                print (line[0:lth])
#                    epochDT = line[5:16]
#                    epochDT = epochDT.replace(' ','')
#                    if (epochDT.isdigit() ):
#                        epochDT = float(epochDT)
#                        dtt=time.strftime('%m/%d/%Y',time.gmtime(epochDT))
#                    else:
#                        dtt = line.replace('Date:','')
#                        dtt = parse(dtt).date()
#                        dtt = dtt.strftime("%m/%d/%Y")
#    #              
#                    print (dtt)
                   
                if re.search('^HEADER-END: YES', line):
                    k =i
                    continue
#            print (k)
#            print (i)
              
#                      
#    #            cleanr =re.compile('<.*?>')
#    #            lin = re.sub(cleanr,'', lin)
#    #            lin = re.sub('\n\s*\n*', '',lin)
#    #            lin = lin.strip()
#    #            lin = lin.rstrip()
#    #            #lin = os.linesep.join([s for s in lin.splitlines() if s])
##           
        with io.open(emailfile,'r',encoding='ascii',errors='ignore') as r:
            raw = r.read()
            rep_txt = ['boundary-LibPST-iamunique','Content-Type:','AA','//','--alt---boundary-LibPST-iamunique','Content-Type: text/plain; charset="utf-8"','text/plain','charset="utf-8"']
            PT = raw[k:i]
            for wds in PT.split():
               lenwds = len(wds)
               #print (lenwds, '\t', wds)
               if (lenwds > 50):
                   PT= PT.replace(wds,'')
               else:
                   continue
              
#        #print (PT)
#          #for z in range(len(rep_txt)):
#        
#        #print (PT)
##        if  rep_txt[0] in PT:
            PT = PT.replace(rep_txt[0],'')
            PT = PT.replace(rep_txt[1],'')
            PT = PT.replace(rep_txt[2],'')
            PT = PT.replace(rep_txt[3],'')
            PT = PT.replace(rep_txt[4],'')
            PT = PT.replace(rep_txt[5],'')
            PT = PT.replace(rep_txt[6],'')
            PT = PT.replace(rep_txt[7],'')
            PT = BSHTML(PT,'lxml')
            PT = PT.getText()
            PT = PT.replace('[^a-zA-Z]','')
            PT = PT.replace('"','')
            PT = PT.replace(';','')
            PT = PT.replace('-','')
            PT = PT.replace('_','')
           PT = PT.replace('\n','')
            PT = PT.replace('\t','')
            PT = PT.replace('\r','')
            PT = PT.replace('\s.\s','')
            PT = PT.replace('<','')
            PT = PT.replace('>','')
            PT = PT.replace(r'^\s*$','')
            PT=re.sub('<[^>]*>', '', PT)
            cleanr =re.compile('<.*?>')
            PT = re.sub(cleanr,'', PT)
            #PT = re.sub('\n\s*\n*', '',PT)
            PT = PT.strip()
            PT = PT.rstrip()
#            nonascii = bytearray(range(0x80, 0x100))
#            PT = PT.translate(nonascii)
 
#            print ('WL==',lenwds,'==SEN==', PT)
            
#        #print ( 'i=', i, '\t', 'k=', k)
#        #print (PT)
#        #print (len(PT))
 
  
            writer.writerow((ib,mb,frmnm,mandt,DT,DD,MM,year,MMYYYY,PT) )
#        #writer.writerow(('\n') )
  
#        f.close()
#        r.close()  
        
        r.close()
        f.close()  
            
   out_file.close()        
                 #j=j+1
#       
if __name__ == '__main__':
  args = sys.argv[1:]
  if (len(args) != 3):
    print("Usage: python arrange_headers.py <Directory for the E-mail files> <Output Directory> <csvfilename>")
    sys.exit(1)
  dirname = args[0]
  outdirname = args[1]
  csvfilename = args[2]
  ah = parse_emails(dirname, outdirname, csvfilename)       
 
 
 
 