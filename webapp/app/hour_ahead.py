# from django.http import Http404, HttpResponse
# import datetime

# def hour_ahead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(offset, dt)
#     return HttpResponse(html)

from django.shortcuts import render_to_response
import datetime

def hour_ahead(request, hour_offset):
    try:
        hour_offset = int(hour_offset)
    except ValueError:
        raise Http404()
    
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('hour_ahead.html', locals())


    
