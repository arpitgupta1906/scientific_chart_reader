from django.urls import path
from .views import testhtml,ImageInputView,OutputView

urlpatterns = [
    path('',testhtml.as_view(),name='index'),    
]
