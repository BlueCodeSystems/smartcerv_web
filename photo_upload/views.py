from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import FormView
from django.views.generic import ListView

from .forms import SmartcervUploadForm


def index(request):
    template = loader.get_template('photo_upload/index.html')
    context = {
        'latest_question_list': 'test',
    }
    return HttpResponse(template.render(context, request))

class SmartcervUploadView(FormView):
    form_class = SmartcervUploadForm
    template_name = 'photo_upload/change_form.html'
    success_url = 'photo_upload/change_form.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('upload')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

