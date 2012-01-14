from django.http import Http404, HttpResponse
import datetime

def min_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(minutes=offset)
    html = "<html><body>In %s min(s), it will be %s.</body></html>" %(offset, dt)
    return HttpResponse(html)




    
