from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
 
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='profile_pics',blank=True)
    dob=models.DateField( null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    father_name=models.CharField(max_length=50,null=True,blank=True)
    mother_name=models.CharField(max_length=50,null=True,blank=True)
    place = models.CharField(max_length=100,null=True,blank=True)
    


 
    def __str__(self):
        return f'{self.user.username} Profile'