# -*- coding: utf-8 -*-
"""
For transforming PDF based credit reports to CSV
"""
"""
 This extracts credit history from the PDF reports provided by credit bureau 
"""
 
from __future__ import division 
import csv
import re
import os
import io
import numpy as np
 
 
dirname = "<input file directory>/"
outdirname = "<Output file directory>/"
csvfilename="<out put report file>.csv"
 
headerline=re.compile("^([^:]+):\s+(.*)")
 
 
class parse_emails:
   
  def __init__(self, dirname, outdirname, csvfilename):
   self.dirname = dirname
   self.outdirname = outdirname
   self.csvfilename = csvfilename
   self.examFileName = os.listdir(self.dirname)
    #with open(csvfile, 'w') as out_file:
   file_count =0
   with io.open(outdirname + "/" + csvfilename,'w',encoding='ascii',errors='replace') as out_file:   
      writer = csv.writer(out_file)
      writer.writerow(("File_Name","Req_Inst_Name","Loan_Inst_Name","Loan_Acct_Num","Clinet_Tracking","Client_Code","Requested_By",
           "Date Requested","Report_ID","Time_Requested","Applicant_Name",
         "First_Name","Date_Of_Birth","SSN","Present_Residence","Previous_Residence","Employment","AKA","Credit_Score",
         "Opened","Reported","High_Balance","Reviewed","Thirty","Sixty","Ninty","Last_Active","BU1"
         ,"High_Limit","Install_Or_Revolv","Pastdue","Payment","Balance",
         "Total_High_Credit","Total_High_Balance","Total_Past_Due","Total_Payment","Total_Balance"))   
      for filename in self.examFileName:
        examFileName = self.dirname + "/" + filename
        StartOfNameBlock =0
        EndOfNameBlock=0
        Client_Tracking_line=0
        Requested_by_line=0
        Client_Code_line=0
        Date_requested_line=0
        Time_requested_line=0
        Report_ID_line=0  
        last_line =0
        Applicants_last_name_line =0
        Residence_Information_line=0  
#        File_Variations_line =0 
        Database_Residence_Information_line=0
        Database_Employment_Information_line=0
        TruAlert_Applicant_line=0
        AKA_Records_line=0
        Credit_Score_Information_line=0
        Credit_History_line=0
        Totals_line =0
        InstName = []
        Client_Tracking_val=[]
        Requested_by_val=[]
        Client_Code_val=[]
        Date_requested_val=[]
        Time_requested_val=[]
        Report_ID_val=[]
        Applicants_last_name_val=[]
        First_Name_val=[]
        DOB_val=[]
        SSN_val=[]
        Present_Residence_val=[]
        Previous_residence_val=[]
        Employment_Info_val =[]
        AKA_val =[]
        credit_score_val =[]
        Opened_line =[]
        Opened_line_Index = []
        Reported_Index = []
        Reported_Index= []
        High_balance_Index= []
        Reviewed_Index= []
        Thirty_Index= []
        Sixty_Index= []
        Ninty_Index= []
        Pastdue_Index= []
        Payment_Index= []
        Balance_Index= []
        InstNameCSV = ''
        Client_Tracking_val_CSV =''
        Requested_by_val_CSV=''
        Client_Code_val_CSV=''
        Date_requested_val_CSV =''
        Time_requested_val_CSV =''
        Report_ID_val_CSV =''
        Applicants_last_name_val_CSV = ''
        First_Name_val_CSV=''
        DOB_val_CSV=''
        SSN_val_CSV = ''
        Present_Residence_val_CSV=''
        Previous_residence_val_CSV=''
        Employment_Info_val_CSV=''
        AKA_val_CSV =''
        credit_score_val_CSV=''
        i=0
        Inst_CSV = np.array([""])
        Opened_CSV = np.array([""])
        Reported_CSV = np.array([""])
        High_Balance_CSV = np.array([""])
        Reviewed_CSV = np.array([""])
        Thirty_CSV = np.array([""])
        Sixty_CSV = np.array([""])
        Ninty_CSV = np.array([""])
        Last_active_Index=[]
        BU1_index=[]
        High_limit_index=[]
        Install_index=[]
        test = ''
        Acct_Num_CSV = np.array([""])
        BU1_CSV=np.array([""])
        High_Limit_CSV=np.array([""])
        Install_Or_Revolv_CSV=np.array([""])
        Last_Active_CSV = np.array([""])
        Total_High_Credit =[]
        Total_High_Balance =[]
        Total_Past_Due =[]
        Total_Payment =[]
        Total_Balance=[]
        Total_High_Credit_Index =[]
        Total_High_Balance_Index =[]
        Total_Past_Due_Index =[]
        Total_Payment_Index =[]
        Total_Balance_Index=[]
        Pastdue_CSV= np.array([""])
        Payment_CSV= np.array([""])
        Balance_CSV= np.array([""])
 
        """  READ The Line number for Start and End Of Data to be read """
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
            print ("Starting file ", filename)
            for num1, line in enumerate(fr, 1):
#                if re.search('^ SUBNAME', line):
#                    SUBNAMELineNumber =num1
#                    print("SUBNAMELineNumber :" + str(SUBNAMELineNumber))
                """ Verify other sample of Credit report , may be you will have to change the
                start of line search word as of now its restrictive to 2 sample reports that we have
                """
                if  "KROLL FACTUAL DATA, 5200 HAHNS PEAK DRIVE LOVELAND, CO 80538 800-766-5600 FAX 800-456-7669" in line:
                     StartOfNameBlock = num1
#                     print ("Start of Name Block :",StartOfNameBlock)
                    
                if "Creditor Information" in line:
                   last_line = num1
        fr.close
       
        """ Read Fields and columns for data set """
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
            for num1, line in enumerate(fr, 1):
                if num1 >= StartOfNameBlock and num1 <= last_line:               
                    """ Lines related to top header block """
                    if  "Identification (as requested)" in line:  
                        EndOfNameBlock = num1
#                        print ("End Of Name Block :",EndOfNameBlock)
   
                    if "Client Tracking"  in line:
                        Client_Tracking_line = num1
                    if "Requested by"  in line:
                        Requested_by_line = num1
                    if "Client Code"  in line:
                        Client_Code_line = num1
                    if "Date requested"  in line:
                        Date_requested_line = num1
                    if "Report ID"  in line:
                        Report_ID_line = num1
#                        print ("Report_ID_line" ,Report_ID_line)
                    if "Time requested"  in line:
                        Time_requested_line = num1
                    """ Lines Related to Block between Identification (as requested) 
                    and Residence Information (as requested)
                    """
                    if "Applicant's last name"  in line:
                        Applicants_last_name_line = num1
                    if "Residence Information (as requested)" in line:
                        Residence_Information_line = num1
                    """ End Of Residence Info Block """
#                    if   "File Variations" in line:
#                        File_Variations_line = num1
                       
                    if    "Database Residence Information" in line:
                        Database_Residence_Information_line = num1
                    if    "Database Employment Information" in line:
                        Database_Employment_Information_line = num1
                    if    "TruAlert - Applicant" in line:
                        TruAlert_Applicant_line = num1
                    if    "AKA Records" in line:
                        AKA_Records_line = num1
                    if    "Credit Score Information" in line:
                        Credit_Score_Information_line = num1
                    if    "Credit History" in line:
                        Credit_History_line = num1
                       
                    if "Opened" in line:
                       Opened_line.append(num1)
#                       Opened_line_Index.append(line.index("Opened"))
#                     
                    if    "TOTALS"  in line:
                       Totals_line=num1
                        Total_High_Credit_Index.append(line.index("High credit"))
                        Total_High_Balance_Index.append(line.index("High balance"))
                        Total_Past_Due_Index.append(line.index("Pastdue"))
                        Total_Payment_Index.append(line.index("Payment"))
                        Total_Balance_Index.append(line.index("Balance"))
                   
                       #line.next()
                       #print("Line Num ",xyz)
                       
#                if re.search('^ Creditor Information',line.strip()):
#                    last_line = num1
#                    print("last_line ", last_line)
#                    print (Report_Number,'\n',Borrower_Coborrower)
#                if re.search('$ TRANSUNION CREDIT REPORT', line):
#                           print ("test",line)
#                if  line.find("TRANSUNION CREDIT REPORT") > 1 :         
#                 print(num1,line,line[line.find("TRANSUNION CREDIT REPORT")])
               
                
        fr.close
        with io.open(examFileName,'r',encoding='utf-8',errors='ignore') as fr:
      
            
            for num1, line in enumerate(fr, 1):
                  
                    if num1 > StartOfNameBlock and num1 < EndOfNameBlock:
                        InstName.append(line[0:56].strip())
    #                    InstName = ''.join(map(str, InstName))
                        InstNameCSV = ''.join(map(str, InstName))
#                        print ("Report ID :", line[130:])
#                        print("Report_ID_line",num1, Report_ID_line)
#                        print("EndOfNameBlock",num1, EndOfNameBlock)
#                        print("last_line ", last_line)
#                        print ("Address ",InstNameCSV)
#                        print("\n")
                   
                    if num1 > Client_Tracking_line and num1 < Client_Code_line :
                        Client_Tracking_val.append(line[57:87].strip())
                        Client_Tracking_val_CSV = ''.join(map(str, Client_Tracking_val))
    #                    print ("Client Tracking :",line[57:87])
    #                    print("\n")
                   
                    if num1 > Client_Code_line and num1 < EndOfNameBlock :
                        Client_Code_val.append(line[57:87].strip())
                        Client_Code_val_CSV=''.join(map(str, Client_Code_val))
    #                    print ("Client Code :",Client_Code_val)
    #                    print("\n")
                       
                    if num1 > Requested_by_line  and num1 < Date_requested_line:
                        Requested_by_val.append(line[88:130].strip())
                        Requested_by_val_CSV=''.join(map(str, Requested_by_val))
    #                     print ("Requested By :", line[88:130])
    #                     print("\n")
   
                    if num1 > Date_requested_line  and num1 < EndOfNameBlock:
                         Date_requested_val.append(line[88:130].strip())
                         Date_requested_val_CSV =''.join(map(str, Date_requested_val))
    #                     print ("Date Requested :", line[88:130])
    #                     print("\n")
                    if num1 > Report_ID_line  and num1 < Time_requested_line:
                             Report_ID_val.append(line[130:].strip())
                             Report_ID_val_CSV=''.join(map(str, Report_ID_val))
#                             print ("Report ID num :=",num1,Report_ID_val)
#                            
#                             print ("Report ID2 :", line)
    #                     print("\n")
   
                    if num1 > Time_requested_line and num1 < EndOfNameBlock:
                        Time_requested_val.append(line[130:].strip())
                        Time_requested_val_CSV=''.join(map(str, Time_requested_val))
    #                     print ("Time Requested :", line[130:])
    #                     print("\n")
                    if num1 > Applicants_last_name_line and num1 < Residence_Information_line:
                        Applicants_last_name_val.append(line[0:45].strip())
                        Applicants_last_name_val_CSV = ''.join(map(str, Applicants_last_name_val))
                        First_Name_val.append(line[45:91].strip())
                        First_Name_val_CSV=''.join(map(str,First_Name_val))
                        DOB_val.append(line[117:136].strip())
                        DOB_val_CSV=''.join(map(str,DOB_val))
                        SSN_val.append(line[137:].strip())
                        SSN_val_CSV = ''.join(map(str,SSN_val))
                    if num1 > Residence_Information_line and num1 < (Residence_Information_line+3):
                            line = line.strip()
                            line = line.replace("     ",'') 
                            line = line.replace("Present",'')
                            Present_Residence_val.append(line[0:])
                            Present_Residence_val_CSV=''.join(map(str,Present_Residence_val))
                    if num1 > Database_Residence_Information_line and num1 < Database_Employment_Information_line:   
                             
                            line = line.replace("       ",'')
                            line = line.replace("\n",'--Next Address--')
                            line = line.strip()
#                            line = line.replace("--Next Address----Next Address--","Next Address")
                            Previous_residence_val.append(line[0:])
                            Previous_residence_val_CSV = ''.join(map(str,Previous_residence_val))
                    if num1> Database_Employment_Information_line and  num1 < TruAlert_Applicant_line:
                            line = line.strip()
                            line = line.replace("     ",'')                           
                            Employment_Info_val.append(line[0:])
                            Employment_Info_val_CSV = ''.join(map(str,Employment_Info_val))
       
        
                    if  num1 > AKA_Records_line and num1 < Credit_Score_Information_line:
                            #line = line.strip()
                            #line = line.replace("     ",'')
                            line = line.replace("\n",'--')
                            line = line.strip()
                            AKA_val.append(line[0:])
                            AKA_val_CSV = ''.join(map(str,AKA_val))
      
                    if  num1 > Credit_Score_Information_line and num1 < Credit_History_line:
                        credit_score_val.append(line[0:13].strip())
                       credit_score_val_CSV=''.join(map(str,credit_score_val))
                   
                    #print((Opened_line[1]))
                    j =0
                    for i,item in enumerate(Opened_line):
                       #print (item)
#                       line = line.strip()
#                       line = line.replace("    ",'')
                          if num1 == item:
                            #Opened_line_Index = np.vstack([line.index("Opened")]) 
                           Opened_line_Index.append(line.index("Opened"))
                           Reported_Index.append(line.index("Reported"))
                           High_balance_Index.append(line.index("High balance"))
                           Reviewed_Index.append(line.index("Reviewed"))
                           Thirty_Index.append(line.index("30"))
                           Sixty_Index.append(line.index("60"))
                           Ninty_Index.append(line.index("90+"))
                           Pastdue_Index.append(line.index("Pastdue"))
                           Payment_Index.append(line.index("Payment"))
                           Balance_Index.append(line.index("Balance"))
                           #print (item1)
                          if num1 == item+2:
                              # print (Opened_line_Index[j],Reported_Index[j])
#                               print (num1,"Inst :",line[0:Opened_line_Index[j]-2].strip(),
#                               " Opened :",line[Opened_line_Index[j]:Reported_Index[j]-2].strip(),
#                               " Reported :", line[Reported_Index[j]:High_balance_Index[j]-2].strip()
#                               ," High Balance :",line[High_balance_Index[j]:Reviewed_Index[j]-2].strip(),
#                                " Reviewed :", line[Reviewed_Index[j]:Thirty_Index[j]-2].strip(),
#                                " Thirty :",line[Thirty_Index[j]:Sixty_Index[j]-2].strip(),
#                                " Sixty :",line[Sixty_Index[j]:Ninty_Index[j]-2].strip(),
#                                " Ninty :",line[Ninty_Index[j]:Pastdue_Index[j]-2].strip()
#                                )
                               Inst_CSV = np.vstack([Inst_CSV,line[0:Opened_line_Index[j]-2].strip()])
                              Opened_CSV = np.vstack([Opened_CSV,line[Opened_line_Index[j]:Reported_Index[j]-2].strip()])
                               Reported_CSV = np.vstack([Reported_CSV,line[Reported_Index[j]:High_balance_Index[j]-2].strip()])
                               High_Balance_CSV = np.vstack([High_Balance_CSV,line[High_balance_Index[j]:Reviewed_Index[j]-2].strip()])
                               Reviewed_CSV = np.vstack([Reviewed_CSV,line[Reviewed_Index[j]:Thirty_Index[j]-2].strip()])
                               Thirty_CSV = np.vstack([Thirty_CSV,line[Thirty_Index[j]:Sixty_Index[j]-2].strip()])
                               Sixty_CSV = np.vstack([Sixty_CSV,line[Sixty_Index[j]:Ninty_Index[j]-2].strip()])
                               Ninty_CSV = np.vstack([Ninty_CSV,line[Ninty_Index[j]:Pastdue_Index[j]-2].strip()])
                          if num1 == item +4:
                              #print (line)
                              Pastdue_CSV= np.vstack([Pastdue_CSV,line[Pastdue_Index[j]-1:Payment_Index[j]-2]])
                              Payment_CSV=np.vstack([Payment_CSV,line[Payment_Index[j]-2:Balance_Index[j]-2]])
                              Balance_CSV=np.vstack([Balance_CSV,line[Balance_Index[j]-2:].strip()])
                              #print("PAS D:",Pastdue_CSV,"PAY:",Payment_CSV,"Bal:",Balance_CSV)
#                              print("Bal:",Balance_CSV)
 
#                              print ("Item Plu 4", num1, line.strip())
                              Last_active_Index.append(line.index("Last active"))
                              BU1_index.append(line.index("BU1"))
                              High_limit_index.append(line.index("High limit"))
                              try:
                                  Install_index.append(line.index("Install"))
                              except:
                                  Install_index.append(line.index("Revolv"))
#                              print(line[0:Last_active_Index[j]].strip())
                              test = line[0:Last_active_Index[j]].strip()
                             
                          if num1 == item+6:
                            idx = line[0:Last_active_Index[j]].strip() 
                            if idx == '':
                                idx = test
                            Acct_Num_CSV = np.vstack([Acct_Num_CSV,idx])
#                            else:
#                                idx = line[0:Last_active_Index[j]].strip()
#                            print(num1,"Acct Number:", idx,
#                                  "Last Active :", line[Last_active_Index[j]:BU1_index[j]-2].strip(),
#                                  "BU1 :",line[BU1_index[j]:High_limit_index[j]-2].strip() ,
#                                  "High Limit:", line[High_limit_index[j]:Install_index[j]-2].strip(),
#                                  "Install Or Revolv:",line[Install_index[j]-2:].strip())
                            Last_Active_CSV = np.vstack([Last_Active_CSV,line[Last_active_Index[j]-1:BU1_index[j]-2].strip()])
                            BU1_CSV=np.vstack([BU1_CSV,line[BU1_index[j]-1:High_limit_index[j]-2].strip()])
                            High_Limit_CSV=np.vstack([High_Limit_CSV,line[High_limit_index[j]:Install_index[j]-9].strip()])
                            Install_Or_Revolv_CSV=np.vstack([Install_Or_Revolv_CSV,line[Install_index[j]-9:].strip()])
                       #print (Opened_line_Index, line.index("Opened"))
                          
#                          print ("Ordered ",line)
#                          print ("Ordered ",line.split())
#                          print (num1,"Inst : ",line[0:(open_line-1)], "Open Dt ", line[32:45])
                          j = j+1
                    #print("Help ",Opened_line_Index[0:1])
                    if  num1 >= Totals_line and num1 <= Totals_line+2:
                        #print (line.replace("High credit",'') )
                        #line =line.replace("High credit",'')
                        #line = line.strip()
                       if num1 == Totals_line+2:
                        Total_High_Credit.append(line[Total_High_Credit_Index[0]-2:Total_High_Balance_Index[0]-2])
                        Total_High_Credit=''.join(map(str,Total_High_Credit))
                        Total_High_Balance.append(line[Total_High_Balance_Index[0]-2:Total_Past_Due_Index[0]].strip())
                        Total_High_Balance=''.join(map(str,Total_High_Balance))
                        Total_Past_Due.append(line[Total_Past_Due_Index[0]:Total_Payment_Index[0]-1].strip())
                        Total_Past_Due=''.join(map(str,Total_Past_Due))
                        Total_Payment.append(line[Total_Payment_Index[0]-2:Total_Balance_Index[0]-2].strip())
                        Total_Payment=''.join(map(str,Total_Payment))
                        Total_Balance.append(line[Total_Balance_Index[0]-2:].strip())
                        Total_Balance=''.join(map(str,Total_Balance))
#                        print ("Total_High_Credit:",Total_High_Credit
#                              ,"\n Total_High_Balance:",Total_High_Balance
#                              ,"\n Total_Past_Due:",Total_Past_Due
#                              ,"\n Total_Payment:", Total_Payment
#                              ,"\n Total_Balance:",Total_Balance )
        fr.close      
        #print((Opened_line[0].value()))
#        print("Number Of Open Index :",len(Opened_line_Index))
#        print("Number Of Open Line",len(Opened_line),Opened_line[0:2])
#        for i , item in enumerate(Opened_line):
#                       print ("I Value",Opened_line[i],item)
#                       if num1 == i+2:
#                          print ("Ordered ",line)
       
#        print ("Req Inst Name :",InstNameCSV,"\n Clinet Tracking :",Client_Tracking_val_CSV,"\n- Client Code :"
#        ,Client_Code_val_CSV,"\n Requested By :",Requested_by_val_CSV,"\n Date Requested :",Date_requested_val_CSV
#        ,"\n Report ID :"
#        ,Report_ID_val_CSV,"\n Time Requested :",Time_requested_val_CSV,"\n Appli Name :",Applicants_last_name_val_CSV,"\n First Name :"
#        , First_Name_val_CSV, "\n DOB :", DOB_val_CSV
#         ,"\n SSN :", SSN_val_CSV,"\n Present Residence :", Present_Residence_val_CSV
#         ,"\n Prev Resid :",Previous_residence_val_CSV,"\n Employment :",Employment_Info_val_CSV,
#         "\n AKA :", AKA_val_CSV, "\n Credit Score :", credit_score_val_CSV)
        
        """
         "File_Name","Req_Inst_Name","Clinet_Tracking","Client_Code","Requested_By","Date Requested","Report_ID","Time_Requested","Applicant_Name",
         "First_Name","Date_Of_Birth","SSN","Present_Residence","Previous_Residence","Employment","AKA","Credit_Score",
         "Inst_Name","Opened","Reported","High_Balance","Reviewed","Thirty","Sixty","Ninty"
         filename,InstNameCSV,Client_Tracking_val_CSV,Client_Code_val_CSV,Requested_by_val_CSV,Date_requested_val_CSV,Report_ID_val_CSV
         ,Time_requested_val_CSV,Applicants_last_name_val_CSV,First_Name_val_CSV,DOB_val_CSV,SSN_val_CSV,Present_Residence_val_CSV,
         Previous_residence_val_CSV,Employment_Info_val_CSV,AKA_val_CSV,credit_score_val_CSV,Inst_CSV[k],Opened_CSV[k],Reported_CSV[k],
         High_Balance_CSV[k],Reviewed_CSV[k],Thirty_CSV[k],Sixty_CSV[k],Ninty_CSV[k]
        """
        for k in range(1,len(Opened_CSV)):
         writer.writerow((filename,InstNameCSV,''.join(map(str,Inst_CSV[k])),''.join(map(str,Acct_Num_CSV[k])),Client_Tracking_val_CSV,Client_Code_val_CSV,Requested_by_val_CSV,Date_requested_val_CSV,Report_ID_val_CSV
         ,Time_requested_val_CSV,Applicants_last_name_val_CSV,First_Name_val_CSV,DOB_val_CSV,SSN_val_CSV,Present_Residence_val_CSV,
         Previous_residence_val_CSV,Employment_Info_val_CSV,AKA_val_CSV,credit_score_val_CSV,
         ''.join(map(str,Opened_CSV[k])),''.join(map(str,Reported_CSV[k])),
         ''.join(map(str,High_Balance_CSV[k])),''.join(map(str,Reviewed_CSV[k])),''.join(map(str,Thirty_CSV[k]))
         ,''.join(map(str,Sixty_CSV[k])),''.join(map(str,Ninty_CSV[k])),''.join(map(str,Last_Active_CSV[k]))
         ,''.join(map(str,BU1_CSV[k])), ''.join(map(str,High_Limit_CSV[k]))
         , ''.join(map(str,Install_Or_Revolv_CSV[k])),''.join(map(str,Pastdue_CSV[k])),''.join(map(str,Payment_CSV[k])),''.join(map(str,Balance_CSV[k]))
         ,Total_High_Credit,Total_High_Balance
         ,Total_Past_Due,Total_Payment,Total_Balance))
        
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
