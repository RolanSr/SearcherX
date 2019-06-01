from django.shortcuts import render
from . import attachments


def home(request):
    data = {
        'attachments': attachments.getAtachments(),
        'title': 'SearcherX - Main',
    }
    return render(request, 'main/main.html', data)

def DetailSearcher(request):
    data = {
        'title': 'DetailSearcher',
    }
    return render(request, 'main/detailSearcher.html', data)

def ExpressAdds(request):
    data = {
        'title': 'ExpressAdds',
    }
    return render(request, 'main/expressAdds.html', data)
