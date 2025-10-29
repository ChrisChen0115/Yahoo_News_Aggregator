from django.http import JsonResponse
from .models import News
from Yahoo_Project.scraper.yahoo_news_scraper import yahoo_scraper

# Create your views here.
def crawl_news(request):
    data = yahoo_scraper()
    for item in data:
        News.objects.get_or_create(
            title = item['title'],
            link = item['link'],
            published_at = item['published_at']
        )
    return JsonResponse({"status": "success", "count": len(data)})