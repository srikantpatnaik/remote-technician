from django.http import HttpResponse


def hu(request, userName):
    try:
        userName = str(userName)
    except ValueError:
        raise Http404()
    html = "<html><body>Hello %s</body></html>" %(userName)
    return HttpResponse(html)




