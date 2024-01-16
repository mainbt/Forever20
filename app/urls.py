from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "image-search-result/<str:pk>",
        views.image_search_result,
        name="image-search-result",
    ),
    path("image-upload/", views.image_upload_view, name="image-upload"),
    path(
        "text-search-result",
        views.text_search_result,
        name="text-search-result",
    ),
]
