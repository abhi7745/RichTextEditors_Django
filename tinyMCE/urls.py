from django.urls import path

from . views import *

urlpatterns = [

    path('basic_tinyMCE_direct_validation_without_api_key', basic_tinyMCE_direct_validation_without_api_key, name='basic_tinyMCE_direct_validation_without_api_key'),
]