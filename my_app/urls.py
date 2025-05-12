from django.urls import path
from .views  import first_views, second_views

urlpatterns = [
    path("", first_views, name="first page"),
    path("second/", second_views, name="second page"),
]


