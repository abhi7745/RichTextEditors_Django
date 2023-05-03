from django.shortcuts import render

from . models import summernote_data

# Create your views here.


def summernote_direct_validation(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        summernote_data.objects.create(description=data)
        print('summernote_direct_validation data saved successfully')


    return render(request, 'summernote/1.0_summernote_direct_validation.html')

def summernote_validation_using_inputbox(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        summernote_data.objects.create(description=data)
        print('summernote_validation_using_inputbox data saved successfully')


    return render(request, 'summernote/1.1_summernote_validation_using_inputbox.html')

def custom_summernote_direct_validation(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        summernote_data.objects.create(description=data)
        print('custom_summernote_direct_validation data saved successfully')


    return render(request, 'summernote/1.2_custom_summernote_direct_validation.html')

def custom_summernote_validation_using_inputbox(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        summernote_data.objects.create(description=data)
        print('custom_summernote_validation_using_inputbox data saved successfully')


    return render(request, 'summernote/1.3_custom_summernote_validation_using_inputbox.html')