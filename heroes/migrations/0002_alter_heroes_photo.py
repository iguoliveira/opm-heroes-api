# Generated by Django 4.1 on 2022-08-26 01:51

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroes',
            name='photo',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='%y/%m/%d', variations={}),
        ),
    ]
