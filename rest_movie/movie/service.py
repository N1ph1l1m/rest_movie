from django_filters import rest_framework as filters
from .models import *

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass



class MovieFilter(filters.FilterSet):
    genres = CharFilterInFilter(field_name='genres__url',lookup_expr='in') ## field_name='genres__name'поиск по полю name
    year = filters.RangeFilter() # RangeFilter диапозон значений

    class Meta:
        model = Movie
        fields = ['genres','year']