# Generated by Django 2.2.4 on 2019-09-02 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='img',
            new_name='image',
        ),
    ]