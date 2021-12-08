from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('authorlist/', AuthorList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('search/', Search.as_view()),
    path('add/', Add.as_view(), name='add'),
    path('<int:pk>/edit/', Edit.as_view(), name='edit'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete'),
]