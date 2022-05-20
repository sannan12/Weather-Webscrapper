
#The Libraries required to Run the program
from bs4 import BeautifulSoap
import urllib.request
import pandas as pd
from time import sleep
from datetime import datetime

#################################This Part is for Regular Interval Scrapping####################################
#Time recording inside the weather interval function
def weather_interval():
    temperature=[]
    url="http://m.bom.gov.au/vic/melbourne/"
    req=urllib.request.urlopen(url)
    page=req.read()
    scrapping = BeatifulSoap(page)
    #Time Recording
    DateTime=datetime.now().strftime("%I:%M")
    DateTime=DateTime.replace("AM","")
    DateTime=DateTime.replace("PM","")
    #Recording the Current Temperature from the Website 
    tempraturea.append(DateTime)
    Temperature = scrapping.findAll("div",attrs={"class":"current-temp"})[0].text
    ct=Temperature.replace("\n\t\t\t\t","")
    ct=ct.replace("°","")
    temp=float(ct)
    temperature.append(temp)
    #Recording the Wind Speed
    WindSpeed=scraping.findAll("p",attrs={"class":"wind-spd"})[0].text
    ct=WindSpeed.replace("km/h","")
    temp=float(ct)
    temperature.append(temp)

    #Recording the Humidity
    Relativehumidity=scraping.findAll("p")[8].text
    Relativehumidity=Relativehumidity.replace("%","")
    temperature.append(Relativehumidity)
    return temperature

print("Collection of temperature by Regular Interval Evaluation")
count = 0
weatherdata= {'DataTime':[],'Temperature':[],'WindSpeed':[],'Humidity'[]}
while count <10:
    T= weather_Interval()
    weatherdata['DateTime'].append(T[0])
    weatherdata['Temperature'].append(T[1])
    weatherdata['WindSpeed'].append(T[2])
    weatherdata['Humidity'].append(T[3])

    count +=1
    print(weatherdata)
    sleep(1200)
    data=pd.DataFrame(weatherdata)

data.to_csv(r'Regular-1.csv',index=False)
print('End of Test')

