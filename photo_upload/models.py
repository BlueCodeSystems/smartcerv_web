from django.db import models

class SmartcervUpload(models.Model):
    upload = models.FileField(upload_to = 'smartcerv_patient_pictures', verbose_name = 'choose image')
