from django.db import models

class SmartcervUpload(models.Model):
    title = models.TextField('image title', null=True)
    upload = models.FileField(upload_to = 'smartcerv_patient_pictures', verbose_name = 'choose image')
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if(self.title == None):
            self.title = 'patient'
        return self.title

