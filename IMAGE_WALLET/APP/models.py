from django.db import models

# Create your models here.
class wallet(models.Model):
    uname=models.TextField()
    email=models.TextField()
    psw=models.TextField()

class File(models.Model):
    user=models.ForeignKey(wallet,on_delete=models.CASCADE)
    document=models.FileField()
    describe=models.TextField()