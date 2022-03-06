import random
import string
from datetime import datetime
from django.shortcuts import render
from core.models import File
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .tasks import delete_File
import os


def generate_hash():
        hashCode = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
        print(File.objects)
        # if hash in File.objects :
        #     generate_hash()
        return hashCode


# Create your views here.
def index(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('file')
        if uploaded_file.size <= 1024**3 :
            file = File(name=uploaded_file.name, file=uploaded_file, hashCode = generate_hash())
            file.save()
            return JsonResponse({'filelink': reverse('download_file', args=(file.hashCode,)), 'response' : "True", "filename": uploaded_file.name })
        else:
            return JsonResponse({"error" : "File is larger than the expected size"})
    return render(request, 'index.html')


def download_file(request, hashCode):
    try:
        file = File.objects.get(hashCode = hashCode)
        context = {"filelink" : file.file.url, "filename" : file.file.name, "filesize" : round(os.path.getsize(file.file.path)/2**20,2) }
        return render(request, 'download.html', context)
    except:
        return render(request, '404.html' )