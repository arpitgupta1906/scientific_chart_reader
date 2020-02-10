import pandas as pd 
pd.plotting.register_matplotlib_converters()
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




numberOfGraphs=1


for i in range(numberOfGraphs):
    plt.title("Title "+str(5))
    plt.figure(figsize=(10,6))
    plt.xlabel("countries")
    plt.ylabel("values")

    x=random.choice(x_axis_dataset)
    y=[]
    
    for _ in range(len(x)):
        y.append(random.randint(1,100))
    
    data={'X_axis':x,
            'Y_axis':y
            }

    df=pd.DataFrame(data)
    df.set_index('X_axis', inplace=True)

    k=str(i)
    var="data"+k

    
    

    u=sns.barplot(x=df.index,y=df['Y_axis'])
    u=u.get_figure()
    
    # plt.plot()
    plt.draw()
    # plt.show()

    var="image"+k+".png"
    image_filepath="testing.png"

    # var='table'+k+'.csv'
    # table_filepath=os.path.join(filepath,var)
    
    u.savefig(image_filepath)
    # df.to_csv(table_filepath)

    plt.cla()

    