
import string
import re
import pandas as pd
import numpy as np
import sqlite3
import os
import sys


def read_txt(location):

    the_lines=[]
    f= open (location,"r")

    the_text =f.readline(0)
    print(the_text)
    for the_text in f:
        if the_text=="":
            break
         
        lines=the_text.split('\t')

        print(lines[-1])

        breakdown=lines[-1].split()
        
        dissect_sensor_string(breakdown)



def read_all_sensor_files():
    """List sensor files in the designated directory and open each file"""

    os.chdir(r'J:\Jim Dowd\SENSOR STATUS')
    dir_list=os.listdir()
    
    for k in dir_list:
    
        if k[0:6]=='SENSOR' and k.endswith('2019.TXT'):
            print (k)
            
            sensor_file=open('J:\\Jim Dowd\\SENSOR STATUS\\'+k)
            
            the_text=sensor_file.readline(0)
            print(the_text)
            for the_text in sensor_file:
                if the_text=="":
                    break
                print(the_text)

                lines=the_text.split('\t')

                print(lines[-1])

                breakdown=lines[-1].split()
                
                df=dissect_sensor_string(breakdown)


            sensor_file.close()

    return df       


    
def word_count(lines):
    fart={}
    for word in lines:
        if word not in fart:
            fart[word]=1
        else:
            fart[word]+=1
    print ('word count dict:\n',fart,'\n')

    sort_it_1(fart)
    sort_by_value(fart)


def sort_it_1(fart):
    lst=list(fart.keys())
    lst.sort()
    print('the keys:\n',lst,'\n')
    for key in lst:
        print(key,fart[key])

def sort_by_value(fart):
    lst=list()
    for key,val in list(fart.items()):

        lst.append((val,key))
        lst.sort(reverse=True)
    for key,val in lst:
        print(key,val)


def remove_stock_words(lines):
    R=['the','on','for','is','to','that','in','a','with','of','and','this','as','at']
    R2=['*','&','-','/','!','@','_','<','>']
    setA=set(R+R2)
    setB=set(lines)

    print('set R:\n',setA,'\n')
    print('sorted word list:\n',lines,'\n')
    print('set B:\n',setB,'\n')

    no_the=setB.difference(setA)
    print('without the:\n', no_the,'\n')
    stuff_removed=list(no_the)
    print('stuff removed:',stuff_removed)


def search_1(the_text):
    print(the_text)
##    x = re.findall("PSI", the_text)
##    print(x)

    x = re.findall("\d{1}-\d{5}"+"PSI", the_text)
    print(x)

##    x = re.findall("0-..0", the_text)
##    print(x)

##    x = re.findall("[PSI]", the_text)
##    print(x)

    p=re.compile(r'PSI')
    x=p.findall(the_text)
    print(x)

    p=re.compile(r'\t')
    x=p.findall(the_text)
    print(x)

    x = re.findall("\d{1}-\d{2}-\d{4}", the_text)
    print(x)
    
def dissect_sensor_string(breakdown):

    mfr.append(breakdown[4]+' '+breakdown[5])

    model_number.append(breakdown[6])
    serial_number.append(breakdown[7])
    sensor_range.append(breakdown[8])
    recert_due.append(breakdown[9])

    print(model_number[-1])
    print(serial_number[-1])

    asset_description.append(get_asset_descriptor(sensor_range[-1]))
    lab_id.append(get_lab_id(asset_description[-1], serial_number[-1]))

    sensor={'Model':model_number,
            'Make':mfr,
            'Serial_No.':serial_number,
            'Sensor_Range':sensor_range,
            'Recert_Date':recert_due,
            'Lab_ID':lab_id}

    print(sensor)
    
    for k in sensor.items():
        print (k)

    df=create_sensor_dataframe(sensor)
    return df
    

def get_asset_descriptor(sensor_range):
    print(sensor_range)

    ranges=[ '0-30PSI',
         '0-60PSI',
         '0-100PSI',
         '0-300PSI',
         '0-600PSI',
         '0-1000PSI',
         '0-3000PSI',
         '0-5000PSI',
         '0-10000PSI',
         '0-15000PSI',
         '0-20000PSI',
         '0-30000PSI',
         '0-40000PSI',
         '0-50000PSI']

    asset_descript=['30 PSI',
                '60 PSI',
                '100 PSI',
                '300 PSI',
                '600 PSI',
                '1 KSI',
                '3 KSI',
                '5 KSI',
                '10 KSI',
                '15 KSI',
                '20 KSI',
                '30 KSI',
                '40 KSI',
                '50 KSI']

    if sensor_range in ranges:
        i=ranges.index(sensor_range)
        the_asset_descript=asset_descript[i]
        print (the_asset_descript)

    return the_asset_descript



def get_lab_id(asset_description, serial_number):
    lab_id=asset_description+'-'+serial_number

    return lab_id

def create_sensor_dataframe(sensor_dict):
    df=pd.DataFrame.from_dict(sensor_dict)

    print (df)
    return df
    


if __name__ == "__main__":

    global mfr,model_number,serial_number,sensor_range,recert_due,asset_description,lab_id,df
    mfr=[]
    model_number=[]
    serial_number=[]
    sensor_range=[]
    recert_due=[]
    asset_description=[]
    lab_id=[]

    
##    location=r'J:\Jim Dowd\SENSOR STATUS\SENSOR UPDATE - 03-08-2019.TXT'
##    read_txt(location)
    df=read_all_sensor_files()


