from django.shortcuts import render
from rest_framework import status
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

    def post(self,request,):
        genre = GenreListSerializers(data= request.data)
        if genre.is_valid():
            genre.save()
        return Response(status=201)

class ReviewListView(APIView):

    def post(self,request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)
    def get(self,request):
        review = Review.objects.all()
        serializer = ReviewCreateSerializer(review, many = True)
        return Response(serializer.data)

class ReviewDetail(APIView):
    def get(self,request,pk):
        review = Review.objects.get(id = pk)
        serializer = ReviewDetailSerializer(review,)
        return Response(serializer.data)


class ActorListView(APIView):

    def get(self,request):
        actor = Actor.objects.all()
        serializer = ActorSerializer(actor,many = True)
        return Response(serializer.data)

    def post(self,request):
        actor = ActorSerializer(data=request.data)
        if actor.is_valid():
            actor.save()
        return Response(status=201)


class ActorDetailView(APIView):
    def get(self, request, pk):
        actor = Actor.objects.get(id=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def put(self,request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT now allowed"})

        try:
            instance = Actor.objects.get(pk=pk)
        except:
            return Response({"error": "object does not exist"})

        serializer = ActorSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})

    def delete(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data)

    def post(self,request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
        return Response(status=201)


class CategoryDetailView(APIView):

    def get(self,request,pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    def put(self,request,**kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response({"error": "Method PUT now allowed"})

        try:
            instance = Category.objects.get(pk=pk)
        except:
            return Response({"error": "object does not exist"})

        serializer = CategorySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})

    def delete(self,request,**kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


