from django.urls import path
from .views import BlogHome, BlogDetail

urlpatterns = [
    path("", BlogHome.as_view(), name="Blog Home"),
    path("/<int:pk>", BlogDetail.as_view(), name="article-detail"),
]
