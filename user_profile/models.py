from django.db import models
from django.core.validators import MinValueValidator

from authentication.models import User
# Create your models here.

class Posts(models.Model) :
    photo = models.FileField(upload_to='uploads/')
    caption = models.TextField(null =True, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)


    class Meta:
        verbose_name_plural = "Posts"


class Comments(models.Model) :
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name_plural ="Comments"


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    like_value= models.BooleanField(default= False)
    class Meta:
        verbose_name_plural = "Likes"

