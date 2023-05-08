from django.urls import path

from . views import *

urlpatterns = [ 

    path('wysihtml5_direct_validation', wysihtml5_direct_validation, name='wysihtml5_direct_validation'),
]