################################################For Predicting the data##################################
import pandas as pd
import numpy as np

def CompTime(a,b):
    flag=0
    time1=int(a.split(':')[0])*60 +int(a.split(':')[1])
    time2=int(b.split(':')[0])*60 +int(a.split(':')[1])
    if time1==time2: return 0
    elif time1 <time2: return 1
    else: return 2

if __name__=='__main__':
    data=pd.read_csv(r'D:\Datafusion.csv')
    while True:
        print('Please enter the time of weather')
        query= input('')
        time=data['DateTime']
        lowbound=-1
        upbound=-1
        key=-1

        for idx in range(len(time)):
            if compTime(time[idx],query)==1:lowbound=idx
            elif compTime(time[idx],query)==0:key=idx;break
        if key !=-1 : print(data['Temperature'][key])
        elif lowbound!=-1 and upbound!=-1: print(round(np.mean([float(data['Temperature'][lowbound]),float(data['Temperate'][upbound])])))
        elif lowbound==-1: print(data['Temperature'][upbound])
        else: print(data['Temperature'][lowbound])
    print('End of Test')