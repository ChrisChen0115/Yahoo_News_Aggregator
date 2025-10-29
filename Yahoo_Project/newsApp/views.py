from django.shortcuts import render
from .models import News
from Yahoo_Project.scraper.yahoo_news_scraper import yahoo_scraper

# Create your views here.
def home(request):
    return render(request, 'home.html')

def crawl_news(request):
    data = yahoo_scraper()
    for item in data:
        News.objects.get_or_create(
            title = item['title'],
            link = item['link'],
            published_at = item['published_at']
        )
    
    news_list = News.objects.all().order_by('-published_at')
    return render(request, 'news.html', {'news_list': news_list})