# Generated by Django 3.0.4 on 2020-05-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_jobtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='none', max_length=600),
        ),
        migrations.AddField(
            model_name='job',
            name='timepd',
            field=models.CharField(default='none', max_length=600),
        ),
    ]
