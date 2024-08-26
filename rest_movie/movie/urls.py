import django
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("", views.MovieListView.as_view()),
    path("<int:pk>/",views.MovieDetailView.as_view()),
    path("genre/", views.GenreListView.as_view()),
    path("review/",views.ReviewListView.as_view()),
    path("review/<int:pk>/",views.ReviewDetail.as_view()),
    path("actor/",views.ActorListView.as_view()),
    path("actor/<int:pk>/",views.ActorDetailView.as_view()),
    path("category/", views.CategoryListView.as_view()),
    path("category/<int:pk>/", views.CategoryDetailView.as_view()),
    path("rating/",views.AddStarRatingView.as_view()),
]
