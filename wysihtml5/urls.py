from django.urls import path

from . views import *

urlpatterns = [ 

    path('wysihtml5_direct_validation', wysihtml5_direct_validation, name='wysihtml5_direct_validation'),
    path('wysihtml5_validation_using_inputbox', wysihtml5_validation_using_inputbox, name='wysihtml5_validation_using_inputbox'),
]