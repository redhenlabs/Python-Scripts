# -*- coding: utf-8 -*-
"""

Compares Columns of 2 Different CSV files 
def test_run()
1.  gets the masster and the credit file 
2. Changes the name of application numver column to report numnber
3. Splits the application number column based on the "-" 

def compare()
4. reindexes the column to be compared
5. merge it 

generate_result()
6. Store the diff result in a new file

"""

import pandas as pd
 
infile_master_dir = "<< /Add the path to your file directory />>"
infile_master ="<Name of your CSV file>.csv"
 
credit_file_dir="/Add the path to your file directory /"
credit_file = "<<Name of your CSV file>>.csv"
def test_run():
  
    df = pd.read_csv(infile_master_dir+infile_master,  usecols=['Application Number'],na_values=['nan'])

    df = df.rename(columns = {'Application Number':'ReportNumber' })
    df = df.drop_duplicates()

    df.ReportNumber = df.ReportNumber.map(lambda x: x.split('-')[0])
    df['ReportNumber'] = df['ReportNumber'].astype(str).convert_objects(convert_numeric=True)
    print( (df.ReportNumber.head()))
   
    df_crd = pd.read_csv(credit_file_dir+credit_file,  usecols=['ReportNumber'],na_values=['nan'])

 
    df_crd = df_crd.drop_duplicates()

   
    df.ReportNumber.to_csv('master.csv', header=True)
    df_crd.ReportNumber.to_csv('creditreport.csv',header=True)
              
def compare():
    df_mst = pd.read_csv('master.csv',  usecols=['ReportNumber'],na_values=['nan'])
    df_det = pd.read_csv('creditreport.csv',  usecols=['ReportNumber'],na_values=['nan'])
   
    df_mst.sort(columns="ReportNumber")
    df_mst=df_mst.reindex()
    df_det.sort(columns="ReportNumber")
    df_det=df_det.reindex()   
    

   
    print(df_mst.head(),"\n",df_det.head())
    print("\n DETAIL :",df_det.dtypes)
    print("\n MASTER :",df_mst.dtypes )

   
    dfs = pd.DataFrame({})
    for name, group in df_det.groupby('ReportNumber'):
        buffer_df = pd.DataFrame({'ReportNumber': group['ReportNumber'][:1]})
        i = 0
        for index, value in group['ReportNumber'].iteritems():
            i += 1
            string = 'Column_' + str(i)
            buffer_df[string] = value
   
        dfs = dfs.append(buffer_df)
   
    result = pd.merge(df_mst, dfs, how='left', on='ReportNumber')
    dfsr = pd.DataFrame({})
    dfsr = result
    dfsr.to_csv('result.csv', header=True)
    print(result.head)
   

def generate_result():
   
    df_rslt = pd.read_csv('result.csv',  usecols=['ReportNumber','Column_1'],na_values=['nan'])
    newdf = df_rslt[(df_rslt['Column_1'].isnull() ) & (df_rslt['ReportNumber'].notnull() )]

 
    newdf.to_csv('missing_application_number_report.csv', header=True)
    print(newdf.head())
   
    
if __name__ == "__main__":
    test_run()
    compare()
    generate_result()