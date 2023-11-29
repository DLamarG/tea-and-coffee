from django.urls import path
from . import views

urlpatterns = [
path('coffee-likes/<int:coffee_id>/', views.CoffeeLikesNewAPIView.as_view(), name='add_like_to_coffee'),
]