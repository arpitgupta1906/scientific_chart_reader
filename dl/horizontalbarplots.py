# libraries
import numpy as np
import matplotlib.pyplot as plt
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

color1=["red","#7f6d5f","brown","blue","green","#2d7f5e","orange"]

os.mkdir("horizontalbarplots")
numberOfGraphs=4000



for i in range(numberOfGraphs):
    bars=random.choice(x_axis_dataset)
    height=[]
    colors=[]
    for j in range(len(bars)):
        height.append(random.randint(1,100))
        colors.append(random.choice(color1))

    
    # Make fake dataset

    y_pos = np.arange(len(bars))
 
    # Create horizontal bars
    plt.barh(y_pos, height,color=colors)
 
    # Create names on the y-axis
    plt.yticks(y_pos, bars)
 
    k=str(i+1)
    var="image"+k+".png"
    image_filepath=os.path.join("horizontalbarplots/",var)
    # Show graphic
    plt.savefig(image_filepath)
    plt.cla()

