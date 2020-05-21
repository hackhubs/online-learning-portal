from django.urls import path

from users.views import Profile, RequestsView

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('request/', RequestsView, name='request')

]