from django.shortcuts import render
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def article_view(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/404.html", {
            "title": title
        })
    else:    
        return render(request, "encyclopedia/article.html", {
            "contents": util.markdown_to_html(util.get_entry(title)),

            "title" : title
        })


def search_view(request):
    search = request.GET.get('q')
    entries = util.list_entries()
    results = []
    for entry in entries:
        if search in entry:
            results.append(entry)
    if len(results) >1:
        return render(request, "encyclopedia/index.html", {
        "entries": results
    })
    elif len(results) ==1 and util.get_entry(search) == None:
        return render(request, "encyclopedia/index.html", {
        "entries": results
    })
    elif len(results) ==1:
        return article_view(request, search)
    else:
        
        return article_view(request, search)


def newpage_view(request):
    if request.method== "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        util.save_entry(request.POST.get('title'), request.POST.get('content'))
        return article_view(request, request.POST.get('title'))


def random_view(request):
    x = util.list_entries()
    i = random.randrange(0, len(x))
    article = x[i]
    return article_view(request, article)

def edit_view(request):
    title = request.GET.get('head')
    return render(request, "encyclopedia/editpage.html", {
            "contents": util.get_entry(title),
            "title" : title
        })