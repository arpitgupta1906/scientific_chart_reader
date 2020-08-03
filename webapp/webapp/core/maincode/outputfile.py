from .vertical_mixed import mainvalue_vmixed
from vertical_stack import mainvalue_vstack
from horizontal_mixed import mainvalue_hmixed
from horizontal_stack import mainvalue_hstack
from deep_learning_predictor import classifier


def classify(img_path):
    """
    A deep learning classifier to classify the type of graph
    """    
    return classifier(img_path)
    # return 1

def outputfunction(img_path):
    """
    returns the readings of the bar graph 
    """

    graph_id=classify(img_path)
    # graph_id=0

    result=[]

    #if it is a single or mixed vertical bar graph

    if graph_id==2:
        result=mainvalue_vmixed.mainfunction(img_path)

    #if it is a stacked vertical bar graph

    elif graph_id==0:
        result=mainvalue_vstack.mainfunction(img_path)

    #if it is a single or mixed horizontal bar graph

    elif graph_id==3:
        result=mainvalue_hmixed.mainfunction(img_path)

    #if it is a stacked horizontal bar graph

    elif graph_id==1:
        result=mainvalue_hstack.mainfunction(img_path)

    datatitles=result[0]
    values=result[1]
    output=dict()
    
    for i in range(len(datatitles)):
        output[datatitles[i]]=values[i]

    output_latex=table_to_latex(output,len(values[0]))

    return [output,output_latex,len(values[0])]

def table_to_latex(output,columns):
    text_initial="""
    \\documentclass{article} \n

    \\begin{document} \n

    \\begin{table}[h!] \n
    \\begin{center} \n

    \\begin{tabular}{l|c|r}  \n
        """

    d="""\\textbf{X-axis titles}"""

    if columns==1:
        d="""\\textbf{X-axis titles} & \\textbf{Values}\\\\  \n"""
    else:
        l=""
        for i in range(1,columns+1):
            l+="& \\textbf{value "+str(i)+"}"
        l+="\\\\ \n"

        d+=l
    d+="\\hline  \n"

    text_initial+=d

    text_middle=""

    for key in output:
        value_text="    "+str(key)
        for i in range(len(output[key])):
            value_text+=" & "+str(output[key][i])
        value_text+=" \\\\ \n"

        text_middle+=value_text

    text_last="""
        \\end{tabular} \n
        \\end{center} \n
        \\end{table} \n

        \\end{document} \n
        """

    output_text=text_initial+text_middle+text_last

    return output_text


if __name__ == "__main__":
    # print(table_to_latex({"first":[1,2],"second":[2,3]},2))
    print(outputfunction('image1.png'))
    print("works")