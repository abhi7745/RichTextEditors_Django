from django.shortcuts import render

from . models import summernote_data

# Create your views here.


def summernote_direct_validation(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        summernote_data.objects.create(description=data)
        print('summernote data saved successfully')


    return render(request, 'summernote/1.0_summernote_direct_validation.html')