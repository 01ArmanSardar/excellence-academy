from django.db import models
from ClassCtg.models import Category
from django.contrib.auth.models import User
# Create your models here.
# for user Uploaded file(2-6-24)
# def user_directory_path(instance, filename): 
  
#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

class Tution(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category)  # ekta post multiple categorir moddeh thakteh pare abar akta categorir moddeh multiple post takte pareh
    TutionApprove=models.BooleanField(default=False)
    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    # image=models.ImageField(upload_to='posts/media/uploads/',blank=True,null=True) #global media file holeh upload_to='uploads/',
    # upload = models.ImageField(upload_to = user_directory_path) 

    def __str__(self):
        return f'{self.title}'

class Application(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tution = models.ForeignKey(Tution,on_delete=models.CASCADE)
    applied_at=models.DateTimeField(auto_now_add=True)
    is_approved=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.tution.title}'