from django.urls import path
from . import views



urlpatterns = [
    # UserProfiles
    path('user_profiles/', views.UserProfileCreateView.as_view()),
    # path('user_profile/<int:pk>/',views.UserProfileDetail .as_view()),
]
