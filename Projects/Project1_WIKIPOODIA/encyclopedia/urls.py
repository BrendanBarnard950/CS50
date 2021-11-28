from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.article_view, name="article"),
    path("search/", views.search_view, name="search"),
    path("newpage", views.newpage_view, name="newpage")
]
