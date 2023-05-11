from django.urls import path

from . views import *

urlpatterns = [ 

    path('bootstrap_wysihtml5_direct_validation', bootstrap_wysihtml5_direct_validation, name='bootstrap_wysihtml5_direct_validation'),
    path('bootstrap_wysihtml5_validation_using_inputbox', bootstrap_wysihtml5_validation_using_inputbox, name='bootstrap_wysihtml5_validation_using_inputbox'),
]