from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crawl/', views.crawl_news, name='crawl_and_show'),
]