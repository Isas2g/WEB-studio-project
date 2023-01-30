from django_filters import rest_framework as filters
from .models import Projects
from rest_framework.pagination import PageNumberPagination


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter()

    class Meta:
        model = Projects
        fields = ['title']


class PaginationProjects(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PaginationProjectFeedback(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000
