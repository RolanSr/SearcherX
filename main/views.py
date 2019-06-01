from django.shortcuts import render
from . import attachments

def home(request):
    data = {
        'attachments': attachments.getAtachments(),
        'title': 'SearcherX - Main',
        'input_info': 'main/',
    }
    return render(request, 'main/main.html', data)

def DetailSearcher(request):
    data = {
        'title': 'DetailSearcher',
        'input_info': 'main/detailsearcher/',
    }
    return render(request, 'main/detailSearcher.html', data)

def ExpressAdds(request):
    data = {
        'title': 'ExpressAdds',
        'input_info': 'main/expressadds/',
    }
    return render(request, 'main/expressAdds.html', data)
