from django.urls import path

from . views import *

urlpatterns = [
   
    path('classic_ckeditor_ckeditor5_direct_validation', classic_ckeditor_ckeditor5_direct_validation, name='classic_ckeditor_ckeditor5_direct_validation'),
    path('classic_ckeditor_ckeditor5_validation_using_inputbox', classic_ckeditor_ckeditor5_validation_using_inputbox, name='classic_ckeditor_ckeditor5_validation_using_inputbox'),
    path('custom_classic_ckeditor5_direct_validation', custom_classic_ckeditor5_direct_validation, name='custom_classic_ckeditor5_direct_validation')

]