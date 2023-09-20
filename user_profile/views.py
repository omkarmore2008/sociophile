# importing libraries
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from authentication.models import User
from django.db.models.signals import pre_delete,post_delete
from django.dispatch import receiver
# importing models
from user_profile.models import Posts, Comments, Likes

@login_required
def dashboard(request) :
     post = Posts.objects.all().order_by("-id")
     return render(request, 'user_profile/dashboard.html',{
                        "post" : post})
 

@login_required
def profile(request):
    """
        Profile Page View 
    """
    data = Posts.objects.filter(user = request.user).order_by("-id")
    return render(request, 'user_profile/profile.html',{
                        "post" : data
    })
 

@login_required
def photo_post(request) :
    """
        function to upload posts
    """
    if request.method == 'POST' :
        if request.user.is_authenticated :
            photo= request.FILES['photo']
            caption = request.POST.get('caption')
            user_posted = request.user
            posts = Posts.objects.create(photo = photo, caption = caption, user = user_posted)
            posts.save()

            return redirect('profile')
        
    return redirect('profile')


@login_required
def comment_post(request, id) :
    """
        function to add comment on post
    """   
    if request.method == 'POST' :
        if request.user.is_authenticated :
            user_commented = request.user
            post = Posts.objects.get(id=id) 
            comment = request.POST['comment']
            Comments.objects.create(post=post, user = user_commented, comment = comment)
            return redirect('dashboard')
        
    return redirect('dashboard')
   
@login_required 
def show_individual(request, id) :
    """
        function to view each post individually
    """
    post_data = Posts.objects.filter(id = id).first()
    return render(request, 'user_profile/show_individual.html',{
                        "post" : post_data })


@login_required
def delete_post(request,id):
    post = Posts.objects.filter(id=id).first()
    if request.user == post.user:
        if post:
            post.delete()
            return redirect("profile")
        else:
            return HttpResponse("No post found")
    return HttpResponse("Unauthorised user")


@login_required
def edit_profile(request,id):
    if request.method == 'POST':
        user = User.objects.filter(id=id).first()
        if request.user == user:
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.mobile_number = request.POST.get('mobile_number')
            user.bio = request.POST.get('bio')
            user.location = request.POST.get('location')
            
            user.save()
            return redirect('profile')
        else:
            return HttpResponse("You are not authorised to edit information!")
    return redirect('profile')

