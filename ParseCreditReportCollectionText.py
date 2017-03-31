# -*- coding: utf-8 -*-
"""
parses and creates structure for credit reports purchased from credit agencies (text to CSV)
"""
 
 
from __future__ import division  
import csv
import re
import os

import io
import numpy as np
 
 
 
dirname = "<Input directory>/"
outdirname = "<Output directory>/"
csvfilename="<>.csv"
 
headerline=re.compile("^([^:]+):\s+(.*)")
 
 
class parse_credit_reports:
   
  def __init__(self, dirname, outdirname, csvfilename):
   self.dirname = dirname
   self.outdirname = outdirname
   self.csvfilename = csvfilename
   self.examFileName = os.listdir(self.dirname)
    #with open(csvfile, 'w') as out_file:
   file_count =0
  with io.open(outdirname + "/" + csvfilename,'w',encoding='ascii',errors='replace') as out_file:   
      writer = csv.writer(out_file)
#      writer.writerow(('Inbox','MailBox','From_Name','Manual_Date','date','day','month','year','MMYYYY','From','To','CC','CC1','BCC','Subject','FULL_Content'))   
      for filename in self.examFileName:
        examFileName = self.dirname + "/" + filename
       
 
        SUBNAMELineNumber_Collection = 0
        SUBNAMELineNumber=0
        ACCOUNTLineNumber = 0
        ACCOUNTLineNumber_Collection = 0
        ECOALineNumber = 0
        endLineNumber=0
        SUBNAME_COL_POS = []
        SUBNAME_COL_POS_Collection = []
        SUBNAME_COL_NAME = []
        SUBNAME_COL_NAME_Collection = []
        ACCOUNT_COL_POS = []
        ACCOUNT_COL_POS_Collection = []
        ACCOUNT_COL_NAME = []   
        ACCOUNT_COL_NAME_Collection = []
        ECOA_COL_POS = []
        ECOA_COL_NAME = []    
        report_number_end_index =0
        borrower_end_index =0
        ALL_COL_NAME = []
        ECOA_VAL = []
        ECOA_COL_1 =[]
        SUBNAME=np.array([""])
        SUBCODE=np.array([""])
        ECOA=np.array([""])
        OPENED =np.array([""])
        CLOSED =np.array([""])
        PLACED=np.array([""])
        CREDITOR=np.array([""])
        MOP=np.array([""])
        ACCOUNT=np.array([""])
        VERIFIED=np.array([""])
        BALANCE=np.array([""])
        REMARKS=np.array([""])
        MAXDELQ=np.array([""])
        PAYPAT112=np.array([""])
        MOP=np.array([""])
        VERFIED=np.array([""])
        CREDLIM=np.array([""])
        PASTDUE=np.array([""])
        AMT_MOP=np.array([""])
        PAYPAT1324=np.array([""])
        COLLATRL_LOANTYPE=np.array([""])
        CLSD_PD=np.array([""])
        MO=np.array([""])
        N30_60_90=np.array([""])
        test = []
        kk =np.array([""])
        Report_Number = ''
        Borrower_Coborrower=''
        for_line_num=0
        subname_line_num=0
        mktsub_line_num=0
        infile_line_num=0
        date_line_num=0
        time_line_num=0
        start_of_for=0
        start_of_subname=0
        start_of_mktsub=0
        start_of_inline=0
        start_of_date=0
        start_of_time=0
        start_of_subject=0
        subject_line_num=0
        snn_of_time=0
        snn_line_num=0
        birthdate_of_time=0
        birthdate_line_num=0
        aks_of_subject=0
        aka_line_num=0
        curradd_of_time=0
        curradd_line_num=0
        daterpt_of_time=0
        daterpt_line_num=0
        frmradd_of_time=0
        frmradd_line_num=0
        startCollectionsLineNumber = 0
        startTradeLineNumber = 0
        FOR_VAL=''
        SUBNAME_VAL=''
        INFILE_VAL=''
        DATE_VAL=''
        TIME_VAL=''
        SUBJECT_VAL=''
        SNN_VAL=''
        BIRTHDT_VAL=''
        AKA_VAL=''
        CURRADD_VAL=''
        DTREPORT_VAL=''
        FORMR_VAL=''
#        ECOA_VAL.append([])
#        ECOA_VAL.append([])
        ####  READ The Line number for Start and End Of Data to be read ####
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
      
            
            print ("Starting file ", filename)
           
            
            for num1, line in enumerate(fr, 1):
               
            
                
                if re.search('^ SUBNAME', line):
                    SUBNAMELineNumber =num1
                    #print("SUBNAMELineNumber :" + str(SUBNAMELineNumber))
                if re.search('^ ACCOUNT#', line):
                    ACCOUNTLineNumber =num1
#                    print("ACCOUNTLineNumber :" + str(ACCOUNTLineNumber))                   
                if re.search('^ ECOA', line):
                    ECOALineNumber =num1
#                    print ("ECOALineNumber " ,ECOALineNumber)
                if re.search('^ I N Q U I R I E S', line):
                           endLineNumber = num1
#                           print ("End of Line ",endLineNumber)
                          
                if re.search('^ C O L L E C T I O N S', line):
                           startCollectionsLineNumber = num1
                          # print("Collection Line :", startCollectionsLineNumber)
                          
                if re.search('^ T R A D E S', line):
                           startTradeLineNumber = num1
                           #print("Trade  Line :", startTradeLineNumber)
                          
                           
                if  "TRANSUNION CREDIT REPORT" in line:
#                    print (line.replace("TRANSUNION CREDIT REPORT",''))
#                    print (line.index(","))
#                    print(line.index("TRANSUNION"))
                    report_number_end_index =line.index(",")
                    borrower_end_index = line.index("TRANSUNION")
                    Report_Number = line[0:report_number_end_index]
                    Borrower_Coborrower=line[report_number_end_index+1:borrower_end_index]
                if re.search('<FOR>',line):
#                    print(line.index('<FOR>'))
                    start_of_for =line.index('<FOR>')
                    for_line_num = num1+1
                if  "<SUB NAME>" in line:
#                    print(line.index('<SUB NAME>'))
                    start_of_subname =line.index('<SUB NAME>')
                    subname_line_num = num1+1
                if  "<MKT SUB>" in line:
#                    print(line.index('<MKT SUB>'))
                    start_of_mktsub = line.index('<MKT SUB>')
                    mktsub_line_num = num1+1
                if  "<INFILE>" in line:
#                    print(line.index('<INFILE>'))
                    start_of_inline = line.index('<INFILE>')
                    infile_line_num = num1+1
                if  "<DATE>" in line:
#                    print(line.index('<DATE>'))
                    start_of_date=line.index('<DATE>')
                    date_line_num = num1+1
                if  "<TIME>" in line:
#                    print(line.index('<TIME>'))
                    start_of_time = line.index('<TIME>')
                    time_line_num = num1+1
                if  "<SUBJECT>" in line:
#                    print(line.index('<SUBJECT>'))
                    start_of_subject = line.index('<SUBJECT>')
                    subject_line_num = num1+1
                if  "<SSN>" in line:
#                    print(line.index('<SSN>'))
                    snn_of_time = line.index('<SSN>')
                    snn_line_num = num1+1   
                if  "<BIRTH DATE>" in line:
#                    print(line.index('<BIRTH DATE>'))
                    birthdate_of_time = line.index('<BIRTH DATE>')
                    birthdate_line_num = num1+1
                if  "<ALSO KNOWN AS>" in line:
#                    print(line.index('<ALSO KNOWN AS>'))
                    aks_of_subject = line.index('<ALSO KNOWN AS>')
                    aka_line_num = num1+1
                if  "<CURRENT ADDRESS> " in line:
#                    print(line.index('<CURRENT ADDRESS> '))
                    curradd_of_time = line.index('<CURRENT ADDRESS> ')
                    curradd_line_num = num1+1   
                if  "<DATE RPTD>" in line:
#                    print(line.index('<DATE RPTD>'))
                    daterpt_of_time = line.index('<DATE RPTD>')
                    daterpt_line_num = num1+1   
                if  "<FORMER ADDRESS>" in line:
#                    print(line.index('<FORMER ADDRESS>'))
                    frmradd_of_time = line.index('<FORMER ADDRESS>')
                    frmradd_line_num = num1+1    
                    
#                    print (Report_Number,'\n',Borrower_Coborrower)
#                if re.search('$ TRANSUNION CREDIT REPORT', line):
#                           print ("test",line)
#                if  line.find("TRANSUNION CREDIT REPORT") > 1 :         
#                 print(num1,line,line[line.find("TRANSUNION CREDIT REPORT")])
        fr.close
        ALL_COL_NAME.append("FILE_NAME")
        ALL_COL_NAME.append("ReportNumber")
        ALL_COL_NAME.append("BorrowerCoborrower")
        ALL_COL_NAME.append("FOR")
        ALL_COL_NAME.append("SUBNAME")
        ALL_COL_NAME.append("INFILE")
        ALL_COL_NAME.append("DATE")
        ALL_COL_NAME.append("TIME")
        ALL_COL_NAME.append("SUBJECT")
        ALL_COL_NAME.append("SNN")
        ALL_COL_NAME.append("BIRTH_DATE")
        ALL_COL_NAME.append("ALSO_KNOWN_AS")
        ALL_COL_NAME.append("CURRENT_ADDRESS")
        ALL_COL_NAME.append("Address_Date_Reported")
        ALL_COL_NAME.append("FORMER_ADDRESS")
       
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
            for num1, line in enumerate(fr, 1):
                 if (num1 == for_line_num  ):
                     FOR_VAL = line[start_of_for:start_of_subname-1]
#                     print (FOR_VAL)
                 if (num1 == subname_line_num  ):
                     SUBNAME_VAL = line[start_of_subname:start_of_mktsub-1]
#                     print (SUBNAME_VAL)
                 if (num1 == infile_line_num  ):
                     INFILE_VAL = line[start_of_inline:start_of_date-1]
#                     print (INFILE_VAL)
                 if (num1 == date_line_num  ):
                     DATE_VAL = line[start_of_date:start_of_time-1]
#                     print (DATE_VAL)
                 if (num1 == time_line_num  ):
                     TIME_VAL = line[start_of_time:]
                     TIME_VAL = TIME_VAL.strip()
#                     print (TIME_VAL)
                 if (num1 == subject_line_num  ):
                     SUBJECT_VAL = line[start_of_subject:snn_of_time-1]
#                     print (SUBJECT_VAL)
                 if (num1 == snn_line_num  ):
                     SNN_VAL = line[snn_of_time:birthdate_of_time-1]
#                     print (SNN_VAL)
                 if (num1 == birthdate_line_num  ):
                     BIRTHDT_VAL = line[birthdate_of_time:]
                     BIRTHDT_VAL =BIRTHDT_VAL.strip()
#                     print (BIRTHDT_VAL)
                 if (num1 == aka_line_num  ):
                     AKA_VAL = line[aks_of_subject:]
                     AKA_VAL =AKA_VAL.strip()
#                     print (AKA_VAL)
                 if (num1 == curradd_line_num  ):
                     CURRADD_VAL = line[curradd_of_time:daterpt_of_time-1]
#                     print (CURRADD_VAL)
                 if (num1 == daterpt_line_num  ):
                     DTREPORT_VAL = line[daterpt_of_time:]
                     DTREPORT_VAL =DTREPORT_VAL.strip()
#                     print (DTREPORT_VAL)
                 if (num1 == frmradd_line_num  ):
                     FORMR_VAL = line[frmradd_of_time:daterpt_of_time-1]
#                     print (FORMR_VAL)
        fr.close
       
        
 
        """
        FIND THE POSITION OF COLLECTION ITEMS
        """
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
            for num1, line in enumerate(fr, 1):
 
                """
                Extracting the  C O L L E C T I O N S  Values From Text File and copying to CSV
                """
#                print ("HELLO ", num1, startCollectionsLineNumber ,startTradeLineNumber )
               
                if (num1 > startCollectionsLineNumber and num1 < (startTradeLineNumber-1)  ):
                    if re.search('^ SUBNAME', line):
                        SUBNAMELineNumber_Collection =num1
#                        print(num1,"SUBNAMELineNumber_Collection :" + str(SUBNAMELineNumber_Collection))                    
#                        print(line)
                    if re.search('^ ACCOUNT#', line):
                      ACCOUNTLineNumber_Collection =num1
#                      print(num1, "ACCOUNTLineNumber_Collection",ACCOUNTLineNumber_Collection)
#                      print(line)
        fr.close
 
        """
        SPLIT  COLLECTION HEADER ITEMS AND STORE EACH POSITION
        """
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
            for num1, line in enumerate(fr, 1):
 
              
                if (num1 == SUBNAMELineNumber_Collection ):
                    SUBNAME_Collection_split = line.split()
                   
                    for i in range(len(SUBNAME_Collection_split)):
                         #print("i=",i,SUBNAME_Collection_split[i],line.index(SUBNAME_Collection_split[i]))
                         SUBNAME_COL_POS_Collection.append(line.index(SUBNAME_Collection_split[i]))
                         SUBNAME_COL_NAME_Collection.append(SUBNAME_Collection_split[i])
                         ALL_COL_NAME.append(SUBNAME_Collection_split[i])
#                        
                             
                if (ACCOUNTLineNumber_Collection == num1):
                   ACCOUNT_Colllection_split= line.split()
                   for i in range(len(ACCOUNT_Colllection_split)):
#                         print("i=",i)
#                         print(ACCOUNT_Colllection_split[i])
                       #print("i=",i,ACCOUNT_Colllection_split[i],line.index(ACCOUNT_Colllection_split[i]))
                       ACCOUNT_COL_POS_Collection.append(line.index(ACCOUNT_Colllection_split[i]))
                       ACCOUNT_COL_NAME_Collection.append(ACCOUNT_Colllection_split[i])
                       ALL_COL_NAME.append(ACCOUNT_Colllection_split[i])
                  
        fr.close
#        print(SUBNAME_COL_POS_Collection,SUBNAME_COL_NAME_Collection)
#        print(ACCOUNT_COL_POS_Collection,ACCOUNT_COL_NAME_Collection)
#        print(ALL_COL_NAME)
       
        if file_count ==0 :
            writer.writerow((ALL_COL_NAME))
            file_count = file_count+1
        else:
            print("Dont print Header")
           
            
        """
        FIND THE POSITION OF VALUE OF COLLECTION ITEMS
        """
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
            for num1, line in enumerate(fr, 1):
 
                k =0
                if (num1 >= startCollectionsLineNumber and num1 < (startTradeLineNumber-1)  ):
                   #print (num1,startCollectionsLineNumber+3,startTradeLineNumber-2,((startCollectionsLineNumber+2) - (startTradeLineNumber-2)))
                   k= ((startTradeLineNumber) - (startCollectionsLineNumber+2))
                   #print(k)
                   subname_start = 3
                   while subname_start < k:
                        SUBNAME_num_collection = startCollectionsLineNumber +subname_start
                        #print (num1,SUBNAME_num_collection)
                        if (num1 == SUBNAME_num_collection):
                          #print("\nSUBNAME",len(SUBNAME_COL_POS_Collection),num1,line)
                          for wordpos in range(0,len(SUBNAME_COL_POS_Collection)):
                              if SUBNAME_COL_NAME_Collection[wordpos] == 'SUBNAME':
#                                print ('SUBNAME :' ,line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])
                                SUBNAME = np.vstack([SUBNAME,(line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])])
                              if SUBNAME_COL_NAME_Collection[wordpos] == 'SUBCODE':
#                                print ('SUBCODE :' ,line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])
                                SUBCODE = np.vstack([SUBCODE,(line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])])
                              if SUBNAME_COL_NAME_Collection[wordpos] == 'ECOA':
#                                print ('ECOA :',line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])
                                ECOA= np.vstack([ECOA,(line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])])
                              if SUBNAME_COL_NAME_Collection[wordpos] == 'OPENED':
#                                print ('OPENED :',line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])
                                OPENED= np.vstack([OPENED,(line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])])
                              if SUBNAME_COL_NAME_Collection[wordpos] == 'CLOSED':
#                                print ('CLOSED:',line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])
                                CLOSED= np.vstack([CLOSED,(line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])])
                             
                              if SUBNAME_COL_NAME_Collection[wordpos] == '$PLACED':
#                                print ('$PLACED :' ,line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])
                                PLACED= np.vstack([PLACED,(line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])])
                              if SUBNAME_COL_NAME_Collection[wordpos] == 'CREDITOR':
#                                print ('CREDITOR :' ,line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])
                                CREDITOR= np.vstack([CREDITOR,(line[SUBNAME_COL_POS_Collection[wordpos]:SUBNAME_COL_POS_Collection[wordpos+1]])])
                              if SUBNAME_COL_NAME_Collection[wordpos] == 'MOP':
                                line = line.replace(" ","_")
                                line = line.replace("\n","")
                                line = line.replace("\r","")
#                                print ('MOP :',line[SUBNAME_COL_POS_Collection[wordpos]:])
                                MOP= np.vstack([MOP,(line[SUBNAME_COL_POS_Collection[wordpos]:])])
#                                print("\n")
 
##                             
                        if subname_start == k:
                            break
                        subname_start = subname_start +3     
 
 
                   Account_start = 4
                   while Account_start < k+1:
                        Account_num_collection = startCollectionsLineNumber +Account_start
                        #print (num1,Account_num_collection)
                        if (num1 == Account_num_collection):
                          for wordpos in range(0,len(ACCOUNT_COL_POS_Collection)):
                              if ACCOUNT_COL_NAME_Collection[wordpos] == 'ACCOUNT#':
#                                print ('ACCOUNT :' ,line[ACCOUNT_COL_POS_Collection[wordpos]:ACCOUNT_COL_POS_Collection[wordpos+1]])
                                ACCOUNT = np.vstack([ACCOUNT,(line[ACCOUNT_COL_POS_Collection[wordpos]:ACCOUNT_COL_POS_Collection[wordpos+1]])])
                              if ACCOUNT_COL_NAME_Collection[wordpos] == 'VERIFIED':
#                                print (num1,'VERIFIED :' ,line[ACCOUNT_COL_POS_Collection[wordpos]:ACCOUNT_COL_POS_Collection[wordpos+1]])
                                VERIFIED = np.vstack([VERIFIED,(line[ACCOUNT_COL_POS_Collection[wordpos]:ACCOUNT_COL_POS_Collection[wordpos+1]])])
                              if ACCOUNT_COL_NAME_Collection[wordpos] == 'BALANCE':
#                                print ('BALANCE :' ,line[ACCOUNT_COL_POS_Collection[wordpos]:ACCOUNT_COL_POS_Collection[wordpos+1]])
                                BALANCE = np.vstack([BALANCE,(line[ACCOUNT_COL_POS_Collection[wordpos]:ACCOUNT_COL_POS_Collection[wordpos+1]])])
                              if ACCOUNT_COL_NAME_Collection[wordpos] == 'REMARKS':
                                line = line.replace(" ","_")
                                line = line.replace("\n","")
                                line = line.replace("\r","") 
#                                print ('REMARKS :' ,line[ACCOUNT_COL_POS_Collection[wordpos]:])
                                REMARKS = np.vstack([REMARKS,(line[ACCOUNT_COL_POS_Collection[wordpos]:])])
#                                print("\n")
                           
                            
                            
                            
                            
                        if Account_start == k:
                            break
                        Account_start = Account_start +3                            
                            
                            
        fr.close
 
        for i in range(1,len(SUBNAME)):
          writer.writerow((filename,Report_Number,Borrower_Coborrower,FOR_VAL,SUBNAME_VAL,INFILE_VAL,DATE_VAL,TIME_VAL,SUBJECT_VAL,SNN_VAL,BIRTHDT_VAL,AKA_VAL,CURRADD_VAL,DTREPORT_VAL,FORMR_VAL,''.join(map(str,SUBNAME[i])),''.join(map(str,SUBCODE[i])),''.join(map(str, ECOA[i])) ,''.join(map(str,OPENED [i])),''.join(map(str,CLOSED[i])),''.join(map(str,PLACED[i])),''.join(map(str,CREDITOR[i])),''.join(map(str,MOP[i]))  ,''.join(map(str, ACCOUNT[i]))  ,''.join(map(str, VERIFIED[i])) ,''.join(map(str, BALANCE[i])),''.join(map(str,REMARKS[i]))))

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
  ah = parse_credit_reports(dirname, outdirname, csvfilename)       
