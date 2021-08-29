from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
import datetime

# Rest framework imports
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import NewSerializer

# Import models and pagination extra stuffs
from .models import New, Keyword
from .classes import cPagination, Validation

def index(request):
    # get all news from database
    news = New.objects.all()

    # Take only 4 news
    p = Paginator(news, 4)

    # Get page number from get request
    page_number = int(request.GET.get('page', 1))

    try:
        page = p.page(page_number)
    except EmptyPage:
        page = p.page(1)


    data = {
        'news' : page,
        'pages' : page.paginator.num_pages,
        'range' : cPagination.get(int(page_number), page.paginator.num_pages)
    }

    return render(request, 'news/index.html', data)

def preview(request, id):
    data = {
        'news' : New.objects.get(id = id)
    }
    return render(request, 'news/preview.html', data)

# Class for api view - Only allow POST method

class NewsAPI(APIView):
    def get(self, request):
        serializer = NewSerializer(New.objects.all(), many = True)
        return Response(serializer.data)

    def post(self, request):
        keyword = Keyword.objects.get( title =  request.POST.get('keyword')) # Get keyword_id from keyword

        validate = Validation.dValidate(request.POST.get('date'))
        r_data = {} # Empty response

        if(validate['code'] == '0000'):
            data    = New.objects.filter(pubDate__startswith = request.POST.get('date'), keyword_id = keyword.id) # Get data by keyword and date

            r_data  = NewSerializer(data, many = (False if data.count() == 1 else True)).data
            message = "Total : " + str(data.count())
        else:
            message = validate['message']

        return Response({
           'data' : r_data,
           'message': message
        })