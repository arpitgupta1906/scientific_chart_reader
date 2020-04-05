import mainscript
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


    return output


def table_to_latex():
    text=r"""
    \documentclass{article}

    \begin{document}

    \begin{table}[h!]
    \begin{center}
        \caption{Your first table.}
        \label{tab:table1}
        \begin{tabular}{l|c|r} % <-- Alignments: 1st column left, 2nd middle and 3rd right, with vertical lines in between
        \textbf{Value 1} & \textbf{Value 2} & \textbf{Value 3}\\
        $\alpha$ & $\beta$ & $\gamma$ \\
        \hline
        1 & 1110.1 & a\\
        2 & 10.1 & b\\
        3 & 23.113231 & c\\
        \end{tabular}
    \end{center}
    \end{table}

    \end{document}
    """
    print(text)



if __name__=="__main__":
    # print(outputfunction('image2.png'))   
    table_to_latex()