import django
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("", views.MovieListView.as_view()),
    path("<int:pk>/",views.MovieDetailView.as_view()),
    path("genre/", views.GenreListView.as_view()),
    path("genre-add/", views.GenreCreateView.as_view()),
    path("genre/<int:pk>/", views.GenreDetailView.as_view()),
    path("review/",views.ReviewListView.as_view()),
    path("review-add/",views.ReviewCreateView.as_view()),
    path("review/<int:pk>/",views.ReviewDetailView.as_view()),
    path("actor/",views.ActorListView.as_view()),
    path("actor/<int:pk>/",views.ActorDetailView.as_view()),
    path("actor-add/",views.ActorCreateView.as_view()),
    path("category/", views.CategoryListView.as_view()),
    path("category/<slug:url>/", views.CategoryDetailView.as_view()),
    path("category-add/",views.CategoryCreateView.as_view()),
    path("rating/",views.RatingListView.as_view()),
    path("rating/<int:pk>/",views.RatingDetailView.as_view()),
    path("rating-add/",views.AddStarRatingView.as_view()),
]
