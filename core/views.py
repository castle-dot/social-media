from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.http import JsonResponse

from django.shortcuts import get_object_or_404

from .models import Post, Profile

@login_required(login_url='login')
def index(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=request.user)
    post_list = list(Post.objects.all().order_by('-created_at'))
    
    return render(
        request, 
        'index.html', 
        {
            'profile': profile,
            'posts': post_list
        }
    )
   
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
        # Must match name="image_upload" from your HTML input field
        image = request.FILES.get('image_upload')
        caption = request.POST.get('caption', '')

        if image:
            post = Post.objects.create(
                user=request.user,
                image=image,       # Saves the file data to your Post model's image field
                caption=caption
            )
            post.save()
            return redirect('index')

    # Bounces back safely if it's a GET request or missing a file
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

    user = get_object_or_404(User, username=username)

    profile = Profile.objects.get(user=user)

    posts = Post.objects.filter(user=user)

    context = {
        'profile_user': user,
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'profile.html', context)