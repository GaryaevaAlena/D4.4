from django_filters import FilterSet, CharFilter, DateFromToRangeFilter
from .models import *


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'title':['icontains'],
            'dateCreation':['gt'],
            'author':['exact'],
        }