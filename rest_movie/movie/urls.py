import django
from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'movie', views.MovieViewSet, basename='movie')
router.register(r'genre',views.GenreViewSet,basename='genre')
router.register(r'review',views.ReviewViewSet,basename='review')
router.register(r'actor',views.ActorViewSet,basename='actor')
router.register(r'category',views.CategoryViewSet,basename='category')
router.register(r'rating',views.RatingViewSet,basename='rating')


rout = routers.SimpleRouter()
rout.register(r'review',views.GenreViewSet,basename="rev")

urlpatterns = [
    path('', include(router.urls)),
    path("rating-add/",views.AddStarRatingView.as_view()),
]
