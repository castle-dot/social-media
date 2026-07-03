from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.http import JsonResponse

from django.shortcuts import get_object_or_404

from .models import FollowersCount, Post, Profile

@login_required(login_url='login')
def index(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=request.user)
    post_list = list(Post.objects.all().order_by('-created_at'))
    suggestions = Profile.objects.exclude(user=request.user)[:5]
    
    # Pack all data into ONE context dictionary
    context = {
        'profile': profile,
        'posts': post_list,
        'suggestions': suggestions,
    }
    
    # Use the context variable here
    return render(request, 'index.html', context)
   
def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()


            # create profile
            Profile.objects.create(
                user=user
            )


            # automatically login
            auth_login(request, user)


            # send to settings
            return redirect('settings')


    else:

        form = UserCreationForm()


    return render(
        request,
        'signup.html',
        {'form':form}
    )


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    return redirect('login')



@login_required(login_url='login')
def settings(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":

        profile.bio = request.POST['bio']


        if request.FILES.get('image'):
            profile.profileimg = request.FILES['image']


        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']

        request.user.save()
        profile.save()


        return redirect('settings')


    return render(
        request,
        'setting.html',
        {
            'profile':profile
        }
    )

@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image_upload')
        video = request.FILES.get('video_upload') 
        caption = request.POST.get('caption', '')

        # Create the post
        new_post = Post.objects.create(user=request.user, caption=caption)
        
        if image:
            new_post.image = image
        if video:
            new_post.video = video
            
        new_post.save()
        return redirect('index')
    return redirect('index')


@login_required(login_url='login')
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Toggle the like
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    # Return JSON instead of redirecting
    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes.count()
    })

@login_required(login_url='login')
def profile(request, username):
    user_object = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user_object)
    posts = Post.objects.filter(user=user_object)
    
    # Count logic
    user_followers = FollowersCount.objects.filter(user=username).count()
    user_following = FollowersCount.objects.filter(follower=username).count()
    
    # Button logic
    if FollowersCount.objects.filter(follower=request.user.username, user=username).exists():
        button_text = 'Following' # Changed from Unfollow to Following
    else:
        button_text = 'Follow'

    context = {
        'profile_user': user_object,
        'profile': profile,
        'posts': posts,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }

    return render(request, 'profile.html', context)

@login_required(login_url='login')
def follow(request):
    if request.method == 'POST':
        user_following = request.POST['user'] 
        user_follower = request.user.username 
        
       
        if user_following == user_follower:
            return redirect('/profile/'+user_following)
            
        # Toggle Logic
        check_follow = FollowersCount.objects.filter(follower=user_follower, user=user_following)
        if check_follow.exists():
            check_follow.delete()
        else:
            FollowersCount.objects.create(follower=user_follower, user=user_following).save()
            
        return redirect('/profile/'+user_following)

def search_ajax(request):
    query = request.GET.get('q', '')
    users = User.objects.filter(username__icontains=query)[:5] 
    results = [{'username': u.username} for u in users]
    return JsonResponse({'results': results})