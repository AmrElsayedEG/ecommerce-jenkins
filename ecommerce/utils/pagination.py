from rest_framework.pagination import PageNumberPagination


class CategoryProductsPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 10
