from django.urls import path
from .  import views

urlpatterns = [
    path('register/', views.register),
    path('movies/', views.get_movies),
    path('collections/', views.collection_get_post),
    path('collections/<str:id>', views.collection_get_delete),
    
    
]