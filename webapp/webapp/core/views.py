from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .maincode.mainscript import mainfunction
from django.views.generic import CreateView,View,TemplateView
from .models import IMAGE
from .forms import ImageUploadForm
from django.urls import reverse_lazy

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
    template_name='index.html'
    success_url=reverse_lazy('output')


class OutputView(View):
    def get(self,request):
        img=IMAGE.objects.order_by('-pk')[0]
        img_path=img.data.url
        output_data=mainfunction(img_path)
        labels=output_data[0]
        readings=output_data[1]
        return render(request,'output.html',{
            'path':img_path,
            'labels':labels,
            'readings':readings
            })



class testhtml(TemplateView):
    template_name='core/index.html'