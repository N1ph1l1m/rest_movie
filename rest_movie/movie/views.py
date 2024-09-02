from django.shortcuts import render
from rest_framework import status, generics,permissions
from rest_framework.response import  Response
from rest_framework.views import APIView
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .service import get_client_ip , MovieFilter

# Create your views here.


#generic
class MovieListView(generics.ListAPIView):
    serializer_class = MovieListSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
                        rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
                    ).annotate(
                    middle_star = models.Sum(models.F('ratings__star'))/ models.Count(models.F('ratings'))
                )
        return movies

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializers

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializers

class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializers

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer

class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorCreateView(generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'url'

class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer




class RatingListView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
class AddStarRatingView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer
    def perform_create(self, serializer):
        serializer  = self.serializer_class
        serializer.save(ip=get_client_ip(self.request))





# class AddStarRatingView(APIView):
#     def post(self,request):
#         serializer = CreateRatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(ip=get_client_ip(request))
#             return Response(status=200)
#         else:
#             return Response(status=400)





## простой способ


# class MovieListView(APIView):
#
#     def get(self,request):
#
#         movies = Movie.objects.filter(draft=False).annotate(
#                 rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(request)))
#             ).annotate(
#             middle_star = models.Sum(models.F('ratings__star'))/ models.Count(models.F('ratings'))
#         )
#         serializer = MovieListSerializers(movies,many=True)
#         return Response(serializer.data)



# class MovieDetailView(APIView):
#     def get(self,request,pk):
#         movie = Movie.objects.get(id=pk, draft=False)
#         serializer = MovieDetailSerializer(movie)
#         return Response(serializer.data)


# class GenreListView(APIView):
#     def get(self,request):
#         genre = Genre.objects.all()
#         serializer = GenreListSerializers(genre, many=True)
#         return Response(serializer.data)
#
#     def post(self,request,):
#         genre = GenreListSerializers(data= request.data)
#         if genre.is_valid():
#             genre.save()
#         return Response(status=201)


# class ReviewListView(APIView):
#
#     def post(self,request):
#         review = ReviewCreateSerializer(data=request.data, many=True)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)
#     def get(self,request):
#         review = Review.objects.all()
#         serializer = ReviewCreateSerializer(review, many = True)
#         return Response(serializer.data)


# class ReviewDetail(APIView):
#     def get(self,request,pk):
#         review = Review.objects.get(id = pk)
#         serializer = ReviewDetailSerializer(review,)
#         return Response(serializer.data)
#
#     def put(self, request, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT now allowed"})
#
#         try:
#             instance = Review.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not exist"})
#
#         serializer = ReviewDetailSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             instance = Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         instance.delete()
#         return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



# class ActorListView(APIView):
#
#     def get(self,request):
#         actor = Actor.objects.all()
#         serializer = ActorSerializer(actor,many = True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         actor = ActorSerializer(data=request.data,many=True)
#         if actor.is_valid():
#             actor.save()
#         return Response(status=201)


# class ActorDetailView(APIView):
#     def get(self, request, pk):
#         actor = Actor.objects.get(id=pk)
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data)
#
#     def put(self,request, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT now allowed"})
#
#         try:
#             instance = Actor.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not exist"})
#
#         serializer = ActorSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#
#     def delete(self, request, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             instance = Actor.objects.get(pk=pk)
#         except Actor.DoesNotExist:
#             return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         instance.delete()
#         return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# class CategoryListView(APIView):
#     def get(self,request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         category = CategorySerializer(data=request.data)
#         if category.is_valid():
#             category.save()
#         return Response(status=201)
#
#
# class CategoryDetailView(APIView):
#
#     def get(self,request,pk):
#         category = Category.objects.get(id=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     def put(self,request,**kwargs):
#         pk = kwargs.get("pk",None)
#         if not pk:
#             return Response({"error": "Method PUT now allowed"})
#
#         try:
#             instance = Category.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not exist"})
#
#         serializer = CategorySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#
#     def delete(self,request,**kwargs):
#         pk = kwargs.get("pk",None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             instance = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         instance.delete()
#         return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)