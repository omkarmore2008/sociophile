from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name = 'dashboard'),
    path("profile", views.profile, name = 'profile'),
    path("post", views.photo_post, name = 'post'),
    path("comment/<int:id>", views.comment_post, name = 'comment'),
    path("show-individual/<int:id>", views.show_individual, name= 'show-individual'),
    path("delete-post/<int:id>", views.delete_post, name="delete-post"),
    path("edit-profile/<int:id>", views.edit_profile, name="edit-profile"),  
    
]