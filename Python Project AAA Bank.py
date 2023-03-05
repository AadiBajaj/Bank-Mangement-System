import mysql.connector as a
con = a.connect(host='localhost',user='root',password='aadi.aditya@123',database="bank2223")
def openAcc():
    n=input('Enter Name:')
    ac=int(input('Enter Account No:'))
    db=input('Enter D.O.B:')
    p=int(input('Enter Phone:'))
    ad=input('Enter Address:')
    ob=int(input('Enter Opening Balance:'))
    data1=(n,ac,db,p,ad,ob)
    data2=(n,ac,ob)
    sql1='insert into account value(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount value(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print('Data Entered Successfully')
    main()
def depoAmo():
    am=int(input('Enter Amount:'))
    ac=input('Enter Account No:')
    a="Select balance from amount where AccountNo=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql='Update amount set Balance =%s where AccountNo=%s'
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    main()
def witham():
    am=int(input('Enter Amount:'))
    ac=input('Enter Account No:')
    a='Select balance from amount where AccountNo =%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql='update amount set Balance =%s where AccountNo =%s'
    data=(tam,ac)
    c.execute(sql,data)
    con.commit()
    main()
def balance():
    ac=input('Enter Account N0:')
    a='Select balance from amount where AccountNo=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print('Balance for Account:',ac,'is',myresult[0])
    main()
def dispacc():
    ac=input('Enter Account NO:')
    a='Select*from account where AccountNo =%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end=' ')
        main()
def closeac():
    ac=input('Enter Account N0:')
    sql1='delete from account where AccountNo=%s'
    sql2='delete from amount where AccountNo =%s'
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()
def main():
    print("""
    1. OPEN NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE
    5. DISPLAY ACCOUNT DETAILS
    6. CLOSE AN ACCOUNT
    """)
    choice=input('Enter Task No:')
    while True:
        if(choice=='1'):
            openAcc()
        elif(choice=='2'):
            depoAmo()
        elif(choice=='3'):
            witham()
        elif(choice=='4'):
            balance()
        elif(choice=='5'):
            dispacc()
        elif(choice=='6'):
            closeac()
        else:
            print('Wrong choice........')
            main()
print("""𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝘼𝘼𝘼 𝘽𝙖𝙣𝙠
𝙁𝙤𝙧 𝙡𝙤𝙖𝙣, 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙤𝙣 𝙤𝙪𝙧 𝙩𝙤𝙡𝙡-𝙛𝙧𝙚𝙚 𝙣𝙪𝙢𝙗𝙚𝙧 𝟏𝟖𝟎𝟎 𝟏𝟎𝟑 𝟏𝟗𝟎𝟔""")            
main()
