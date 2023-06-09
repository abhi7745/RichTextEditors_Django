from django.urls import path

from . views import *

urlpatterns = [
   
    # classic editor
    path('classic_ckeditor5_direct_validation', classic_ckeditor5_direct_validation, name='classic_ckeditor5_direct_validation'),
    path('classic_ckeditor5_validation_using_inputbox', classic_ckeditor5_validation_using_inputbox, name='classic_ckeditor5_validation_using_inputbox'),
    path('custom_classic_ckeditor5_direct_validation', custom_classic_ckeditor5_direct_validation, name='custom_classic_ckeditor5_direct_validation'),
    # classic editor

    # super-build editor
    path('full_ckeditor5_direct_validation', full_ckeditor5_direct_validation, name='full_ckeditor5_direct_validation'),
    path('full_ckeditor5_validation_using_inputbox', full_ckeditor5_validation_using_inputbox, name='full_ckeditor5_validation_using_inputbox'),
    # super-build editor

]