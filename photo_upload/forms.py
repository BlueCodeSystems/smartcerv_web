from django import forms
from photo_upload.models import SmartcervUpload

class SmartcervUploadForm(forms.ModelForm):
    
    upload = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        )
    )

    class Meta:
        model = SmartcervUpload
        fields = ['title']
