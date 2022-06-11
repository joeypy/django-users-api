from django.urls import path
from profiles_api.views import ProfileView

urlpatterns = [
    path('hello-view/', ProfileView.as_view())
]