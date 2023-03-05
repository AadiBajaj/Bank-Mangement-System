def create_table(name):
    row1={}
    name1=name
    name+='.dat'
    table_location(name)
    try:
        f=open(name,'r')
        f.close()
    except FileNotFoundError:
       test="false"
    else:
       test="true" 
    if test=="true":
        print("The file already exist ")
        test=input("Do you want to continue Yes/No: ")
        print(test)
        test=test.capitalize()
    if test=="false":
        print("To Stop type nil in column name ")
        import pickle
        f=open(name,'+wb')
        while 0<1:
            column_name=input("Column name ")     
            if column_name!="nil":
                row=input("value for first row ") 
            else:
                break
            row1[column_name]=[row]
        pickle.dump(row1,f)
        f.close()
        while 0<1:
            a=input("do you want to continue or not?(y/n)")
            a=a.capitalize()
            if a=="N":
                break
            elif a=="Y":
                add_row(name1)
                print("row added")
        print("The table has been created ")
    elif test=="Yes":
        print("To Stop type nil in column name ")
        import pickle
        f=open(name,'+wb')
        while 0<1:
            column_name=input("Column name ")     
            if column_name!="nil":
                row=input("value for first row ") 
            else:
                break
            row1[column_name]=[row]
        pickle.dump(row1,f)
        f.close()
        while 0<1:
            a=input("do you want to continue or not?(y/n)")
            a=a.capitalize()
            if a=="N":
                break
            elif a=="Y":
                add_row(name1)
                print("row added")
        print("The table has been created ")
def column_list(name):
    import pickle
    name+='.dat'
    path=table_location(name)
    test=file_nameerror(path)
    if test=="true":
        f=open(path,'rb')
        table=pickle.load(f)
        column=[]
        for i in table:
            column+=[i]
        f.close()
        return column
def add_row(name):
         import pickle
         name1=name
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
                 f=open(path,'rb')
                 table=pickle.load(f)
                 f.close()
                 col=column_list(name1)
                 for i in col:
                     data=table[i]
                     print(i)
                     rown=input("Enter Value ")
                     data+=[rown]
                     table[i]=data
                 f=open(name,'+wb')
                 pickle.dump(table,f)
                 f.close()
                 print("The row has been added ")
def delete_row(name,col,row_data):
         import pickle
         name1=name
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
                 test=column_error(name1,col)
                 if test=="true":
                     test=data_error(path,col,row_data)
                     if test=="true":
                         f=open(path,'rb')
                         table=pickle.load(f)
                         f.close()
                         column_data=table[col]
                         n=column_data.index(row_data)
                         table_new={}
                         for columns in table:
                             column_data=table[columns]
                             column_data.pop(n)
                             table_new[columns]=column_data
                         f=open(name,'+wb')
                         pickle.dump(table_new,f)
                         f.close()
                         print("The row has been deleted ")
def display_table(name):
    try:
         import pickle
         name1=name
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
                 f=open(path,'rb')
                 table=pickle.load(f)
                 for column in table:
                     print(column,'\t',end='\t')
                     column_data=table[column]
                     n=len(column_data)
                 print('\n')
                 list=column_list(name1)
                 for i in range(0,n):
                     for j in list:
                         data=table[j]
                         print(data[i],'\t',end='\t')
                     print('\n')
                 f.close()
    except UnboundLocalError:
        print("The data of file is cleared")
    else:
        print(" ")
def add_column(name,column_name):
         import pickle
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
                 f=open(path,'rb')
                 table=pickle.load(f)
                 for column in table:
                     column_data=table[column]
                     n=len(column_data)
                 row_data=[]
                 for i in range(0,n):
                     print("row",i+1)
                     data=input("Value ")
                     row_data+=[data]
                 table[column_name]=row_data
                 f=open(name,'+wb')
                 pickle.dump(table,f)
                 f.close()
                 print("The column has been added ")
def remove_column(name,column_name):
         import pickle
         name1=name
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
             test=column_error(name1,column_name)
             if test=="true":
                 f=open(path,'rb')
                 table=pickle.load(f)
                 table_new={}
                 for column in table:
                     if column!=column_name:
                         column_data=table[column]
                         table_new[column]=column_data
                 f=open(name,'+wb')
                 pickle.dump(table_new,f)
                 f.close()
                 print("The column has been removed ")
def delete_table(name):
         import os
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
             os.remove(path)
             print("The table has been deleted ")
         
def backup(name,backup_name):
         import pickle
         name+='.dat'
         backup_name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
             f=open(path,'rb')
             table=pickle.load(f)
             f.close()
             f1=open(backup_name,'+wb')
             pickle.dump(table,f1)
             f.close()
             print("The backup has been taken ")
def rename_column(name,old_column,new_column):
         import pickle
         name1=name
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
             test=column_error(name1,old_column)
             if test=="true":
                 f=open(path,'rb')
                 table=pickle.load(f)
                 table_new={}
                 for column in table:
                     if column!=old_column:
                         column_data=table[column]
                         table_new[column]=column_data
                     elif column==old_column:
                         column_data=table[old_column]
                         table_new[new_column]=column_data
                 f=open(name,'+wb')
                 pickle.dump(table_new,f)
                 f.close()
                 print("column renamed ")
def update(name,column,old_data,new_data):
         import pickle
         name1=name
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
             test=column_error(name1,column)
             if test=="true":
                  test=data_error(path,column,old_data)
                  if test=="true":
                     f=open(path,'rb')
                     table=pickle.load(f)
                     table_new={}
                     changed_data=[]
                     for columns in table:
                         column_data=table[columns]
                         if columns==column:
                             for i in column_data:
                                 if i==old_data:
                                     changed_data+=[new_data]
                         
                                 else:
                                     changed_data+=[i]
                                 table_new[column]=changed_data
                         else:
                             table_new[columns]=column_data
                     f=open(name,'+wb')
                     pickle.dump(table_new,f)
                     f.close()
                     print("The data updated ")
def clear_data(name):
         import pickle
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
             table_new={}
             f=open(path,'+wb')
             pickle.dump(table_new,f)
             f.close()
             print("The data cleared ")
def find_row(name,column,row_dt):
         import pickle
         name1=name
         name+='.dat'
         path=table_location(name)
         test=file_nameerror(path)
         if test=="true":
             test=column_error(name1,column)
             if test=="true":
                  test=data_error(path,column,row_dt)
                  if test=="true":
                     f=open(path,'rb')
                     table=pickle.load(f)
                     for columns in table:
                         print(columns,end='\t')
                         if columns==column:
                             column_data=table[columns]                
                             n=column_data.index(row_dt)
                     print('\n')
                     row=row_data(name1,n+1)
                     for i in row:
                         print(i,end='\t')
                     print('\n',"The data is present in",n+1,"row")
                     f.close()
def row_data(name,n):
         import pickle
         binary=name+'.dat'
         path=table_location(binary)
         test=file_nameerror(path)
         if test=="true":
             f=open(path,'rb')
             table=pickle.load(f)
             the_row=[]
             for columns in table:
                     column=table[columns]
                     column_data=column[n-1]
                     the_row+=[column_data]
             return the_row
def convert_csv(name):
         import pickle
         binary=name+'.dat'
         path=table_location(binary)
         test=file_nameerror(path)
         if test=="true":
             f=open(path,'rb')
             table=pickle.load(f)
             f.close()
             import csv
             file=name+'.csv'
             f1=open(file,'+w')
             wrt=csv.writer(f1)
             list=column_list(name)
             wrt.writerow(list)
             column=list[0]
             column_data=table[column]
             n=len(column_data)
             for i in range(0,n):
                 row=row_data(name,i+1)
                 wrt.writerow(row)
             f.close()
             print(file,"is created")
def table_location(name):
        import os
        binary=name
        path=os.path.abspath(binary)
        return path

def show_choices():
    print('Menu')
    print('1. Create Table')
    print('2. Add Row')
    print('3. Delete Row')
    print('4. Show Table')
    print("5. Add Column")
    print("6. Delete Column")
    print("7. Backup")
    print("8. Delete Table")
    print("9. Clear Data")
    print('10. Rename Column')
    print("11. Update Row")
    print("12. Search")
    print("13. Convert Into CSV File")
    print("14. Exit")

def main():
    while(True):
        show_choices()
        name=input("Enter name of the file: ")
        choice = input('Enter choice(1-14): ')
        print()
        
        if choice == '1':
            create_table(name) 
           
        elif choice == '2':
            add_row(name)
            
        elif choice == '3':
            col=input("Enter the column Name :")
            row_data=input("Enter row data :")
            delete_row(name,col,row_data)
        
        elif choice == "4":
            display_table(name)

        elif choice == "5":
            column_name=input("Enter the name of the column to be added: ")
            add_column(name,column_name)
            
        elif choice == "6":
            column_name=input("Enter the name of the column to be deleted: ")
            remove_column(name,column_name)
            
        elif choice == "7":
           backup_name= input("Enter Backup name: ")
           backup(name,backup_name)

        elif choice == "8":
            delete_table(name)
            
        elif choice == "9":
            clear_data(name)   

        elif choice == "10":
            old_column=input("enter old_column")
            new_column=input("enter new_column")
            rename_column(name,old_column,new_column)

        elif choice == "11":
            column=input("enter column name")
            old_data=input ("enter old_data")
            new_data = input("enter new_data")
            update(name,column,old_data,new_data)
            
        elif choice == "12":
            column= input("enter column")
            row_dt=input("enter row data")
            find_row(name,column,row_dt)
            
        elif choice == "13":
            convert_csv(name)
            
        elif choice == "14":
            break
    
        else:
            print('Invalid input')
def file_nameerror(name):
   try:
        f=open(name,'r')
        f.close()
   except FileNotFoundError:
       print("file does not exsist")
       return "false"
   else:
       return "true" 
def column_error(name,col_name):
    list=column_list(name)
    if col_name in list:
        return "true"
    else:
        name+=".dat"
        print(col_name,"does not exsist","in",name)
def data_error(name,column,data):
    import pickle
    f=open(name,'rb')
    table=pickle.load(f)
    col=table[column]
    f.close()
    if data in col:
        return "true"
    else:
    
        print(data,"is not present in",column)   
main()            
