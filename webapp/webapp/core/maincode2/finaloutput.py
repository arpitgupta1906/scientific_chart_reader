from  . import mainscript
import json


class CustomType:
    def __init__(self, title, text):
        self.key = title
        self.value = text

    def toJSON(self):
        '''
        Serialize the object custom object
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

def outputjson(img_path):
    result=mainscript.mainfunction(img_path)
    datatitles=result[0]
    values=result[1]
    
    output=[]
    
    for i in range(len(datatitles)):
        obj=CustomType(datatitles[i],values[i])
        output.append(json.loads(obj.toJSON()))
    
    output=json.dumps(output)
    # print(output)

    return output


def outputfunction(img_path):
    result=mainscript.mainfunction(img_path)
    datatitles=result[0]
    values=result[1]
    output=dict()

    for i in range(len(datatitles)):
        output[datatitles[i]]=values[i]

    output_latex=table_to_latex(output)

    return [output,output_latex]


def table_to_latex(output):
    text_initial="""
    \\documentclass{article} 

    \\begin{document} 

    \\begin{table}[h!] 
    \\begin{center} 

    \\begin{tabular}{l|c|r}  
    \\textbf{X-axis titles} & \\textbf{Values}\\\\  
    \\hline  
        """

    text_middle=""
    for key,value in output.items():
         value_text= str(key)+" & "+str(value)+" \\\\ \n"
         text_middle=text_middle+"\t"+value_text

    text_last="""
    \\end{tabular} 
    \\end{center} 
    \\end{table} 

    \\end{document} 
        """

    output_text=text_initial+text_middle+text_last

    return output_text
    
    # print(output_text)



if __name__=="__main__":
    print(outputfunction('image2.png'))   
    # table_to_latex()