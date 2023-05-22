from django.shortcuts import render

from . models import trix_data


# Create your views here.


def trix_direct_validation(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        trix_data.objects.create(description=data)
        print('trix_direct_validation data saved successfully')

    return render(request, 'trix/1.0_trix_direct_validation.html')