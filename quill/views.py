from django.shortcuts import render


from . models import quill_data
# Create your views here.


def quill_validation_using_inputbox(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        quill_data.objects.create(description=data)
        print('quill_validation_using_inputbox data saved successfully')


    return render(request, 'quill/1.0_quill_validation_using_inputbox.html')

def inline_quill_validation_using_inputbox(request):

    if request.method == 'POST':
        data = request.POST.get('description')
        print(data)

        quill_data.objects.create(description=data)
        print('inline_quill_validation_using_inputbox data saved successfully')


    return render(request, 'quill/1.1_inline_quill_validation_using_inputbox..html')