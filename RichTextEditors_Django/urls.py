"""RichTextEditors_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings # for 'media' folder setting purpose
from django.conf.urls.static import static # for 'media' folder setting purpose

# from mainapp.views import index

# rendering a index page in main project folder
from django.shortcuts import render
def index(request):
	return render(request,'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'), # home url
    path('ckeditor/', include('ckeditor.urls'), name='ckeditor'), # ckeditor url
    path('summernote/', include('summernote.urls'), name='summernote'), # summernote url
    path('quill/', include('quill.urls'), name='quill' ), # quill url
    path('bootstrap_wysihtml5/', include('bootstrap_wysihtml5.urls'), name='bootstrap_wysihtml5' ), # bootstrap_wysihtml5 url
    path('tinyMCE/', include('tinyMCE.urls'), name='tinyMCE' ), # tinyMCE url
    path('trix/', include('trix.urls'), name='trix' ), # trix url

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # for 'media' folder setting purpose
