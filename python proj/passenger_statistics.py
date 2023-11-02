import matplotlib.pyplot as plt 
import numpy as np 
import passenger_statistics
import administrator

#monthly statistis
def passengers_travelled_year():
    data={'Jan':1102,'Feb':690,'March':293,'Apr':670,'May':925,'Jun':834,'Jul':515,'Aug':690,'Sep': 1220,'Oct':1760,'Nov':1140,'Dec':2590} 
    months = list(data.keys()) 
    values=list(data.values())
    
    fig = plt.figure(figsize=(10,5))
    
    plt.bar(months,values,color='maroon',width=0.4) 

    plt.xlabel("Months") 
    plt.ylabel("Number of passengers") 
    plt.title("Passengers travelled in Year") 
    plt.show()

#flight class statistics
def passengers_travelled_class():
    data={'Economy':11002,'Business':4900}
    months = list(data.keys()) 
    values=list(data.values()) 

    fig = plt.figure(figsize=(10,5)) 

    plt.bar(months,values,color='blue',width=0.4) 

    plt.xlabel("Flight Class") 
    plt.ylabel("Number of passengers") 
    plt.title("Passengers travelled in Class")
    plt.show()


