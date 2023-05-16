from django.shortcuts import render

from . models import tinyMCE_data

# Create your views here.


def basic_tinyMCE_direct_validation_without_api_key(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        tinyMCE_data.objects.create(description=data)
        print('basic_tinyMCE_direct_validation_without_api_key data saved successfully')

    return render(request, 'tinyMCE/1.0_basic_tinyMCE_direct_validation_without_api_key.html')