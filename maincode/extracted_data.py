import textdetector
# import json


def extractdata(image_path):
    """
    Takes normal image path as input and returns the extracted data
    and the range ratio
    """
    text1,text2=textdetector.graphtextdetextor(image_path)
    data1=text1.strip().split('\n')
    data2=text2.strip().split('\n')
    
    # print(data1)
    
    y_axis_title=data2[0]
    y_axis_list=[]
    k=[]



    for i in data1:
        for d in i.split(" "):
            # try:
            #     float(d)
            #     y_axis_list.append(d)
            # except:
            #     k.append(d)
            if d.isdigit():
                y_axis_list.append(d)
            else:
                k.append(d)

    # print(y_axis_list)
    if y_axis_list[-1]!=0:
        y_axis_list.append(0)

    x_axis_title=data2[-1]
    k=k[1:-1]

    graph_title=data1[0]
    # data_titles=k[-1].strip().split(' ')

    diff=[]

    for i in range(len(y_axis_list)-1):
        diff.append(int(y_axis_list[i])-int(y_axis_list[i+1]))

    freq={}
    for i in diff:
        freq[i]=diff.count(i)

    max=0
    maxnumber=0

    for key,value in freq.items():
        if value>max:
            max=value
            maxnumber=key

    ydata=[]
    i=0

    print(freq)

    while True:
        o=int(y_axis_list[0])-i*maxnumber
        if o>0:
            ydata.append(o)
        else:
            ydata.append(0)
        if o<=0:
            break
        i=i+1


    if graph_title==str(ydata[0]):
        graph_title=""

    data_dictionary={
        "Graph_title":graph_title,
        "Yaxis_title":y_axis_title,
        "Xaxis_title":x_axis_title,
        "Yaxis_plotdata":ydata,
        "Data_titles":" "
    }

    # print("Graph Title: ",graph_title)
    # print("Y Axis title: ",y_axis_title)
    # print("X Axis title: ",x_axis_title)
    # print("Y axis plot list: ",ydata)
    # print("Data titles: ",data_titles)

    # print(data_dictionary)
    return [data_dictionary,maxnumber]

    # with open('person.txt','w') as json_file:
    # json.dump(data_dictionary,json_file)




if __name__=='__main__':
    image_path='7.jpg'
    a=extractdata(image_path)
    print(a)