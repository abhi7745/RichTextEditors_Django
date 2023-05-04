from django.urls import path

from . views import *

urlpatterns = [ 

    path('quill_validation_using_inputbox', quill_validation_using_inputbox, name='quill_validation_using_inputbox'),
    
]