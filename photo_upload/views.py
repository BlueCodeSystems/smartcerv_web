from django.http import HttpResponse
from django.template import loader

from .models import SmartcervUpload


def index(request):
    template = loader.get_template('photo_upload/index.html')
    context = {
        'latest_question_list': 'test',
    }
    return HttpResponse(template.render(context, request))