from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .maincode.finaloutput import outputfunction
from django.views.generic import CreateView,View,TemplateView
from .models import IMAGE
from .forms import ImageUploadForm
from django.urls import reverse_lazy
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def mainpage(request):
#     if request.method=='POST' and request.FILES['myfile']:
#         myfile=request.POST.get('myfile',False)
#         # output=mainfunction(myfile)
#         output="workings"
#         return render(request,'core/index.html',{'output':output})
#     return render(request,'core/index.html')



class ImageInputView(CreateView):
    model=IMAGE
    form_class=ImageUploadForm
    template_name='core/input.html'
    success_url=reverse_lazy('core:output')


class OutputView(View):
    def get(self,request):
        img=IMAGE.objects.order_by('-pk')[0]
        img_path=img.data.url

        img_patha=img_path
        #to get absolute file path
        img_path=BASE_DIR+img_path
        output_data=outputfunction(img_path)
        # data=json.loads(output_data)
        # labels=output_data[0]
        # readings=output_data[1]
        return render(request,'core/output.html',{
            'path':img_patha,
            'outputdata':output_data[0],
            'outputlatex':output_data[1]
            })



class testhtml(TemplateView):
    template_name='core/index.html'
