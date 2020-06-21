import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
color1=["red","yellow","pink"]
color2=["blue","green","brown"]
label1=["local","overseas","sale","profit"]
label2=["profit","loss","price","value"]

#os.mkdir("doublehorizontal")
fig, ax = plt.subplots()
numberOfGraphs=10

for i in range(numberOfGraphs):
    xx=random.choice(x_axis_dataset)
    bars1=[]
    bars2=[]
    # width of the bars
    
    for _ in range(len(xx)):
        bars1.append(random.randint(1,30))
        bars2.append(random.randint(1,30))

    df = pandas.DataFrame(dict(graph=xx,n=bars1, m=bars2)) 

    ind = np.arange(len(df))
    width = 0.4

    
    ax.barh(ind, df.n, width, color=random.choice(color1), label='N')
    ax.barh(ind + width, df.m, width, color=random.choice(color2), label='M')

    ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2*width - 1, len(df)])
    plt.ylabel('groups')
    plt.xlabel('values')
    ax.legend()
    k=str(i+1)
    var="hordoub"+k+".png"
    image_filepath=os.path.join("doublehorizontal/",var)
    # Show graphic
    plt.savefig(image_filepath)
    plt.cla()
