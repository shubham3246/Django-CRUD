from django.urls import path
from app.views import *
urlpatterns = [  
    path('get/', EventGetRecentView.as_view()), 
    path('get/<int:pk>/', EventGetView.as_view()),
    path('create/', EventCreateView.as_view()),
    path('update/<int:pk>/', EventUpdateView.as_view()),
    path('delete/<int:pk>/', EventDeleteView.as_view()),
]  
