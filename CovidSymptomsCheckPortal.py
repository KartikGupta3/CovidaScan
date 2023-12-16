import pickle
import os
import datetime
import mysql.connector as sqltor



print('WELCOME TO ABC HOSPITAL')
print('Today\'s Date is :')
print(datetime.date.today())
print("The Time You Entered This Page Was :")
print(datetime.datetime.now())




def Display_p():
    try:

        mydb=sqltor.connect(host="localhost",user="root",passwd="jamster##@",database="hospital")
        mycursor=mydb.cursor()
        sql="Select*from patient_details"
 
        mycursor.execute(sql)
        data=mycursor.fetchall()

        for i in data :
            print(i)
            print("*****************************************************")
            print()
    except Exception as e:
        print(e)
def Add_p():
    mydb=sqltor.connect(host="localhost",user="root",passwd="jamster##@",database="hospital")
    mycursor=mydb.cursor()
    p_id=int(input("Enter patient id:"))
    p_name=input("Enter patient's full name:")
    p_age=int(input("Enter patient's age:"))
    p_sex=input("Enter patient's sex:")
    p_bg=input("Enter blood group:")
    p_address=input("Enter patient's address:")
    p_phone=int(input("Enter pateint's contact number(10 digits):"))
    sql="INSERT INTO patient_details(p_id,p_name,p_age,p_sex,p_bg,p_address,p_phoneno)values({},'{}',{},'{}','{}','{}',{})".format(p_id,p_name,p_age,p_sex,p_bg,p_address,p_phone)
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()
    print("Record entered...")



    print("*****************************************************")
    print()

def Delete_p():

    mydb=sqltor.connect(host="localhost",user="root",passwd="jamster##@",database="hospital")
    mycursor=mydb.cursor()
    p_id=int(input("Enter the p_id of the patient whose record is to be deleted:"))
    sql="delete from patient_details where p_id={}".format(p_id)
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()
    print("Record deleted...")
    print("*****************************************************")
    print()
def Modify_p():

    mydb=sqltor.connect(host="localhost",user="root",passwd="jamster##@",database="hospital")
    mycursor=mydb.cursor()
    p_id=int(input("Enter the p_id of the patient whose record is to be modified:"))
    r=input("Enter the name of the column which needs modification:")
    if r=="p_name":
        n=input("Enter the modifications to be made in the patient's name:")
        sql="update patient_details set p_name='{}' where p_id={}".format(n,p_id)
        mycursor.execute(sql)

        print("Name modified")
    elif r=="p_age":
        a=input("Enter the modifications to be made in the patient's age:")
        sql="update patient_details set p_age={} where p_id={}".format(a,p_id)
        mycursor.execute(sql)
        print("Age modified")
    elif r=="p_sex":
        s=input("Enter the modifications to be made in the patient's sex:")
        sql="update patient_details set p_sex='{}' where p_id={}".format(s,p_id)
        mycursor.execute(sql)
        print("Sex modified")
    elif r=="p_bg":
        bg=input("Enter the modifications to be made in the patient's blood group:")
        sql="update patient_details set p_bg='{}' where p_id={}".format(bg,p_id)
        mycursor.execute(sql)
        print("Blood Group modified")
    elif r=="p_address":
        add=input("Enter the modifications to be made in the patient's address:")
        sql="update patient_details set p_address='{}' where p_id={}".format(add,p_id)
        mycursor.execute(sql)
        print("Address modified")
    elif r=="p_phoneno":
        p=input("Enter the modifications to be made in the patient's contact number:")
        sql="update patient_details set p_phoneno={} where p_id={}".format(p,p_id)
        mycursor.execute(sql)
        print("Contact number modified")
    else:
        print("Enter a valid column name. Try again.")

    mydb.commit()
    mydb.close()
    print("*****************************************************")
    print()


#MAIN PROGRAM


while True:

    print('===========================================MENU====================================================')
    print('1-Patient')
    print('2-Covid-19 Test')
    print('3-Exit')

    print('===================================================================================================')
    ch=int(input('Enter your choice(1-4):'))
    if ch==1:
        choice='Y'
        while choice.upper()=='Y' :
            print()
            print("1. Display all records")
            print("2. Enter records")
            print("3. Delete records")
            print("4. Modify records")
            print()
            ch=int(input("Enter a choice(1-4):"))
            if ch==1:
                Display_p()
            elif ch==2:
                Add_p()
            elif ch==3:
                Delete_p()
            elif ch==4:
                Modify_p()
            else:
                print("Wrong input...")


                break
            choice=input('Do you want to continue?(y/n): ')

    elif ch==2:
        print("\n\nLIST OF SYMPTOMS")
        print("\n#Most Common Symptoms#")
        print("1.Fever")
        print("2.Dry cough")
        print("3.Tiredness")
        print("\n#Serious Symptoms#")
        print("4.Difficulty breathing or shortness of breath")
        print("5.Chest pain or pressure")
        print("6.Loss of speech or movement")
        sym=eval(input("Enter the serial numbers in form of list of symptoms you are currently experiencing:"))
        n=len(sym)
        if n>3:
            print("SEEK IMMEDIATE MEDICAL HELP AND GET TESTED")
        else:
            print("MANAGE YOUR SYMPTOMS AT HOME")
       
    elif ch==3:
        print("\n\n=========================================THANkYOU==============================================")
        break







