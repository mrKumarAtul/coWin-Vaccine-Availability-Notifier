# -*- coding: utf-8 -*-
"""
Created on Sun May 16 06:58:00 2021

@author: atul.k
"""
from datetime import datetime
import winsound
import time


def user_input():
    #pin_code=[813103,804453,812001] #provide a list of preffered Pincode
    #preffered_date="16-05-2021" #Preffered format is DD-MM-YYYY
    #age_limit=18 #should be either 18 or 45 
    #preffered_vaccine=["COVAXIN","COVISHIELD"] #choose vaccine of your choice
    pin_code=[]
    preffered_date=""
    age_limit=0
    preffered_vaccine=[]
    pin_code=input("Please Enter Comma Seperated PinCodes: \n").split(",")
    pin_code = [int(i) for i in pin_code]
    preffered_date=input("Please Enter prefered Date in DD-MM-YYYY Format: \n")
    age_limit_temp=int(input("Please Choose your age limit \n Press 1 for 18+ \n Press 2 for 45+ \n"))
    if age_limit_temp==1:
       age_limit=18
    else:
        age_limit=45
    preffered_vaccine_temp=int(input("Please Choose Vaccine preference:\n Press 0 for No preference \n Press 1 for Covaxin \n Press 2 for COVISHIELD \n"))
    if preffered_vaccine_temp==1:
        preffered_vaccine=["COVAXIN",]
    elif preffered_vaccine_temp==2:
        preffered_vaccine=["COVISHIELD",]
    else:
        preffered_vaccine=["COVAXIN","COVISHIELD"]
    print("\n\n")
    return  pin_code,preffered_date,age_limit,preffered_vaccine
    

def print_data(pin_code,preffered_date,age_limit,preffered_vaccine):
    print(f"Scanning for pincode: {pin_code}"),
    print(f"Scanning for prefered_date: {preffered_date}")
    print(f"Scanning for Age Limit: {age_limit}+")
    print(f"Scanning for Preffered Vaccine {preffered_vaccine}")
    print("\n\n")

def app():
    pin_code,preffered_date,age_limit,preffered_vaccine=user_input()
    print_data(pin_code,preffered_date,age_limit,preffered_vaccine)
    while(True):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("@Time ", current_time)
    
        availabilty_list={}
        for pin in pin_code:
            lst=[]
            url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+str(pin)+"&date="+preffered_date
            from urllib.request import urlopen, Request
            headers = {'User-Agent': 'Chrome/41.0.2228.0'}
            req = Request(url, headers=headers) 
            html = str(urlopen(req).read())[2:-3]
            available=html[html.find(":")+2:]
            ava=available.split("{")[1:]
            for a in ava:
                if age_limit==(int(a[a.find("min_age_limit")+15:a.find("min_age_limit")+17])):
                    if len(preffered_vaccine)>0:
                        if ((a[a.find("vaccine")+10:].split('"')[0]).upper()) in preffered_vaccine:
                            lst.append(a[a.find("name")+7:].split('"')[0]+"---"+a[a.find("vaccine")+10:].split('"')[0])
                        else:
                            pass
                    else:
                        lst.append(a[a.find("name")+7:].split('"')[0]+"---"+a[a.find("vaccine")+10:])
                else:
                   pass
            availabilty_list[pin]=lst
        for key,values in availabilty_list.items():
            print(key,values)
            if len(values)>0:
                for i in range(2):
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        time.sleep(5)
        print()


if __name__ == "__main__":
        app()
