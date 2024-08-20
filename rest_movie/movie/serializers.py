from rest_framework import serializers
from .models import *


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'category','description')


class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only = True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only = True, many=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewCreateSerializer(many=True)



    class Meta:
        model = Movie
        exclude = ("draft",)## выражение exlude означет что мы берем все поля бд крое поля draft


class GenreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'description',)


class ReviewDetailSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field="name", read_only=True)
    #movie = MovieDetailSerializer(read_only=True) передача всех данных таблицы movie
    movie = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


