from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def my_homepage(request):
    return HttpResponse("My Home Page")

def one_hour_ahead(request):
    now = date.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


