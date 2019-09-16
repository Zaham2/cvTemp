from django.db import models

class Job(models.Model):
    #upload_to  --> Where would you like the job object's image to be saved?

    # all files uploaded as part ofmdels are (generically) saved to the same directory... e.d will always be saved
    # to media root b default
    # BUT
    # You can define your own folders in that directory
    image = models.ImageField(upload_to='images/')
    desc = models.CharField(max_length=200)