import django
django.setup()

from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule

import feedparser # Used for parsing feeds
from .models import New, Keyword

@shared_task(bind = True)

def fetchData(self):

    #Keywords model -> contains title (APL, TWTR, INTC etc)
    keywords = Keyword.objects.all()

    totalFetched = 0

    for keyword in Keyword.objects.all():
        url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=" + keyword.title + "&region=US&lang=en-US"

        # Fetch all news by keyword AAPL, TWTR etc.
        feeds = feedparser.parse(url)

        for entry in feeds.entries:
            if New.objects.filter(guid = entry.id).exists() == False:

                dT = entry.published_parsed

                New.objects.create(
                    guid = entry.id,
                    title = entry.title,
                    pubDate = str(dT.tm_year) + '-' + str(dT.tm_mon) + '-' + str(dT.tm_mday) + ' ' + str(dT.tm_hour) + ':' + str(dT.tm_min) + ':' + str(dT.tm_sec),
                    description = entry.summary,
                    link = entry.link,
                    keyword_id = keyword.id
                )

                totalFetched += 1


    return "Total fetched " + str(totalFetched)
