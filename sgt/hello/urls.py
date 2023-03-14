from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("greet", views.greet, name="greet"),
    # path("<str:nome>", views.greeting, name="greeting"),
    # path("<str:pessoa>", views.greet, name="greet"),
    path("<str:sobrinha>", views.tiadozap, name="tiadozap"),
]
