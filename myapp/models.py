from django.db import models

# Create your models here.

from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()



from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "cycarulasan@gmail.com"
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))

class Map(models.Model):
    map_name = models.CharField(max_length=200)
    map_data = models.FileField(upload_to='maps', storage=gd_storage)