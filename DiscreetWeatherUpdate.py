#The Libraries required to Run the program
from bs4 import BeatifulSoap
import urllib.request
import pandas as pd
from time import sleep
from datetime import datetime

#################################This Part is for Discreete Interval Scrapping####################################
def weather_discreete():
    temperature=[]
    url=urllib.request.urlopen(url)
    page=req.read()
    scrapping=BeautifulSoap(page)

    #Time Recording
    DateTime=datetime.now().strftime("%I:%M")
    DateTime=Datetime.replace("AM","")
    DateTime=Datetime.replace("PM","")
    temperature.append(DateTime)

    #Temperature
    Temperature=scraping.findAll("div",attrs={"class":"class-temp"})[0].text
    ct=Temperature.replace("\n\t\t\t\t","")
    ct=ct.replace("°","")
    temp=float(ct)
    temperature.append(temp)

    #WindSpeed
    WindSpeed=scraping.findAll("p",attrs={"class":"wind-spd"})[0].text
    ct=WindSpeed.replace("km/hr","")
    temp=float(ct)
    temperature.append(temp)

    #Humidity
    Relativehumidity=scraping.findAll("p")[8].text
    Relativehumidity=Relativehumidity.replace("%","")
    temperature.append(Relativehumidity)
    return temperature

print("Collection of temperature by Discreete Evaluation")
count=0
weatherdata= {'DataTime':[],'Temperature':[],'WindSpeed':[],'Humdity':[]}
while count<10:
    T= weather_discreete()
    oldtemp=-100
    currenttemp=T[1]
    if count!=0:
        oldtemp=weatherdata['Temperature'][count-1]
    currenttemp=T[1]
    if(currenttemp-oldtemp)<1:sleep(60); continue
    weatherdata['DateTime'].append(T[0])
    weatherdata['Temperature'].append(T[1])
    weatherdata['WindSpeed'].append(T[2])
    weatherdata['Humidity'].append(T[3])
    count +=1
    
data=pd.DataFrame(weatherdata)
data.to_csv(r'Regular-1.csv',index=False)
print('End of Test')

