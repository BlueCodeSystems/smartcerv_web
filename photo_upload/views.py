from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import SmartcervUpload

from .forms import UploadFileForm


def index(request):
    template = loader.get_template('photo_upload/index.html')
    context = {
        'latest_question_list': 'test',
    }
    return HttpResponse(template.render(context, request))

def get_photo(request):
    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST)

        if form.is_valid():
            pass    # stub
            return HttpResponseRedirect('/thanks/')
    else:
        upload_form = UploadFileForm()
    
    context = {
        'upload_form': upload_form
    }

    return render(request, 'photo_upload/photo_request.html', context)