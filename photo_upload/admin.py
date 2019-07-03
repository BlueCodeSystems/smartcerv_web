from django.contrib import admin

from .models import SmartcervUpload
from .forms import SmartcervUploadForm


class SmartcervUploadAdmin(admin.ModelAdmin):
    list_filter = ['time_stamp']
    fields = ['title', 'upload']
    form = SmartcervUploadForm
    
    def save_model(self, request, obj, form, change):
        obj.save()
 
        for afile in request.FILES.getlist('photos_multiple'):
            obj.upload.create(image=afile)
    
admin.site.register(SmartcervUpload, SmartcervUploadAdmin)
