from django.contrib import admin

from .models import SmartcervUpload


class SmartcervUploadAdmin(admin.ModelAdmin):
    list_filter = ['time_stamp']
    fields = ['title', 'upload']
    
    def save_model(self, request, obj, form, change):
        obj.save()
 
        for afile in request.FILES.getlist('photos_multiple'):
            obj.upload.create(image=afile)
    
admin.site.register(SmartcervUpload, SmartcervUploadAdmin)
