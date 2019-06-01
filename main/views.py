from django.shortcuts import render

news = [
    {
        'title': 'Наша первая запись',
        'text': "text text text text text text text text text text text text",
        'date': 'date date date',
        'author': 'author',
    },
    {
        'title': 'Наша lol запись',
        'text': "text2 text2 text2 text2 text2 text2 text2 text2 text2 text2 text2 text2",
        'date': 'date2 date2 date2',
    },
]

def home(request):
    data = {
        'news':news,
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
