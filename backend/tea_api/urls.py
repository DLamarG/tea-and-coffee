from django.urls import path

from tea_api.views import TeaListView

urlpatterns = [

path('', TeaListView.as_view()),

]