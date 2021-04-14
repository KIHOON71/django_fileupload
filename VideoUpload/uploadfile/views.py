from django.shortcuts import render
from VideoUpload.settings import MEDIA_ROOT
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def welcome(request):
    return render(request, 'home.html')

@csrf_exempt
def upload(request):
    print('connected')
    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid:
            file = request.FILES['file']
            file_name = file.name
            with open(settings.MEDIA_ROOT + file_name , 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return HttpResponseRedirect('/success/')

    else:
        return HttpResponseRedirect('/failed/')

def success(request):
    return render(request, 'success.html')

def failed(request):
    return render(request, 'failed.html')