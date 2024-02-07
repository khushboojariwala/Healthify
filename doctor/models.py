from django.db import models
from django.utils import timezone
from master.models import BaseClass
from master.utils.generate_unique_id import custom_filename

class doctor(BaseClass):
    DIR_NAME = 'doctors-profile'
    FILENAME_WORD = 'dp'
    profile = models.ImageField(upload_to=custom_filename, default=r'default_images\doctor-profile.png')

    name = models.CharField(max_length= 255)
    degree = models.CharField(max_length=50)
    contact = models.CharField(max_length=255)
    total_patient = models.IntegerField(default=0)
    summary = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name
    