from django.forms import ModelForm
from photo_upload.models import SmartcervUpload

class UploadFileForm(ModelForm):
    class Meta:
        model = SmartcervUpload
        fields = '__all__'
