from django.shortcuts import render
from VideoUpload.settings import MEDIA_ROOT
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def failed(request):
    return render(request, 'failed.html')

def upload(request):
    if request.method=='POST':
        file = request.FILES['file']
        file_name = file.name
        with open(MEDIA_ROOT + file_name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return HttpResponseRedirect('/success/')

    else:
        return HttpResponseRedirect('/failed/')



