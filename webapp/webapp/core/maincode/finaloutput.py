from . import mainscript
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

if __name__=="__main__":
    print(outputfunction('image2.png'))