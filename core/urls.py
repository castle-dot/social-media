
from django.urls import path
from .views import index, profile, signup, login, logout, settings, upload, like_post


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name = 'signup'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('settings/', settings, name = 'settings'),
    path('upload/', upload, name = 'upload'),
    path('like/<uuid:id>/', like_post, name='like_post'),
    path('profile/<str:username>/', profile, name='profile'),
]