from django.shortcuts import render
from . import models

# Create your views here.

def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    arge = {'articles' : articles}
    return render(request, 'articles/articleslist.html', arge)

    
