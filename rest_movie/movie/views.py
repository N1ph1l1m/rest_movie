from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.


class MovieListView(APIView):
    def get(self,request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializers(movies,many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    def get(self,request,pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)



class GenreListView(APIView):
    def get(self,request):
        genre = Genre.objects.all()
        serializer = GenreListSerializers(genre, many=True)
        return Response(serializer.data)


class ReviewListView(APIView):

    def post(self,request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


    def get(self,request):
        rewiew = Review.objects.all()
        serializers = ReviewCreateSerializer(rewiew, many = True)
        return Response(serializers.data)

class RevievDetail(APIView):
    def get(self,request,pk):
        rewiew = Review.objects.get(id = pk)
        serializer = ReviewDetailSerializer(rewiew,)
        return Response(serializer.data)
