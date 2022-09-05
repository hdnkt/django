from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    path("", views.index, name="index"),
    path("vote/", views.vote),
    path("result/<username>/",views.result),
    path("result/<username>/r",views.resultr),
    
]