# -*- coding: utf-8 -*-
"""
Transform specifuc section of text based credit treports to CSV
"""

"""
Parse only the collection section of credit reports.


"""
 
 
from __future__ import division  # Python 2 users only
import csv
import re

import os
import numpy as np
 
 
 
dirname = "C:/BigData/PII_Finder/DCP/Aug_20_2016/CreditReports/CreditReports/"
outdirname = "C:/BigData/PII_Finder/DCP/"
csvfilename="CreditReport_78350_Files_Only_Trade.csv"
 
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
       
 
        SUBNAMELineNumber = 0
        ACCOUNTLineNumber = 0
        ECOALineNumber = 0
        endLineNumber=0
        SUBNAME_COL_POS = []
        SUBNAME_COL_NAME = []
        ACCOUNT_COL_POS = []
        ACCOUNT_COL_NAME = []       
        ECOA_COL_POS = []
        ECOA_COL_NAME = []    
        report_number_end_index =0
        borrower_end_index =0
        ALL_COL_NAME = []
        ECOA_VAL = []
        ECOA_COL_1 =[]
        SUBNAME=np.array([""])
        SUBCODE=np.array([""])
        OPENED =np.array([""])
        HIGHCRED=np.array([""])
        TERMS=np.array([""])
        MAXDELQ=np.array([""])
        PAYPAT112=np.array([""])
        MOP=np.array([""])
        ACCOUNT=np.array([""])
        VERFIED=np.array([""])
        CREDLIM=np.array([""])
        PASTDUE=np.array([""])
        AMT_MOP=np.array([""])
        PAYPAT1324=np.array([""])
        ECOA=np.array([""])
        COLLATRL_LOANTYPE=np.array([""])
        CLSD_PD=np.array([""])
        BALANCE=np.array([""])
        REMARKS=np.array([""])
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
#                    print("SUBNAMELineNumber :" + str(SUBNAMELineNumber))
                if re.search('^ ACCOUNT#', line):
                    ACCOUNTLineNumber =num1
#                    print("ACCOUNTLineNumber :" + str(ACCOUNTLineNumber))                   
                if re.search('^ ECOA', line):
                    ECOALineNumber =num1
#                    print ("ECOALineNumber " ,ECOALineNumber)
                if re.search('^ I N Q U I R I E S', line):
                           endLineNumber = num1
#                           print ("End of Line ",endLineNumber)
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
            j =''
            for num1, line in enumerate(fr, 1):
                if (num1 == SUBNAMELineNumber):
#                     print ("Header SUBNAME \n",num1,len(line.strip()), line.split())
                     SUBNAME_split = line.split()
#                     print(SUBNAME_split[0], "Number Of words in header =", len(SUBNAME_split))
                     for i in range(len(SUBNAME_split)):
                         #print("i=",i)
                         if "PAYPAT" == SUBNAME_split[i]:
#                             print (line.index(SUBNAME_split[i]),SUBNAME_split[i]+' '+SUBNAME_split[i+1] )
                             SUBNAME_COL_POS.append(line.index(SUBNAME_split[i]))
                             SUBNAME_COL_NAME.append(SUBNAME_split[i])
                             ALL_COL_NAME.append(SUBNAME_split[i])
                             j = i +1
                             #print(i,j)
                         elif (i != j):
#                             print (i,line.index(SUBNAME_split[0]),SUBNAME_split[0])
#                             print (line.index(SUBNAME_split[i]),SUBNAME_split[i])
                             SUBNAME_COL_POS.append(line.index(SUBNAME_split[i]))
                             SUBNAME_COL_NAME.append(SUBNAME_split[i])
                             ALL_COL_NAME.append(SUBNAME_split[i])
                         #print ("Test ==",line[14:24])
                         
                elif (num1 == ACCOUNTLineNumber ):
#                     print ("Header Account \n",num1,len(line.strip()), line.split())
                     ACCOUNT_split = line.split()
#                     print(ACCOUNT_split[0], "Number Of words in header =", len(ACCOUNT_split))
                     for i in range(len(ACCOUNT_split)):
                         if "PAYPAT" == ACCOUNT_split[i]:
#                             print (line.index(ACCOUNT_split[i]),ACCOUNT_split[i]+' '+ACCOUNT_split[i+1] )
                             ACCOUNT_COL_POS.append(line.index(ACCOUNT_split[i]))
                             ACCOUNT_COL_NAME.append(ACCOUNT_split[i])
                             ALL_COL_NAME.append(ACCOUNT_split[i])
                             j = i +1
                             #print(i,j)
                         elif (i != j):
#                             print (line.index(ACCOUNT_split[i]),ACCOUNT_split[i])
                             ACCOUNT_COL_POS.append(line.index(ACCOUNT_split[i]))
                             ACCOUNT_COL_NAME.append(ACCOUNT_split[i])
                             ALL_COL_NAME.append(ACCOUNT_split[i])
                            
                elif (num1 == ECOALineNumber ):
#                     print ("Header EOA \n",num1,len(line.strip()), line.split())
                     ECOA_split = line.split()
                     for i in range(len(ECOA_split)):
#                         print (line.index(ECOA_split[i]),ECOA_split[i])
                         ECOA_COL_POS.append(line.index(ECOA_split[i]))
                         ECOA_COL_NAME.append(ECOA_split[i])
                         ALL_COL_NAME.append(ECOA_split[i])
               
#                     print (ECOA_COL_NAME[0:1],ECOA_COL_NAME[1:2])       
        fr.close
#        header_length = len(ALL_COL_NAME)
#        print(ALL_COL_NAME,ALL_COL_NAME[header_length-1])
       
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
            for num1, line in enumerate(fr, 1):
                 if (num1 == for_line_num  ):
                     FOR_VAL = line[start_of_for:start_of_subname-1]
                     print (FOR_VAL)
                 if (num1 == subname_line_num  ):
                     SUBNAME_VAL = line[start_of_subname:start_of_mktsub-1]
                     print (SUBNAME_VAL)
                 if (num1 == infile_line_num  ):
                     INFILE_VAL = line[start_of_inline:start_of_date-1]
                     print (INFILE_VAL)
                 if (num1 == date_line_num  ):
                     DATE_VAL = line[start_of_date:start_of_time-1]
                     print (DATE_VAL)
                 if (num1 == time_line_num  ):
                     TIME_VAL = line[start_of_time:]
                     TIME_VAL = TIME_VAL.strip()
                     print (TIME_VAL)
                 if (num1 == subject_line_num  ):
                     SUBJECT_VAL = line[start_of_subject:snn_of_time-1]
                     print (SUBJECT_VAL)
                 if (num1 == snn_line_num  ):
                     SNN_VAL = line[snn_of_time:birthdate_of_time-1]
                     print (SNN_VAL)
                 if (num1 == birthdate_line_num  ):
                     BIRTHDT_VAL = line[birthdate_of_time:]
                     BIRTHDT_VAL =BIRTHDT_VAL.strip()
                     print (BIRTHDT_VAL)
                 if (num1 == aka_line_num  ):
                     AKA_VAL = line[aks_of_subject:]
                     AKA_VAL =AKA_VAL.strip()
                     print (AKA_VAL)
                 if (num1 == curradd_line_num  ):
                     CURRADD_VAL = line[curradd_of_time:daterpt_of_time-1]
                     print (CURRADD_VAL)
                 if (num1 == daterpt_line_num  ):
                     DTREPORT_VAL = line[daterpt_of_time:]
                     DTREPORT_VAL =DTREPORT_VAL.strip()
                     print (DTREPORT_VAL)
                 if (num1 == frmradd_line_num  ):
                     FORMR_VAL = line[frmradd_of_time:daterpt_of_time-1]
                     print (FORMR_VAL)
        fr.close
       
        
        if file_count ==0 :
            writer.writerow((ALL_COL_NAME))
            file_count = file_count+1
        else:
            print("Dont print Header")
       
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
            for num1, line in enumerate(fr, 1):
 
                """
                Extracting the Values From Text File and copying to CSV
                """
                k =0
                if (num1 > ECOALineNumber and num1 < (endLineNumber-1)  ):
                     k = ((endLineNumber - ECOALineNumber)-2)
                     
 
                    
                     n = 1
                     while n < k:
                        SUBNAME_num = ECOALineNumber +n
                        #print (num2)
                        if (num1 == SUBNAME_num):
#                          print("\nSUBNAME",num1,line)
                         if(len(SUBNAME_COL_POS) > 0 ):
                          for wordpos in range(0,len(SUBNAME_COL_POS)-1):
                              if SUBNAME_COL_NAME[wordpos] == 'SUBNAME':
                                  SUBNAME = np.vstack([SUBNAME,(line[SUBNAME_COL_POS[wordpos]-1:SUBNAME_COL_POS[wordpos+1]-1])])
                              if SUBNAME_COL_NAME[wordpos] == 'SUBCODE':
                                  SUBCODE = np.vstack([SUBCODE,(line[SUBNAME_COL_POS[wordpos]-1:SUBNAME_COL_POS[wordpos+1]-1])])
                              if SUBNAME_COL_NAME[wordpos] == 'OPENED':
                                  OPENED = np.vstack([OPENED,(line[SUBNAME_COL_POS[wordpos]-1:SUBNAME_COL_POS[wordpos+1]-1])])
                              if SUBNAME_COL_NAME[wordpos] == 'HIGHCRED':
                                  HIGHCRED = np.vstack([HIGHCRED,(line[SUBNAME_COL_POS[wordpos]-1:SUBNAME_COL_POS[wordpos+1]-1])])
                              if SUBNAME_COL_NAME[wordpos] == 'TERMS':
                                  TERMS = np.vstack([TERMS,(line[SUBNAME_COL_POS[wordpos]-1:SUBNAME_COL_POS[wordpos+1]-1])])
                              if SUBNAME_COL_NAME[wordpos] == 'MAXDELQ':
                                  MAXDELQ = np.vstack([MAXDELQ,(line[SUBNAME_COL_POS[wordpos]-1:SUBNAME_COL_POS[wordpos+1]-1])])
                              if SUBNAME_COL_NAME[wordpos] == 'PAYPAT':
                                  PAYPAT112 = np.vstack([PAYPAT112,(line[SUBNAME_COL_POS[wordpos]-1:SUBNAME_COL_POS[wordpos+1]-1])])
                             
                          if SUBNAME_COL_NAME[len(SUBNAME_COL_POS)-1] == "MOP":          
                             line = line.replace(" ","_")
                             line = line.replace("\n","")
                             line = line.replace("\r","")
                             MOP=np.vstack([MOP,(line[SUBNAME_COL_POS[len(SUBNAME_COL_POS)-1]:len(line)])])      
                        if n == k:
                            break
                        n = n +4
                    
                     
                     acct = 2
                     while acct < k:
                        ACCOUNT_num = ECOALineNumber + acct
                        #print (num2)
                        if (num1 == ACCOUNT_num):
#                          print("ACCOUNT",num1,line.split())
                         if(len(ACCOUNT_COL_POS) >0 ):
                          for wordpos in range(0,len(ACCOUNT_COL_POS)-1):
                              if ACCOUNT_COL_NAME[wordpos] == 'ACCOUNT#':
                                  ACCOUNT = np.vstack([ACCOUNT,(line[ACCOUNT_COL_POS[wordpos]-1:ACCOUNT_COL_POS[wordpos+1]-1])])
                              if ACCOUNT_COL_NAME[wordpos] == 'VERFIED':
                                  VERFIED = np.vstack([VERFIED,(line[ACCOUNT_COL_POS[wordpos]-1:ACCOUNT_COL_POS[wordpos+1]-1])])
                              if ACCOUNT_COL_NAME[wordpos] == 'CREDLIM':
                                  CREDLIM = np.vstack([CREDLIM,(line[ACCOUNT_COL_POS[wordpos]-1:ACCOUNT_COL_POS[wordpos+1]-1])])
                              if ACCOUNT_COL_NAME[wordpos] == 'PASTDUE':
                                  PASTDUE = np.vstack([PASTDUE,(line[ACCOUNT_COL_POS[wordpos]-1:ACCOUNT_COL_POS[wordpos+1]-1])])
                              if ACCOUNT_COL_NAME[wordpos] == 'AMT-MOP':
                                  AMT_MOP = np.vstack([AMT_MOP,(line[ACCOUNT_COL_POS[wordpos]-1:ACCOUNT_COL_POS[wordpos+1]-1])])
                              #if ACCOUNT_COL_NAME[wordpos] == 'PAYPAT 13-24':
                               #   PAYPAT = np.vstack([PAYPAT,(line[ACCOUNT_COL_POS[wordpos]-1:ACCOUNT_COL_POS[wordpos+1]-1])])
                          if ACCOUNT_COL_NAME[len(ACCOUNT_COL_POS)-1] == "PAYPAT":          
                             line = line.replace(" ","_")
                             line = line.replace("\n","")
                             line = line.replace("\r","")
                             PAYPAT1324=np.vstack([PAYPAT1324,(line[ACCOUNT_COL_POS[len(ACCOUNT_COL_POS)-1]:len(line)])])      
                        if acct == k:
                            break
                        acct = acct +4
                       
                     ecoa = 3
                     while ecoa < k+1:
                        ECOA_num = ECOALineNumber + ecoa
                        if (num1 == ECOA_num):
                         if (len(ECOA_COL_POS) > 0):
                          for wordpos in range(0,len(ECOA_COL_POS)-1):
                              if ECOA_COL_NAME[wordpos] == 'ECOA':
                                  ECOA = np.vstack([ECOA,(line[ECOA_COL_POS[wordpos]-1:ECOA_COL_POS[wordpos+1]-1])])
                              if ECOA_COL_NAME[wordpos] == 'COLLATRL/LOANTYPE':
                                  COLLATRL_LOANTYPE = np.vstack([COLLATRL_LOANTYPE,(line[ECOA_COL_POS[wordpos]-1:ECOA_COL_POS[wordpos+1]-1])])
                              if ECOA_COL_NAME[wordpos] == 'CLSD/PD':
                                  CLSD_PD = np.vstack([CLSD_PD,(line[ECOA_COL_POS[wordpos]-1:ECOA_COL_POS[wordpos+1]-1])])
                              if ECOA_COL_NAME[wordpos] == 'BALANCE':
                                  BALANCE = np.vstack([BALANCE,(line[ECOA_COL_POS[wordpos]-1:ECOA_COL_POS[wordpos+1]-1])])
                              if ECOA_COL_NAME[wordpos] == 'REMARKS':
                                  REMARKS = np.vstack([REMARKS,(line[ECOA_COL_POS[wordpos]-1:ECOA_COL_POS[wordpos+1]-1])])
                              if ECOA_COL_NAME[wordpos] == 'MO':
                                  MO = np.vstack([MO,(line[ECOA_COL_POS[wordpos]-1:ECOA_COL_POS[wordpos+1]-1])])
#                            
                              
#                          print ("Last Column Not Captured in Automated Test ==",ECOA_COL_NAME[len(ECOA_COL_POS)-1],'=',line[ECOA_COL_POS[len(ECOA_COL_POS)-1]:len(line)])
                         
                          if ECOA_COL_NAME[len(ECOA_COL_POS)-1] == "30/60/90":
#                            
                             line = line.replace('/','_')
                             line = line.replace(' ','_')
                             line = line.replace( "\n",'')
                             line = line.replace("\r",'')
                             N30_60_90=np.vstack([N30_60_90,(line[ECOA_COL_POS[len(ECOA_COL_POS)-1]:len(line)])])
                             
 
                        if ecoa == k:
                            break
                        ecoa = ecoa +4 
 
        fr.close
#        print ("kk =", MO[0])
#        print(len(MO))
#        print(len(N30_60_90))
#        print(len(PAYPAT112),PAYPAT112)
        for i in range(1,len(MO)):
            #print(1)
#         writer.writerow((ECOA[i],COLLATRL_LOANTYPE[i],CLSD_PD[i],BALANCE[i],REMARKS[i],MO[i],N30_60_90[i]))
         writer.writerow((filename,Report_Number,Borrower_Coborrower,FOR_VAL,SUBNAME_VAL,INFILE_VAL,DATE_VAL,TIME_VAL,SUBJECT_VAL,SNN_VAL,BIRTHDT_VAL,AKA_VAL,CURRADD_VAL,DTREPORT_VAL,FORMR_VAL,''.join(map(str,SUBNAME[i])),''.join(map(str,SUBCODE[i])),''.join(map(str,OPENED [i])),''.join(map(str,HIGHCRED[i])),''.join(map(str,TERMS[i])),''.join(map(str,MAXDELQ[i])),''.join(map(str,PAYPAT112[i])),''.join(map(str,MOP[i])),''.join(map(str, ACCOUNT[i])),''.join(map(str, VERFIED[i])),''.join(map(str, CREDLIM[i])),''.join(map(str, PASTDUE[i])),''.join(map(str, AMT_MOP[i])),''.join(map(str, PAYPAT1324[i])),''.join(map(str, ECOA[i])),''.join(map(str,COLLATRL_LOANTYPE[i])),''.join(map(str,CLSD_PD[i])),''.join(map(str,BALANCE[i])),''.join(map(str,REMARKS[i])),''.join(map(str,MO[i])),''.join(map(str,N30_60_90[i]))))
        # writer.writerow((''.join(map(str,SUBNAME[i])),''.join(map(str,SUBCODE[i])),''.join(map(str,OPENED [i])),''.join(map(str,HIGHCRED[i])),''.join(map(str,TERMS[i])),''.join(map(str,MAXDELQ[i])),''.join(map(str,PAYPAT112[i])),''.join(map(str,MOP[i]))))
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
