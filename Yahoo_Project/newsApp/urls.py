from django.urls import path
from . import views

urlpatterns = [
    path('', views.crawl_news, name='crawl_news'),
]