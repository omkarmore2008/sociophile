from django.db.models.signals import pre_delete,post_delete
from django.dispatch import receiver
from django.http import HttpResponse

from .models import Posts
@receiver(pre_delete,sender=Posts)
def pre_delete_message(sender, **kwargs):
    print("you are about to delete post")

@receiver(post_delete,sender=Posts)
def pre_delete_message(sender, **kwargs):
    print("Post deleted successfully")
