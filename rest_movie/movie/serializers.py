from rest_framework import serializers
from .models import *
from .service import get_client_ip

class FilterReviewSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        fields = ("name","text","children")

class MovieListSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # actors = serializers.SlugRelatedField(slug_field='name',read_only=True,many=True)
    # directors = serializers.SlugRelatedField(slug_field='name',read_only=True,many=True)
    # genres = serializers.SlugRelatedField(slug_field='name',read_only=True,many=True)

    rating_user = serializers.BooleanField()
    middle_star =  serializers.IntegerField()
    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'category','rating_user', 'middle_star')
        # fields = '__all__'


class GenreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field="name", read_only=True)
    #movie = MovieDetailSerializer(read_only=True) передача всех данных таблицы movie
    movie = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

class CreateRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ("star","movie")

    def create(self, validated_data):
        rating,_ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            movie=validated_data.get('movie',None),
            defaults={'star': validated_data.get('star')}
        )
        return rating



class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only = True)
    actors = ActorSerializer( read_only = True, many=True)
    directors = ActorSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)


    class Meta:
        model = Movie
        exclude = ("draft",)## выражение exlude означет что мы берем все поля бд крое поля draft


