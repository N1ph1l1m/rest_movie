import django
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("movie/", views.MovieListView.as_view()),
    path("movie/<int:pk>/",views.MovieDetailView.as_view()),
    path("genre/", views.GenreListView.as_view()),
    path("review/",views.ReviewListView.as_view()),
    path("review/<int:pk>/",views.RevievDetail.as_view()),



]
