from django.urls import path

from . views import *

urlpatterns = [

    path('basic_tinyMCE_direct_validation_without_api_key', basic_tinyMCE_direct_validation_without_api_key, name='basic_tinyMCE_direct_validation_without_api_key'),
    path('basic_tinyMCE_direct_validation_with_api_key', basic_tinyMCE_direct_validation_with_api_key, name='basic_tinyMCE_direct_validation_with_api_key'),
    path('custom_basic_tinyMCE_direct_validation_with_api_key', custom_basic_tinyMCE_direct_validation_with_api_key, name='custom_basic_tinyMCE_direct_validation_with_api_key'),
]