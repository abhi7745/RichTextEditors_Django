from django.urls import path

from . views import *

urlpatterns = [ 

    path('summernote_direct_validation', summernote_direct_validation, name='summernote_direct_validation'),
]