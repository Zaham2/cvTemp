from django.contrib import admin


# If you want the model to show up in the admin page...
# add it here

from .models import Job

admin.site.register(Job)


