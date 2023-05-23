from django.urls import path

from . views import *

urlpatterns = [

    path('trix_validation_using_inputbox', trix_validation_using_inputbox, name='trix_validation_using_inputbox'),
    
]