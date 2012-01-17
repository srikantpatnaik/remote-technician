# from django.template.loader import get_template
# from django.template import Template, Context
# from django.http import HttpResponse

# def current_date(request):
#     now = datetime.datetime.now()
    
#     # Comment any one of the two lines
#     # fp = open('templates/current_date.html')
#     t = get_template('current_date.html')
    
#     c = Context({'current_date': now})
#     html = t.render(c)
#     return HttpResponse(html)

from django.shortcuts import render_to_response
import datetime

def current_date(request):
    # now = datetime.datetime.now()
    # return render_to_response('current_date.html', {'current_date': now})
    current_date = datetime.datetime.now()
    return render_to_response('current_date.html', locals())




