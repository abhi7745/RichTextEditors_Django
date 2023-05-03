from django.urls import path

from . views import *

urlpatterns = [ 

    path('summernote_direct_validation', summernote_direct_validation, name='summernote_direct_validation'),
    path('summernote_validation_using_inputbox', summernote_validation_using_inputbox, name='summernote_validation_using_inputbox'),
    path('custom_summernote_direct_validation', custom_summernote_direct_validation, name='custom_summernote_direct_validation'),
    path('custom_summernote_validation_using_inputbox', custom_summernote_validation_using_inputbox, name='custom_summernote_validation_using_inputbox'),
]