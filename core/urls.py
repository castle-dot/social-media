
from django.urls import path
from .views import index, signup, login, logout, settings


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name = 'signup'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('settings/', settings, name = 'settings'),
]