# Generated by Django 3.0.2 on 2020-01-30 03:26

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(max_length=200)),
                ('map_data', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(permissions=(gdstorage.storage.GoogleDriveFilePermission(gdstorage.storage.GoogleDrivePermissionRole['READER'], gdstorage.storage.GoogleDrivePermissionType['USER'], 'cycarulasan@gmail.com'),)), upload_to='maps')),
            ],
        ),
    ]
