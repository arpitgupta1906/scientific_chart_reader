from django.urls import path
from .views import testhtml,ImageInputView,OutputView

app_name='core'

urlpatterns = [
    path('',ImageInputView.as_view(),name='input'),
    path('output/',OutputView.as_view(),name='output'),
    path('base',testhtml.as_view(),name='index'),    
]
