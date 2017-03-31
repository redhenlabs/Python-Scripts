# -*- coding: utf-8 -*-
"""
For Transforming Excel based credit reports to CSV
"""
"""
This reads all excel files ( in this case DTI credit history files provided by credit bureau ),

It picks up specific fields that's required for my analysis.

"Report Number",
"File_Name",
"Record Type",
"Effective_Date",
"Borrower_Name",
"ILE",
"Total_Monthly_Debt",
"Total_Monthly_Income",
"DTI",
"Minimum_ILE",
"Retained_Student_Loan_Payment",
"Refi_Consolidation_Student_Loan_Payment",
"Modified_Debt_to_Income_Ratio"

"""

 
import xlrd
import csv
import os
import io
import re
 
dirname = "<Your Input file directory name/>"
outdirname = "<Your out put directory name/>"
csvfilename="FICO_SCORE.csv"
 
 
def open_file( dirname, outdirname, csvfilename):
  dirname = dirname
  outdirname = outdirname
  csvfilename = csvfilename
  examFileName = os.listdir(dirname)
 
  with io.open(outdirname + "/" + csvfilename,'w',encoding='ascii',errors='replace') as out_file:   
    writer = csv.writer(out_file)
    writer.writerow(("Report Number","File_Name","Record Type","Effective_Date","Borrower_Name","ILE","Total_Monthly_Debt","Total_Monthly_Income","DTI","Minimum_ILE","Retained_Student_Loan_Payment","Refi_Consolidation_Student_Loan_Payment","Modified_Debt_to_Income_Ratio"))   
 
    for filename in examFileName:
        DTI_Calculations_header =''
        ILE_COL = ''
        ILE_COL_VAL =''
        Total_Monthly_Debt_COL = ''
        Total_Monthly_Debt_COL_VAL = ''
        Total_Monthly_Income_COL= ''
        Total_Monthly_Income_VAL =''
        DTI_COL =''
        DTI_COL_VAL=''
        Minimum_ILE_COL=''
        Minimum_ILE_COL_VAL=''
        Effective_Date =''
        Borrower_Name = ''
        Retained_Student_Loan_Payment=''
        Refi_Consolidation_Student_Loan_Payment=''
        Modified_Debt_to_Income_Ratio=''
        examFileName = dirname + "/" + filename
       
        book = xlrd.open_workbook(examFileName)
        
       
        
        
        DTI_Sheet = book.sheet_by_name('DTI')
       
        for rowidx in range(DTI_Sheet.nrows):
            row = DTI_Sheet.row(rowidx)
            for colidx, cell in enumerate(row):
                if cell.value == "DTI Calculations" :

                    print (DTI_Sheet.cell(rowidx,colidx))
                    print (DTI_Sheet.cell(rowidx+1,colidx))
                    print (DTI_Sheet.cell(rowidx+1,colidx+2))
                    print (DTI_Sheet.cell(rowidx+2,colidx))
                    print (DTI_Sheet.cell(rowidx+2,colidx+2))
                    print (DTI_Sheet.cell(rowidx+3,colidx))
                    print (DTI_Sheet.cell(rowidx+3,colidx+2))
                    print (DTI_Sheet.cell(rowidx+4,colidx))
                    print (DTI_Sheet.cell(rowidx+4,colidx+2))
                    print (DTI_Sheet.cell(rowidx+5,colidx))
                    print (DTI_Sheet.cell(rowidx+5,colidx+2))
                   
                    DTI_Calculations_header = DTI_Sheet.cell_value(rowidx,colidx)
                    ILE_COL = DTI_Sheet.cell_value(rowidx+1,colidx)
                    ILE_COL_VAL = DTI_Sheet.cell_value(rowidx+1,colidx+2)
                    Total_Monthly_Debt_COL = DTI_Sheet.cell_value(rowidx+2,colidx)
                    Total_Monthly_Debt_COL_VAL = DTI_Sheet.cell_value(rowidx+2,colidx+2)
                    Total_Monthly_Income_COL = DTI_Sheet.cell_value(rowidx+3,colidx)
                    Total_Monthly_Income_VAL =DTI_Sheet.cell_value(rowidx+3,colidx+2)
                    DTI_COL=DTI_Sheet.cell_value(rowidx+4,colidx)
                    DTI_COL_VAL= DTI_Sheet.cell_value(rowidx+4,colidx+2)
                    Minimum_ILE_COL=DTI_Sheet.cell_value(rowidx+5,colidx)
                    Minimum_ILE_COL_VAL=DTI_Sheet.cell_value(rowidx+5,colidx+2)
#                    print (Total_Monthly_Debt_COL,Total_Monthly_Debt_COL_VAL,Minimum_ILE_COL,Minimum_ILE_COL_VAL)
                elif cell.value == "Debt to Income Ratio (Calculated)":
                    DTI_Calculations_header = DTI_Sheet.cell_value(rowidx,colidx)
                    Total_Monthly_Debt_COL_VAL = DTI_Sheet.cell_value(rowidx+2,colidx+1)
                    Total_Monthly_Income_VAL =  DTI_Sheet.cell_value(rowidx+4,colidx+1)
                    DTI_COL_VAL =  DTI_Sheet.cell_value(rowidx+6,colidx+1)
                    Retained_Student_Loan_Payment = DTI_Sheet.cell_value(rowidx+8,colidx+1)
                    Refi_Consolidation_Student_Loan_Payment = DTI_Sheet.cell_value(rowidx+9,colidx+1)
                    Modified_Debt_to_Income_Ratio = DTI_Sheet.cell_value(rowidx+11,colidx+1)
                    #Income for Living Exp.
                    ILE_COL_VAL = DTI_Sheet.cell_value(rowidx+12,colidx+1)
                if    "Effective Date:"  in str(cell.value):
                    print ("Col Index",colidx)
                    print ("Row Index",rowidx)
                    print (DTI_Sheet.cell(rowidx,colidx),"\n")
                    Effective_Date = DTI_Sheet.cell_value(rowidx,colidx)
                    Effective_Date=Effective_Date.replace("Effective Date:",'')
                if cell.value == "Borrower Name:":
                    print ("Col Index",colidx)
                    print ("Row Index",rowidx)
                    print (DTI_Sheet.cell(rowidx,colidx),"\n")
                    Borrower_Name =DTI_Sheet.cell_value(rowidx,colidx+1)
                elif cell.value == "BORROWER(S):":
                     Borrower_Name =DTI_Sheet.cell_value(rowidx,colidx+2)
                     print("test",Borrower_Name)
                     print ("Col Index",colidx)
                     print ("Row Index",rowidx)
#                remove_character = ['a','b','c','d']    
                report_number= re.sub("[^0-9,-]", "", filename)
                report_number=report_number.replace(',','')
#                report_number = filename.translate(None, ''.join(remove_character))     
        
        writer.writerow((report_number,filename,DTI_Calculations_header,Effective_Date,Borrower_Name,ILE_COL_VAL,Total_Monthly_Debt_COL_VAL,Total_Monthly_Income_VAL,DTI_COL_VAL,Minimum_ILE_COL_VAL,Retained_Student_Loan_Payment,Refi_Consolidation_Student_Loan_Payment,Modified_Debt_to_Income_Ratio))   
    out_file.close()
if __name__ == "__main__":
   
    #  args = sys.argv[1:]
#  if (len(args) != 3):
#    print("Usage: python arrange_headers.py <Directory for the E-mail files> <Output Directory> <csvfilename>")
#    sys.exit(1)
#  dirname = args[0]
#  outdirname = args[1]
#  csvfilename = args[2]
  ah = open_file(dirname, outdirname, csvfilename)
 