import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import os
import random


x_axis_dataset=[['yellow','blue','red','green'],
            ['Google','IBM','Facebook'],
            ['Jodhpur','Pune','Mumbai','Delhi'],
            ['Arpit','Raghav','Aditya','Tanuj','Akash'],
            ['Cake','Sandwich','Pizza','Burger','Chips','Chocolate'],
            ['Python','C++','Java','Ruby','C','Javascript','R'],
            ['Html','Css','Javascript'],
            ['Maharashtra','Rajasthan','UP','Kerala','Assam','MP'],
            ['Mi','Realme','Apple','Samsung'],
            ['Android','Iphone'],
            ['Dell','HP','Apple','Asus'],
            ['India','USA','UK','China']
            ]


color1=["red","#7f6d5f","pink"]
color2=["blue","green","#557f2d"]
color3=["#2d7f5e","brown","orange"]

#os.mkdir("horizontalstacked")

numberOfGraphs=4000


for i in range(numberOfGraphs):
    names=random.choice(x_axis_dataset)
    bars1=[]
    bars2=[]
    bars3=[]
     # The position of the bars on the x-axis
    r=[]

    for j in range(len(names)):
        bars1.append(random.randint(1,30))
        bars2.append(random.randint(1,30))
        bars3.append(random.randint(1,30))
        r.append(j)



  
    # Heights of bars1 + bars2
    bars = np.add(bars1, bars2).tolist()
 
   
    
 
    # Names of group and bar width


    # Create brown bars
    plt.barh(r, bars1, color=random.choice(color1))
    # Create green bars (middle), on top of the firs ones
    plt.barh(r, bars2, left=bars1, color=random.choice(color2))
    # Create green bars (top)
    plt.barh(r, bars3, left=bars, color=random.choice(color3))
 
    # Custom X axis
    plt.yticks(r,names)
    plt.xlabel("values")
    plt.ylabel('groups')
    k=str(i+1)
    var="hs"+k+".png"
    image_filepath=os.path.join("horizontalstacked/",var)
    # Show graphic
    plt.savefig(image_filepath)
    plt.cla()
 
    # Show graphic
    #plt.show()
