from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import Http404

cnt = 5
articles = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz', 'tags': []},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi', 'tags': []},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong', 'tags': []},
    {'id': 4, 'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla', 'tags': []},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector', 'tags': []},
]


def create_article(title, author, articles, cnt):
    cnt += 1
    new_article = {
        'id': cnt,
        'title': title,
        'author': author,
    }
    articles.append(new_article)


# Create your views here.
@csrf_exempt
@require_http_methods(["GET", "POST"])
def index(request):
    global articles, cnt
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        create_article(title, author, articles, cnt)
    return render(
        request,
        'articles/index.html',
        context={
          'articles': articles
        }
    )

@require_http_methods(["GET"])
def show_article(request, article_id):
    try:
        article = next(a for a in articles if a['id'] == article_id)
    except StopIteration as e:
        raise Http404()

    return render(
        request,
        'articles/article.html',
        context={
            'article': article,
        }
    )
