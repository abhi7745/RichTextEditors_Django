from django.shortcuts import render

from . models import wysihtml5_data

# Create your views here.


def wysihtml5_direct_validation(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        wysihtml5_data.objects.create(description=data)
        print('wysihtml5_direct_validation data saved successfully')

    return render(request, 'wysihtml5/1.0_wysihtml5_direct_validation.html')