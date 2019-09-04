from django.db import models

class Job(models.Model):
    #upload_to  --> Where would you like the job object's image to be saved?
    image = models.ImageField(upload_to='images/')
    desc = models.CharField(max_length=200)