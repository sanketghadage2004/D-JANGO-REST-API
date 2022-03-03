from django.urls import path
from . import views
urlpatterns = [
    path('blogs', views.BlogAPI.as_view()),
    path('blogs/<int:blog_id>', views.BlogAPI.as_view()),
    # path('login', views.UserAuthApi.as_view())
]

