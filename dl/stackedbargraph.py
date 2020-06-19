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

os.mkdir("stackedbargraphs")

numberOfGraphs=500
plt.figure(figsize=(10,6))

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



    rc('font',weight="bold")
    # Heights of bars1 + bars2
    bars = np.add(bars1, bars2).tolist()
 
   
    
 
    # Names of group and bar width

    barWidth = 0.4
    # Create brown bars
    plt.bar(r, bars1, color=random.choice(color1), width=barWidth)
    # Create green bars (middle), on top of the firs ones
    plt.bar(r, bars2, bottom=bars1, color=random.choice(color2), width=barWidth)
    # Create green bars (top)
    plt.bar(r, bars3, bottom=bars, color=random.choice(color3), width=barWidth)
 
    # Custom X axis
    plt.xticks(r, names, fontweight='bold')
    plt.xlabel("groups")
    plt.ylabel('values')
    k=str(i+1)
    var="image"+k+".png"
    image_filepath=os.path.join("stackedbargraphs/",var)
    # Show graphic
    plt.savefig(image_filepath)
    plt.cla()
 
    # Show graphic
    #plt.show()
