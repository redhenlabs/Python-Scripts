# -*- coding: utf-8 -*-
"""

parse email and create a CSV file for further analysis using ML or AL

This parses unformated email and creates Header columns and contents for each mail file

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
 
 
dirname='<your inpput directory>'
csvfilename='<your final csv file name>.csv'
outdirname='<your output directory name>'
#csvfilename='tst3.csv'
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
      writer.writerow(('Inbox','MailBox','From_Name','Manual_Date','date','day','month','year','MMYYYY','From','To','CC','CC1','BCC','Subject','Content Limited To 30K Characters'))   
      for filename in self.emailfiles:
        emailfile = self.dirname + "/" + filename
        #csvfile = self.outdirname + "/" + self.csvfilename
        #emailfile =self.dirname + "/" +'1006'
        #print(emailfile)
 
        i =0
        k =0
        countTo =0
        countDt =0
        countFrm =0
        countCC =0
        countCc =0
        countBCC =0
        countSub =0
#        countDt =0
        HeaderEndLineNumber =0 
        startFrom =0
        endFrom =0
        startTo =0
        endTo = 0
        startCC =0
        endCC = 0
        startCc =0
        endCc = 0
        startBCC =0
        endBCC = 0
        startDate =0
        endDate = 0
        startSub =0
        countDDt =0
        startDDt =0
        ####
        countMSgID = 0
        startMSgID = 0
        startMSgid = 0
        countMSgid = 0
        counttidx = 0
        starttidx = 0
        countTIDX = 0
        startTIDX = 0
        countTopic = 0
        startTopic = 0
        countrcvd = 0
        startrcvd = 0
        countDKIM = 0
        startDKIM = 0
        countDS = 0
        startDS = 0
        countimp = 0
        startimp = 0
        countrepto = 0
        startrepto = 0
        countref = 0
        startref = 0
        countrpth = 0
        startrpth = 0
        countASGDID = 0
        startASGDID = 0
        startASGsubj = 0
        countASGsubj = 0
        startBarra = 0
        countBarra = 0
        startBarraConn = 0
        countBarraConn = 0
        startBarraSpamRep = 0
        countBarraSpamRep = 0
        countBarraSpamScor = 0
        startBarraSpamScor = 0
        startBarraSpamStat = 0
        countBarraSpamStat = 0
        countBarraStartTime = 0
        startBarraStartTime = 0
        startBarrURL = 0
        countBarrURL = 0
        countBarrVirSacn = 0
        startBarrVirSacn = 0
        countDisclaimed = 0
        startDisclaimed = 0
        countMIMETrack = 0
        startMIMETrack = 0
        countHasAttach = 0
        startHasAttach = 0
        countCorrelator = 0
        startCorrelator = 0
        countMSMailPriority = 0
        startMSMailPriority = 0
        countXMailer = 0
        startXMailer = 0
        countXOriginalArrivalTime = 0
        startXOriginalArrivalTime = 0
        countXPriority = 0
        startXPriority = 0
        countXWFMX = 0
        startXWFMX = 0
        countXYMailOSG = 0
        startXYMailOSG = 0
        countforensic = 0
        startforensic = 0
        countVersion = 0
        startVersion = 0
        startContentType = 0
        countContentType = 0
        countprior=0
        startprior=0
        endOfCC =0
        endOfCc = 0
        endOfBCC =0
        startOfHtml=0
        endOfHtml =0
        #codecs.EncodedFile(emailfile, input, output,  errors='ignore')
        #f = codecs.open(emailfile, mode='r', errors='ignore')
        #l1= f.encode('utf-8').decode('utf-8','ignore').encode("utf-8")
       
        
        ####  READ The Line number for Header ####
        with io.open(emailfile,'r',encoding='utf-8',errors='ignore') as fr:
        #f =f.replace("+\\","")
           
            
            
            for num1, line in enumerate(fr, 1):
               
                if re.search('^HEADER-END:', line):
                    HeaderEndLineNumber =num1
                    #print("Header Line Number :" + str(HeaderEndLineNumber))
               
                if re.search('^From:', line):
                    if  (line.find('From:')) != -1: 
                        countFrm = countFrm +1
                        if (countFrm == 1):
                           startFrom = num1
                           #print('\n From Index Before:-'+ str(startFrom))
                           #print(int(HeaderEndLineNumber) < int(startFrom))
#                           if  (int(HeaderEndLineNumber) < int(startFrom)):# == 'True':
#                                 startFrom = 0
#                                 #print('From Index After  :-'+ str(startFrom) +'\n')
#                           else: startFrom = num1
 
                if re.search('^To:', line):
                    if  (line.find('To:')) != -1: 
                        countTo = countTo +1
                        if (countTo == 1):
                           startTo = num1
                           #print('To Index Initial:-'+ str(startTo))
#                        if  (HeaderEndLineNumber < startTo):# == True:
#                               startTo = 0
#                        else: startTo = num1
                              
                if re.search('^CC:', line):
                    if  (line.find('CC:')) != -1 : 
                        countCC = countCC +1
                        if (countCC == 1):
                           startCC = num1
                           #print('CC Index:-'+ str(startCC))
#                        if ( HeaderEndLineNumber < startCC):#== True:
#                               startCC = 0
#                        else: startCC = num1
                              
                if re.search('^Cc:', line):
                    if  (line.find('Cc:')) != -1 : 
                        countCc = countCc +1
                        if (countCc == 1):
                           startCc = num1
#                           print('Cc Index Before :-'+ str(startCc)+'Header --'+ str(HeaderEndLineNumber))
#                           print( HeaderEndLineNumber < startCc)
#                        if ( HeaderEndLineNumber < startCc):#== True:
#                           startCc = 0
#                           print('Cc Index After:-'+ str(startCc)+'-----Header --'+ str(HeaderEndLineNumber))
#                        else: startCc = num1
                               
                               
                if re.search('^BCC:', line):
                    if  (line.find('BCC:')) != -1 : 
                        countBCC = countBCC +1
                        if (countBCC == 1):
                           startBCC = num1
                           #print('BCC Index:-'+ str(startBCC))
#                        if ( HeaderEndLineNumber < startBCC):#== True:
#                           startBCC = 0
#                        else: startBCC = num1
                               
                               
                if re.search('^Date:', line):
                    if (line.find('Date:')) != -1:
                        countDt = countDt +1
                        if (countDt == 1):
                            startDate = num1
#                            print('Date Index:-'+ str(startDate))
#                        if ( HeaderEndLineNumber < startDate ):#== True:
#                               startDate = 0
#                        else: startDate = num1
                              
                            
                
                if re.search('^Delivery-date:', line):
                    if (line.find('Delivery-date:')) != -1:
                        countDDt = countDDt +1
                        if (countDDt == 1):
                            startDDt = num1
#                            #print('Delivery-date Index:-'+ str(startDDt))
#                            if ( HeaderEndLineNumber < startDDt )== True:
#                               startDDt = 0
               
                if re.search('^Subject:', line):
                    if (line.find('Subject:')) != -1:
                        countSub = countSub +1
                        if (countSub == 1):
                            startSub = num1
                            #print('Subject Index:-'+ str(startSub))
#                            if ( HeaderEndLineNumber < startSub )== True:
#                               startSub = 0               
        
                
#=========
 
                if re.search('^Message-ID:', line):
                    if (line.find('Message-ID:')) != -1:
                        countMSgID = countMSgID +1
                        if (countMSgID == 1):
                            startMSgID = num1
                            #print('Message-ID Index:-'+ str(startMSgID))
#                            if ( HeaderEndLineNumber < startMSgID )== True:
#                               startMSgID = 0                        
                               
                if re.search('^Message-Id:', line):
                    if (line.find('Message-Id:')) != -1:
                        countMSgid = countMSgid +1
                        if (countMSgid == 1):
                            startMSgid = num1
                            #print('Message-Id Index:-'+ str(startMSgid))
#                            if ( HeaderEndLineNumber < startMSgid )== True:
#                               startMSgid = 0
 
 
                if re.search('^thread-index:', line):
                    if (line.find('thread-index:')) != -1:
                        counttidx = counttidx +1
                        if (counttidx == 1):
                            starttidx = num1
                            #print('thread-index Index:-'+ str(starttidx))
#                            if ( HeaderEndLineNumber < starttidx )== True:
#                               starttidx = 0
 
 
                if re.search('^Thread-Index:', line):
                    if (line.find('Thread-Index:')) != -1:
                        countTIDX = countTIDX +1
                        if (countTIDX == 1):
                            startTIDX = num1
                            #print('Thread-Index Index:-'+ str(startTIDX))
#                            if ( HeaderEndLineNumber < startTIDX )== True:
#                               startTIDX = 0
 
 
                if re.search('^Thread-Topic:', line):
                    if (line.find('Thread-Topic:')) != -1:
                        countTopic = countTopic +1
                        if (countTopic == 1):
                            startTopic = num1
                            #print('Thread-Topic Index:-'+ str(startTopic))
#                            if ( HeaderEndLineNumber < startTopic )== True:
#                               startTopic = 0
 
 
                if re.search('^Received:', line):
                    if (line.find('Received:')) != -1:
                        countrcvd = countrcvd +1
                        if (countrcvd == 1):
                            startrcvd = num1
                            #print('Received Index:-'+ str(startrcvd))
#                            if ( HeaderEndLineNumber < startrcvd )== True:
#                               startrcvd = 0
 
 
                if re.search('^DKIM-Signature:', line):
                    if (line.find('DKIM-Signature:')) != -1:
                        countDKIM = countDKIM +1
                        if (countDKIM == 1):
                            startDKIM = num1
                            #print('DKIM-Signature Index:-'+ str(startDKIM))
#                            if ( HeaderEndLineNumber < startDKIM )== True:
#                               startDKIM = 0
 
 
                if re.search('^DomainKey-Signature:', line):
                    if (line.find('DomainKey-Signature:')) != -1:
                        countDS = countDS +1
                        if (countDS == 1):
                            startDS = num1
                            #print('DomainKey-Signature Index:-'+ str(startDS))
#                            if ( HeaderEndLineNumber < startDS )== True:
#                               startDS = 0
 
 
                if re.search('^Importance:', line):
                    if (line.find('Importance:')) != -1:
                        countimp = countimp +1
                        if (countimp == 1):
                            startimp = num1
                            #print('Importance:-'+ str(startimp))
#                            if ( HeaderEndLineNumber < startimp )== True:
#                               startimp = 0
 
 
                if re.search('^In-Reply-To:', line):
                    if (line.find('In-Reply-To:')) != -1:
                        countrepto = countrepto +1
                        if (countrepto == 1):
                            startrepto = num1
                            #print('In-Reply-To Index:-'+ str(startrepto))
#                            if ( HeaderEndLineNumber < startrepto )== True:
#                               startrepto = 0
 
 
                if re.search('^Priority:', line):
                    if (line.find('Priority:')) != -1:
                        countprior = countprior +1
                        if (countprior == 1):
                            startprior = num1
                            #print('Priority Index:-'+ str(startprior))
#                            if ( HeaderEndLineNumber < startprior )== True:
#                               startprior = 0
 
                if re.search('^References:', line):
                    if (line.find('References:')) != -1:
                        countref = countref +1
                        if (countref == 1):
                            startref = num1
                            #print('References Index:-'+ str(startref))
#                            if ( HeaderEndLineNumber < startref )== True:
#                               startref = 0
 
                if re.search('^Return-Path:', line):
                    if (line.find('Return-Path:')) != -1:
                        countrpth = countrpth +1
                        if (countrpth == 1):
                            startrpth = num1
                            #print('Return-Path Index:-'+ str(startrpth))
#                            if ( HeaderEndLineNumber < startrpth )== True:
#                               startrpth = 0
 
                if re.search('^X-ASG-Debug-ID:', line):
                    if (line.find('X-ASG-Debug-ID:')) != -1:
                       countASGDID = countASGDID +1
                        if (countASGDID == 1):
                            startASGDID = num1
                            #print('X-ASG-Debug-ID Index:-'+ str(startASGDID))
#                            if ( HeaderEndLineNumber < startASGDID )== True:
#                               startASGDID = 0
 
                if re.search('^X-ASG-Orig-Subj:', line):
                    if (line.find('X-ASG-Orig-Subj:')) != -1:
                        countASGsubj = countASGsubj +1
                        if (countASGsubj == 1):
                            startASGsubj = num1
                            #print('X-ASG-Orig-Subj Index:-'+ str(startASGsubj))
#                            if ( HeaderEndLineNumber < startASGsubj )== True:
#                               startASGsubj = 0
 
                if re.search('^X-Barracuda-Bayes:', line):
                    if (line.find('X-Barracuda-Bayes:')) != -1:
                        countBarra = countBarra +1
                        if (countBarra == 1):
                            startBarra = num1
                            #print('X-Barracuda-Bayes Index:-'+ str(startBarra))
#                            if ( HeaderEndLineNumber < startBarra )== True:
#                               startBarra = 0
 
                if re.search('^X-Barracuda-Connect:', line):
                    if (line.find('X-Barracuda-Connect:')) != -1:
                        countBarraConn = countBarraConn +1
                        if (countBarraConn == 1):
                            startBarraConn = num1
                            #print('X-Barracuda-Connect Index:-'+ str(startBarraConn))
#                            if ( HeaderEndLineNumber < startBarraConn )== True:
#                               startBarraConn = 0
 
                if re.search('^X-Barracuda-Spam-Report:', line):
                    if (line.find('X-Barracuda-Spam-Report:')) != -1:
                        countBarraSpamRep = countBarraSpamRep +1
                        if (countBarraSpamRep == 1):
                            startBarraSpamRep = num1
                            #print('X-Barracuda-Spam-Report Index:-'+ str(startBarraSpamRep))
#                            if ( HeaderEndLineNumber < startBarraSpamRep )== True:
#                               startBarraSpamRep = 0
                              
                if re.search('^X-Barracuda-Spam-Score:', line):
                    if (line.find('X-Barracuda-Spam-Score:')) != -1:
                        countBarraSpamScor = countBarraSpamScor +1
                        if (countBarraSpamScor == 1):
                            startBarraSpamScor = num1
                            #print('X-Barracuda-Spam-Score Index:-'+ str(startBarraSpamScor))
#                            if ( HeaderEndLineNumber < startBarraSpamScor )== True:
#                               startBarraSpamScor = 0
 
                if re.search('^X-Barracuda-Spam-Status:', line):
                    if (line.find('X-Barracuda-Spam-Status:')) != -1:
                        countBarraSpamStat = countBarraSpamStat +1
                        if (countBarraSpamStat == 1):
                            startBarraSpamStat = num1
                            #print('X-Barracuda-Spam-Status Index:-'+ str(startBarraSpamStat))
#                            if ( HeaderEndLineNumber < startBarraSpamStat )== True:
#                               startBarraSpamStat = 0
 
                if re.search('^X-Barracuda-Start-Time:', line):
                    if (line.find('X-Barracuda-Start-Time:')) != -1:
                        countBarraStartTime = countBarraStartTime +1
                        if (countBarraStartTime == 1):
                            startBarraStartTime = num1
                            #print('X-Barracuda-Start-Time Index:-'+ str(startBarraStartTime))
#                            if ( HeaderEndLineNumber < startBarraStartTime )== True:
#                               startBarraStartTime = 0
 
                if re.search('^X-Barracuda-URL:', line):
                    if (line.find('X-Barracuda-URL:')) != -1:
                        countBarrURL = countBarrURL +1
                        if (countBarrURL == 1):
                            startBarrURL = num1
                            #print('X-Barracuda-URL Index:-'+ str(startBarrURL))
#                            if ( HeaderEndLineNumber < startBarrURL )== True:
#                               startBarrURL = 0
 
                if re.search('^X-Barracuda-Virus-Scanned:', line):
                    if (line.find('X-Barracuda-Virus-Scanned:')) != -1:
                        countBarrVirSacn = countBarrVirSacn +1
                        if (countBarrVirSacn == 1):
                            startBarrVirSacn = num1
                            #print('X-Barracuda-Virus-Scanned Index:-'+ str(startBarrVirSacn))
#                            if ( HeaderEndLineNumber < startBarrVirSacn )== True:
#                               startBarrVirSacn = 0
 
                if re.search('^X-Disclaimed:', line):
                    if (line.find('X-Disclaimed:')) != -1:
                        countDisclaimed = countDisclaimed +1
                        if (countDisclaimed == 1):
                            startDisclaimed = num1
                            #print('X-Disclaimed Index:-'+ str(startDisclaimed))
#                            if ( HeaderEndLineNumber < startDisclaimed )== True:
#                               startDisclaimed = 0
 
                if re.search('^X-MIMETrack:', line):
                    if (line.find('X-MIMETrack:')) != -1:
                        countMIMETrack = countMIMETrack +1
                        if (countMIMETrack == 1):
                            startMIMETrack = num1
                            #print('X-MIMETrack Index:-'+ str(startMIMETrack))
#                            if ( HeaderEndLineNumber < startMIMETrack )== True:
#                               startMIMETrack = 0  
                               
                if re.search('^X-MS-Has-Attach:', line):
                    if (line.find('X-MS-Has-Attach:')) != -1:
                        countHasAttach = countHasAttach +1
                        if (countHasAttach == 1):
                            startHasAttach = num1
                            #print('X-MS-Has-Attach Index:-'+ str(startHasAttach))
#                            if ( HeaderEndLineNumber < startHasAttach )== True:
#                               startHasAttach = 0 
                               
                if re.search('^X-MS-TNEF-Correlator:', line):
                    if (line.find('X-MS-TNEF-Correlator:')) != -1:
                        countCorrelator = countCorrelator +1
                        if (countCorrelator == 1):
                            startCorrelator = num1
                            #print('X-MS-TNEF-Correlator Index:-'+ str(startCorrelator))
#                            if ( HeaderEndLineNumber < startCorrelator )== True:
#                               startCorrelator = 0  
 
                if re.search('^X-MSMail-Priority:', line):
                    if (line.find('X-MSMail-Priority:')) != -1:
                        countMSMailPriority = countMSMailPriority +1
                        if (countMSMailPriority == 1):
                            startMSMailPriority = num1
                            #print('X-MSMail-Priority Index:-'+ str(startMSMailPriority))
#                            if ( HeaderEndLineNumber < startMSMailPriority )== True:
#                               startMSMailPriority = 0  
 
                if re.search('^X-Mailer:', line):
                    if (line.find('X-Mailer:')) != -1:
                        countXMailer = countXMailer +1
                        if (countXMailer == 1):
                            startXMailer = num1
                            #print('X-Mailer Index:-'+ str(startXMailer))
#                            if ( HeaderEndLineNumber < startXMailer )== True:
#                               startXMailer = 0  
 
                if re.search('^X-OriginalArrivalTime:', line):
                    if (line.find('X-OriginalArrivalTime:')) != -1:
                        countXOriginalArrivalTime = countXOriginalArrivalTime +1
                        if (countXOriginalArrivalTime == 1):
                            startXOriginalArrivalTime = num1
                            #print('X-OriginalArrivalTime Index:-'+ str(startXOriginalArrivalTime))
#                            if ( HeaderEndLineNumber < startXOriginalArrivalTime )== True:
#                               startXOriginalArrivalTime = 0  
 
                if re.search('^X-Priority:', line):
                    if (line.find('X-Priority:')) != -1:
                        countXPriority = countXPriority +1
                        if (countXPriority == 1):
                            startXPriority = num1
                            #print('MX-Priority Index:-'+ str(startXPriority))
#                            if ( HeaderEndLineNumber < startXPriority )== True:
#                               startXPriority = 0  
 
                if re.search('^X-WFMX:', line):
                    if (line.find('X-WFMX:')) != -1:
                        countXWFMX = countXWFMX +1
                        if (countXWFMX == 1):
                            startXWFMX = num1
                            #print('X-WFMX Index:-'+ str(startXWFMX))
#                            if ( HeaderEndLineNumber < startXWFMX )== True:
#                               startXWFMX = 0  
 
                if re.search('^X-YMail-OSG:', line):
                    if (line.find('X-YMail-OSG:')) != -1:
                        countXYMailOSG = countXYMailOSG +1
                        if (countXYMailOSG == 1):
                            startXYMailOSG = num1
                            #print('X-YMail-OSG Index:-'+ str(startXYMailOSG))
#                            if ( HeaderEndLineNumber < startXYMailOSG )== True:
#                               startXYMailOSG = 0  
 
                if re.search('^X-libpst-forensic-sender:', line):
                    if (line.find('X-libpst-forensic-sender:')) != -1:
                        countforensic = countforensic +1
                        if (countforensic == 1):
                            startforensic = num1
                            #print('X-libpst-forensic-sender Index:-'+ str(startforensic))
#                            if ( HeaderEndLineNumber < startMSgID )== True:
#                               startforensic = 0  
 
                if re.search('^MIME-Version:', line):
                    if (line.find('MIME-Version:')) != -1:
                        countVersion = countVersion +1
                        if (countVersion == 1):
                            startVersion = num1
                            #print('MIME-Version Index:-'+ str(startVersion))
#                            if ( HeaderEndLineNumber < startVersion )== True:
#                               startVersion = 0  
 
                if re.search('^Content-Type:', line,re.IGNORECASE):
                    if (line.find('Content-Type:')) != -1:
                        countContentType = countContentType +1
                        if (countContentType == 1):
                            startContentType = num1
                            #print('Content-Type Index:-'+ str(startContentType))
#                            if ( HeaderEndLineNumber < startContentType )== True:
#                               startContentType = 0  
                            
                if re.search('<html', line,re.IGNORECASE):    
                    startOfHtml=num1
       
                if re.search('</html>', line,re.IGNORECASE):
                    endOfHtml =num1
                   
###======================================= CHECK IF Its greater than header
#            print("Header Line Number At the Start :" + str(HeaderEndLineNumber))
                             
            if  (startTo > HeaderEndLineNumber):
                startTo=0
           
            if (startCC > HeaderEndLineNumber):
                startCC =0
               
            if (startCc > HeaderEndLineNumber):
                 startCc=0
                 
            if (startBCC > HeaderEndLineNumber):
                           startBCC=0
           
            if (startDate > HeaderEndLineNumber):
                           startDate=0
            if (startDDt > HeaderEndLineNumber):
                           startDDt=0
            if (startSub > HeaderEndLineNumber):
                           startSub=0
            if (startMSgID > HeaderEndLineNumber):
                           startMSgID=0
            if (startMSgid > HeaderEndLineNumber):
                           startMSgid=0
            if (starttidx > HeaderEndLineNumber):
                           starttidx=0
            if (startTIDX > HeaderEndLineNumber):
                           startTIDX=0
            if (startTopic > HeaderEndLineNumber):
                           startTopic=0
            if (startrcvd > HeaderEndLineNumber):
                           startrcvd=0
            if (startDKIM > HeaderEndLineNumber):
                           startDKIM=0
            if (startDS > HeaderEndLineNumber):
                           startDS=0
            if (startimp > HeaderEndLineNumber):
                           startimp=0
            if (startrepto > HeaderEndLineNumber):
                           startrepto=0
            if (startprior> HeaderEndLineNumber):
                           startprior=0
            if (startref > HeaderEndLineNumber):
                           startref=0
            if (startrpth > HeaderEndLineNumber):
                           startrpth=0
            if (startASGDID > HeaderEndLineNumber):
                           startASGDID=0
            if (startASGsubj > HeaderEndLineNumber):
                           startASGsubj=0
            if (startBarra > HeaderEndLineNumber):
                           startBarra=0
            if (startBarraConn > HeaderEndLineNumber):
                           startBarraConn=0
            if (startBarraSpamRep > HeaderEndLineNumber):
                           startBarraSpamRep=0
            if (startBarraSpamScor > HeaderEndLineNumber):
                           startBarraSpamScor=0
            if (startBarraSpamStat > HeaderEndLineNumber):
                           startBarraSpamStat=0
            if (startBarraStartTime > HeaderEndLineNumber):
                           startBarraStartTime=0
            if (startBarrURL > HeaderEndLineNumber):
                           startBarrURL=0
            if (startBarrVirSacn > HeaderEndLineNumber):
                           startBarrVirSacn=0
            if (startDisclaimed > HeaderEndLineNumber):
                           startDisclaimed=0
            if (startMIMETrack > HeaderEndLineNumber):
                           startMIMETrack=0
            if (startHasAttach > HeaderEndLineNumber):
                           startHasAttach=0
            if (startCorrelator > HeaderEndLineNumber):
                           startCorrelator=0
            if (startMSMailPriority > HeaderEndLineNumber):
                           startMSMailPriority=0
            if (startXMailer > HeaderEndLineNumber):
                           startXMailer=0
            if (startXOriginalArrivalTime > HeaderEndLineNumber):
                           startXOriginalArrivalTime=0
            if (startXPriority > HeaderEndLineNumber):
                           startXPriority=0
            if (startXWFMX > HeaderEndLineNumber):
                           startXWFMX=0
            if (startXYMailOSG > HeaderEndLineNumber):
                           startXYMailOSG=0
            if (startforensic > HeaderEndLineNumber):
                           startforensic=0
            if (startVersion > HeaderEndLineNumber):
                           startVersion=0
            if (startContentType > HeaderEndLineNumber):
                           startContentType =0
                                  
#===================               
#                if  (startTo > 0 ):
#                    if (startCC > 0):
#                        endTo = startCC
#                    elif (startCc > 0 ):
#                        endTo = startCc
#                    elif (startBCC > 0 ):
#                        endTo = startBCC
#                    elif (startDate > 0 ):
#                        endTo = startDate
#                       
            if  (startTo > 0):
                    if (startCC > 0):
                        endTo = startCC
                    elif (startCc > 0):
                        endTo = startCc
                    elif (startBCC > 0):
                        endTo = startBCC
                    elif (startDate > 0):
                       endTo = startDate
                    elif (startDDt > 0):
                        endTo = startDDt
                    elif (startSub > 0):
                        endTo = startSub
                    elif (startMSgID > 0):
                        endTo = startMSgID
                    elif (startMSgid > 0):
                        endTo = startMSgid
                    elif (starttidx > 0):
                        endTo = starttidx
                    elif (startTIDX > 0):
                        endTo = startTIDX
                    elif (startTopic > 0):
                        endTo = startTopic
                    elif (startrcvd > 0):
                        endTo = startrcvd
                    elif (startDKIM > 0):
                        endTo = startDKIM
                    elif (startDS > 0):
                        endTo = startDS
                    elif (startimp > 0):
                        endTo = startimp
                    elif (startrepto > 0):
                        endTo = startrepto
                    elif (startprior> 0):
                        endTo = startprior
                    elif (startref > 0):
                        endTo = startref
                    elif (startrpth > 0):
                        endTo = startrpth
                    elif (startASGDID > 0):
                        endTo = startASGDID
                    elif (startASGsubj > 0):
                        endTo = startASGsubj
                    elif (startBarra > 0):
                        endTo = startBarra
                    elif (startBarraConn > 0):
                        endTo = startBarraConn
                    elif (startBarraSpamRep > 0):
                        endTo = startBarraSpamRep
                    elif (startBarraSpamScor > 0):
                        endTo = startBarraSpamScor
                    elif (startBarraSpamStat > 0):
                        endTo = startBarraSpamStat
                    elif (startBarraStartTime > 0):
                        endTo = startBarraStartTime
                    elif (startBarrURL > 0):
                        endTo = startBarrURL
                    elif (startBarrVirSacn > 0):
                        endTo = startBarrVirSacn
                    elif (startDisclaimed > 0):
                        endTo = startDisclaimed
                    elif (startMIMETrack > 0):
                        endTo = startMIMETrack
                    elif (startHasAttach > 0):
                                 endTo = startHasAttach
                    elif (startCorrelator > 0):
                                       endTo = startCorrelator
                    elif (startMSMailPriority > 0):
                        endTo = startMSMailPriority
                    elif (startXMailer > 0):
                       endTo = startXMailer
                    elif (startXOriginalArrivalTime > 0):
                        endTo = startXOriginalArrivalTime
                    elif (startXPriority > 0):
                        endTo = startXPriority
                    elif (startXWFMX > 0):
                        endTo = startXWFMX
                    elif (startXYMailOSG > 0):
                       endTo = startXYMailOSG
                    elif (startforensic > 0):
                        endTo = startforensic
                    elif (startVersion > 0):
                        endTo = startVersion
                    elif (startContentType > 0):
                       endTo = startContentType
                    else:
                          endTo = HeaderEndLineNumber
             
            if (startCC > 0):
                    if (startCc > 0):
                        endOfCC = startCc
                    elif (startBCC > 0):
                        endOfCC = startBCC
                    elif (startDate > 0):
                        endOfCC = startDate
                    elif (startDDt > 0):
                        endOfCC = startDDt
                    elif (startSub > 0):
                        endOfCC = startSub
                    elif (startMSgID > 0):
                        endOfCC = startMSgID
                    elif (startMSgid > 0):
                        endOfCC = startMSgid
                    elif (starttidx > 0):
                        endOfCC = starttidx
                    elif (startTIDX > 0):
                        endOfCC = startTIDX
                    elif (startTopic > 0):
                        endOfCC = startTopic
                    elif (startrcvd > 0):
                        endOfCC = startrcvd
                    elif (startDKIM > 0):
                        endOfCC = startDKIM
                    elif (startDS > 0):
                        endOfCC = startDS
                    elif (startimp > 0):
                        endOfCC = startimp
                    elif (startrepto > 0):
                        endOfCC = startrepto
                    elif (startprior> 0):
                        endOfCC = startprior
                    elif (startref > 0):
                        endOfCC = startref
                    elif (startrpth > 0):
                        endOfCC = startrpth
                    elif (startASGDID > 0):
                        endOfCC = startASGDID
                    elif (startASGsubj > 0):
                        endOfCC = startASGsubj
                    elif (startBarra > 0):
                        endOfCC = startBarra
                    elif (startBarraConn > 0):
                        endOfCC = startBarraConn
                    elif (startBarraSpamRep > 0):
                        endOfCC = startBarraSpamRep
                    elif (startBarraSpamScor > 0):
                        endOfCC = startBarraSpamScor
                    elif (startBarraSpamStat > 0):
                        endOfCC = startBarraSpamStat
                    elif (startBarraStartTime > 0):
                        endOfCC = startBarraStartTime
                    elif (startBarrURL > 0):
                        endOfCC = startBarrURL
                    elif (startBarrVirSacn > 0):
                        endOfCC = startBarrVirSacn
                    elif (startDisclaimed > 0):
                        endOfCC = startDisclaimed
                    elif (startMIMETrack > 0):
                        endOfCC = startMIMETrack
                    elif (startHasAttach > 0):
                                 endOfCC = startHasAttach
                    elif (startCorrelator > 0):
                                       endOfCC = startCorrelator
                    elif (startMSMailPriority > 0):
                        endOfCC = startMSMailPriority
                    elif (startXMailer > 0):
                        endOfCC = startXMailer
                    elif (startXOriginalArrivalTime > 0):
                        endOfCC = startXOriginalArrivalTime
                    elif (startXPriority > 0):
                        endOfCC = startXPriority
                    elif (startXWFMX > 0):
                        endOfCC = startXWFMX
                    elif (startXYMailOSG > 0):
                       endOfCC = startXYMailOSG
                    elif (startforensic > 0):
                        endOfCC = startforensic
                    elif (startVersion > 0):
                        endOfCC = startVersion
                    elif (startContentType > 0):
                       endOfCC = startContentType
                    else:
                          endOfCC = HeaderEndLineNumber
 
 
            if (startCc > 0):
                    if (startBCC > 0):
                       endOfCc = startBCC
                    elif (startDate > 0):
                        endOfCc = startDate
                    elif (startDDt > 0):
                        endOfCc = startDDt
                    elif (startSub > 0):
                        endOfCc = startSub
                    elif (startMSgID > 0):
                        endOfCc = startMSgID
                    elif (startMSgid > 0):
                        endOfCc = startMSgid
                    elif (starttidx > 0):
                        endOfCc = starttidx
                    elif (startTIDX > 0):
                        endOfCc = startTIDX
                    elif (startTopic > 0):
                        endOfCc = startTopic
                    elif (startrcvd > 0):
                        endOfCc = startrcvd
                    elif (startDKIM > 0):
                        endOfCc = startDKIM
                    elif (startDS > 0):
                        endOfCc = startDS
                    elif (startimp > 0):
                        endOfCc = startimp
                    elif (startrepto > 0):
                        endOfCc = startrepto
                    elif (startprior> 0):
                        endOfCc = startprior
                    elif (startref > 0):
                        endOfCc = startref
                    elif (startrpth > 0):
                        endOfCc = startrpth
                    elif (startASGDID > 0):
                        endOfCc = startASGDID
                    elif (startASGsubj > 0):
                        endOfCc = startASGsubj
                    elif (startBarra > 0):
                        endOfCc = startBarra
                    elif (startBarraConn > 0):
                        endOfCc = startBarraConn
                    elif (startBarraSpamRep > 0):
                        endOfCc = startBarraSpamRep
                    elif (startBarraSpamScor > 0):
                        endOfCc = startBarraSpamScor
                    elif (startBarraSpamStat > 0):
                        endOfCc = startBarraSpamStat
                    elif (startBarraStartTime > 0):
                        endOfCc = startBarraStartTime
                    elif (startBarrURL > 0):
                        endOfCc = startBarrURL
                    elif (startBarrVirSacn > 0):
                        endOfCc = startBarrVirSacn
                    elif (startDisclaimed > 0):
                        endOfCc = startDisclaimed
                    elif (startMIMETrack > 0):
                        endOfCc = startMIMETrack
                    elif (startHasAttach > 0):
                                 endOfCc = startHasAttach
                    elif (startCorrelator > 0):
                                       endOfCc = startCorrelator
                    elif (startMSMailPriority > 0):
                        endOfCc = startMSMailPriority
                    elif (startXMailer > 0):
                        endOfCc = startXMailer
                    elif (startXOriginalArrivalTime > 0):
                        endOfCc = startXOriginalArrivalTime
                    elif (startXPriority > 0):
                        endOfCc = startXPriority
                    elif (startXWFMX > 0):
                        endOfCc = startXWFMX
                    elif (startXYMailOSG > 0):
                       endOfCc = startXYMailOSG
                    elif (startforensic > 0):
                        endOfCc = startforensic
                    elif (startVersion > 0):
                        endOfCc = startVersion
                    elif (startContentType > 0):
                       endOfCc = startContentType
                    else:
                          endOfCc = HeaderEndLineNumber
 
 
            if (startBCC > 0):
                    if (startDate > 0):
                        endOfBCC = startDate
                    elif (startDDt > 0):
                        endOfBCC = startDDt
                    elif (startSub > 0):
                        endOfBCC = startSub
                    elif (startMSgID > 0):
                        endOfBCC = startMSgID
                    elif (startMSgid > 0):
                        endOfBCC = startMSgid
                    elif (starttidx > 0):
                        endOfBCC = starttidx
                    elif (startTIDX > 0):
                        endOfBCC = startTIDX
                    elif (startTopic > 0):
                        endOfBCC = startTopic
                    elif (startrcvd > 0):
                        endOfBCC = startrcvd
                    elif (startDKIM > 0):
                        endOfBCC = startDKIM
                    elif (startDS > 0):
                        endOfBCC = startDS
                    elif (startimp > 0):
                        endOfBCC = startimp
                    elif (startrepto > 0):
                        endOfBCC = startrepto
                    elif (startprior> 0):
                        endOfBCC = startprior
                    elif (startref > 0):
                        endOfBCC = startref
                    elif (startrpth > 0):
                        endOfBCC = startrpth
                    elif (startASGDID > 0):
                        endOfBCC = startASGDID
                    elif (startASGsubj > 0):
                        endOfBCC = startASGsubj
                    elif (startBarra > 0):
                        endOfBCC = startBarra
                    elif (startBarraConn > 0):
                        endOfBCC = startBarraConn
                    elif (startBarraSpamRep > 0):
                        endOfBCC = startBarraSpamRep
                    elif (startBarraSpamScor > 0):
                        endOfBCC = startBarraSpamScor
                    elif (startBarraSpamStat > 0):
                        endOfBCC = startBarraSpamStat
                    elif (startBarraStartTime > 0):
                        endOfBCC = startBarraStartTime
                    elif (startBarrURL > 0):
                        endOfBCC = startBarrURL
                    elif (startBarrVirSacn > 0):
                        endOfBCC = startBarrVirSacn
                    elif (startDisclaimed > 0):
                        endOfBCC = startDisclaimed
                    elif (startMIMETrack > 0):
                        endOfBCC = startMIMETrack
                    elif (startHasAttach > 0):
                                 endOfBCC = startHasAttach
                    elif (startCorrelator > 0):
                                       endOfBCC = startCorrelator
                    elif (startMSMailPriority > 0):
                        endOfBCC = startMSMailPriority
                    elif (startXMailer > 0):
                        endOfBCC = startXMailer
                    elif (startXOriginalArrivalTime > 0):
                        endOfBCC = startXOriginalArrivalTime
                    elif (startXPriority > 0):
                        endOfBCC = startXPriority
                    elif (startXWFMX > 0):
                        endOfBCC = startXWFMX
                    elif (startXYMailOSG > 0):
                       endOfBCC = startXYMailOSG
                    elif (startforensic > 0):
                        endOfBCC = startforensic
                    elif (startVersion > 0):
                        endOfBCC = startVersion
                    elif (startContentType > 0):
                       endOfBCC = startContentType
                    else:
                          endOfBCC = HeaderEndLineNumber
                         
               
 
        fr.close
 
 
 
       
        myTolist = []
        myFromlist = []
        mySublist = []
        myCClist = []
        myCclist = []
        myBCClist = []
        myPT = []
       
        with io.open(emailfile,'r',encoding='utf-8',errors='ignore') as f:
        #f =f.replace("+\\","")
            for num, line in enumerate(f, 1):
            #for line in f:
                #print (line)
#                i = i+len(line)
                #print(i)
                #line = line.rstrip()
                line = line.replace('________________________________',' ')
                line = line.replace('-----',' ')
#                line = line.replace('>','')
#                line = line.replace('"','')
#                line=re.sub('<[^>]*>', '', line)
 
                if re.search('^Inbox-ID:', line):
                    line = line.rstrip()
                    lth1= len(line)
                    ib = line[0:lth1]
                    ib = ib.replace('Inbox-ID:', '')
#                    print (ib)
                                
                if re.search('^MAIL-BOX:', line):
                    line = line.rstrip()
                    lth2= len(line)
                    mb = line[0:lth2]
                    mb = mb.replace('MAIL-BOX:','')
#                    print (mb)
                    
                if re.search('^From_Name:', line):
                    line = line.rstrip()
                    frmnmlth= len(line)
                    frmnm = line[0:frmnmlth]
                    frmnm = frmnm.replace('From_Name:','')
#                    print (frmnm)
                   
                    
                if re.search('^Manual_Date:', line):
                    line = line.rstrip()
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
               
 
#                   
                frm = ''
                #if startFrom > 0:
                if (num == startFrom and startFrom > 0):
                    line = line.rstrip()
                    myFromlist.append(line.replace('From:',''))
                frm = ''.join(map(str, myFromlist))
                #print(frm)
                   
                
                if num > startTo-1 and num < (endTo):
                    line = line.rstrip()
                    myTolist.append(line.replace('To:',''))
              
                
                to = ''.join(map(str, myTolist))
 
 
                if (num == startSub and startSub > 0):
                    line = line.rstrip()
                    mySublist.append(line.replace('Subject:',''))
                sub = ''.join(map(str, mySublist))
                #print(sub)
 
                if num > startCC-1 and num < (endOfCC):
                    line = line.rstrip()
                    myCClist.append(line.replace('CC:',''))
                CC = ''.join(map(str, myCClist))
               
                if num > startCc-1 and num < (endOfCc):
                    line = line.rstrip()
                    myCclist.append(line.replace('Cc:',''))
                CC1 = ''.join(map(str, myCclist))
 
                if (num == startBCC and endOfBCC > 0):
                    line = line.rstrip()
                    myBCClist.append(line.replace('BCC:',''))
                BCC = ''.join(map(str, myBCClist))               
 
 
                ###  IF  There is No HTMl TAG , PICK EVERY THING AFTER HEADER LINE   ##############  
                if startOfHtml == 0  and endOfHtml == 0:
                    if num > HeaderEndLineNumber:
                        if re.search("^----boundary-LibPST-iamunique",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Type:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^--alt---boundary-LibPST",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Transfer-Encoding:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Disposition:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.match(r'^\s*$', line):
                            myPT.append('')
                        elif re.search("^<META HTTP-EQUIV=",line,re.IGNORECASE):
                            myPT.append('')
                        else: myPT.append(line)
 
               
###  IF  There is START HTMl TAG  AND NO END HTML TAG, PICK EVERY THING BETWEEN  HEADER LINE
#################                 AND START OF HTL TAG ##############  
                if startOfHtml > 0  and endOfHtml == 0:
                    if num > HeaderEndLineNumber and num < startOfHtml:
                        if re.search("^----boundary-LibPST-iamunique",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Type:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^--alt---boundary-LibPST",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Transfer-Encoding:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Disposition:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.match(r'^\s*$', line):
                            myPT.append('')
                        elif re.search("^<META HTTP-EQUIV=",line,re.IGNORECASE):
                            myPT.append('')
                        else: myPT.append(line)
                   
###  IF  There is START AND END OF  HTMl TAG  PICK EVERY THING BETWEEN  HEADER LINE
#################                 AND START OF HTL TAG and Any thing After
#################  END Of HTML TAG                    ##############
                if startOfHtml > 0  and endOfHtml > 0:   
                    if num > HeaderEndLineNumber and num < startOfHtml :
                        if re.search("^----boundary-LibPST-iamunique",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Type:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^--alt---boundary-LibPST",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Transfer-Encoding:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Disposition:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.match(r'^\s*$', line):
                            myPT.append('')
                        elif re.search("^<META HTTP-EQUIV=",line,re.IGNORECASE):
                            myPT.append('')
                        else: myPT.append(line)
                    elif num > endOfHtml:
                        if re.search("^----boundary-LibPST-iamunique",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Type:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^--alt---boundary-LibPST",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Transfer-Encoding:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.search("^Content-Disposition:",line,re.IGNORECASE):
                            myPT.append('')
                        elif re.match(r'^\s*$', line):
                            myPT.append('')   
                        elif re.search("^<META HTTP-EQUIV=",line,re.IGNORECASE):
                            myPT.append('')
                        else: myPT.append(line)
                PT = ''.join(map(str, myPT))
#                PT = PT.replace(',',' ')
#                PT = PT.replace('"',' ')
#                PT = PT.replace(';',' ')
#                PT = PT.replace('<',' ')
#                PT = PT.replace('>',' ')
                PT = PT.replace('\n',' ')
                  
        
                
 
 
 
  
            writer.writerow((ib,mb,frmnm,mandt,DT,DD,MM,year,MMYYYY,frm,to,CC,CC1,BCC,sub,PT) )
  
        
        
        f.close()  
            
   out_file.close()        
                 #j=j+1
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
 
