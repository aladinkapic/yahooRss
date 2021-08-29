from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
import json
import datetime
from datetime import date


# Views and models
from news.views import index, preview
from .models import New, Keyword

# Test urls
class TestUrls(SimpleTestCase):

    def test_news_is_resolved(self):
        url = reverse('news:news-index')
        self.assertEquals(resolve(url).func, index)

    def test_news_preview_is_resolved(self):
        url = reverse('news:news-preview', args = [1])
        self.assertEquals(resolve(url).func, preview)


# Test views
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.news = reverse('news:news-index')
        self.news_preview = reverse('news:news-preview', args = [81])

    def test_news_GET(self):
        response = self.client.get(self.news)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/index.html')


# Test Models
class TestModels(TestCase):

    def test_create_models(self):

        self.keyword = Keyword.objects.create(
            title = 'AAPL', # Test case as keyword
        )

        self.new = New.objects.create(
            guid = 'xxxx-yyyy',
            title = 'Test title',
            pubDate = datetime.datetime.now(),
            description = 'Test case scenario',
            link = 'https://google.ba',
        )


# Test API
class TestAPI(TestCase):

    def setUp(self):
        self.client = Client()
        self.api = '/api/get-news'

        self.keyword = Keyword.objects.create(
            title = 'AAPL', # Test case as keyword
        )

    def test_api_GET(self):
        response = self.client.get(self.api)
        self.assertEquals(response.status_code, 200)

    def test_api_POST(self):
        data = {
            "date" : "2021-08-29",
            "keyword" : "AAPL"
        }
        response = self.client.post(self.api, data)

        self.assertEquals(response.status_code, 200)
