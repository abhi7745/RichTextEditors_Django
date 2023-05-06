from django.urls import path

from . views import *

urlpatterns = [ 

    path('quill_validation_using_inputbox', quill_validation_using_inputbox, name='quill_validation_using_inputbox'),
    path('inline_quill_validation_using_inputbox', inline_quill_validation_using_inputbox, name='inline_quill_validation_using_inputbox'),
    path('custom_quill_validation_using_inputbox', custom_quill_validation_using_inputbox, name='custom_quill_validation_using_inputbox'),
    
]