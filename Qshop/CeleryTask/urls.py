from CeleryTask.views import *
from django.urls import path

urlpatterns = [
    path("demo/", get_celery)
]