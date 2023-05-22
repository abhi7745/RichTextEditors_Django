from django.urls import path

from . views import *

urlpatterns = [

    path('trix_direct_validation', trix_direct_validation, name='trix_direct_validation'),
    
]