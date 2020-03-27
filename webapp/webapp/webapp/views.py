from django.shortcuts import render 


def mainview(request):
    content={}
    return render(request,'index.html',content)