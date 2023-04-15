from django.shortcuts import render

# Create your views here.

from . models import ckeditor_data

# ckeditor5 - start -------------------------------------------------------------------------------------
# [Classic editor setup] -start
def classic_ckeditor5_direct_validation(request):

    # if request.method == 'GET':
    #     data = request.GET.get('description')
    #     print(data, 'get')
        
    if request.method == 'POST':
        data = request.POST.get('description')
        print(data, 'post')

        ckeditor_data.objects.create(discription=data)
        print('from saved in - 1.0_classic_ckeditor5_direct_validation')

    return render(request, 'ckeditor/ckeditor5/1.0_classic_ckeditor5_direct_validation.html')


def classic_ckeditor5_validation_using_inputbox(request):
        
    if request.method == 'POST':
        data = request.POST.get('description')
        print(data, 'post')

        ckeditor_data.objects.create(discription=data)
        print('from saved in - 1.1_classic_ckeditor5_validation_using_inputbox')

    return render(request, 'ckeditor/ckeditor5/1.1_classic_ckeditor5_validation_using_inputbox.html')



def custom_classic_ckeditor5_direct_validation(request):
        
    if request.method == 'POST':
        data = request.POST.get('description')
        print(data, 'post')

        ckeditor_data.objects.create(discription=data)
        print('from saved in - 1.2_custom_classic_ckeditor5_direct_validation')

    return render(request, 'ckeditor/ckeditor5/1.2_custom_classic_ckeditor5_direct_validation.html')

# [Classic editor setup] - end


# [super-build editor setup] - start
def full_ckeditor5_direct_validation(request):
     
    if request.method == 'POST':
        data = request.POST.get('description')
        print(data, 'post')

        ckeditor_data.objects.create(discription=data)
        print('from saved in - 2.0_full_ckeditor5_direct_validation')

    return render(request, 'ckeditor/ckeditor5/2.0_full_ckeditor5_direct_validation.html')

def full_ckeditor5_validation_using_inputbox(request):
     
    if request.method == 'POST':
        data = request.POST.get('description')
        print(data, 'post')

        ckeditor_data.objects.create(discription=data)
        print('from saved in - 2.1_full_ckeditor5_validation_using_inputbox')

    return render(request, 'ckeditor/ckeditor5/2.1_full_ckeditor5_validation_using_inputbox.html')
# [super-build editor setup] - end

# ckeditor5 - end -------------------------------------------------------------------------------------