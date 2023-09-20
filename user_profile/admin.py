from django.contrib import admin

# Register your models here.
from .models import Comments, Posts, Likes

admin.site.register(Comments)
admin.site.register(Posts)
admin.site.register(Likes)