from django.shortcuts import render

from . models import bootstrap_wysihtml5_data

# Create your views here.


def bootstrap_wysihtml5_direct_validation(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        bootstrap_wysihtml5_data.objects.create(description=data)
        print('bootstrap_wysihtml5_direct_validation data saved successfully')

    return render(request, 'bootstrap_wysihtml5/1.0_bootstrap_wysihtml5_direct_validation.html')

def bootstrap_wysihtml5_validation_using_inputbox(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        bootstrap_wysihtml5_data.objects.create(description=data)
        print('bootstrap_wysihtml5_validation_using_inputbox data saved successfully')

    return render(request, 'bootstrap_wysihtml5/1.1_bootstrap_wysihtml5_validation_using_inputbox.html')