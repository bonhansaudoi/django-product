from django.views import generic
from .models import Article

class ArticleListView(generic.ListView):
    model = Article
    # template_name = 'article_list.html'


class ArticleDetailView(generic.DetailView):
    model = Article
    # template_name = 'article_detail.html'


""" 
from django.utils import timezone
from django.views.generic.list import ListView

from articles.models import Article

class ArticleListView(ListView):

    model = Article
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


from django.utils import timezone
from django.views.generic.detail import DetailView

from articles.models import Article

class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


<h1>Articles</h1>
<ul>
{% for article in object_list %}
    <li>{{ article.pub_date|date }} - {{ article.headline }}</li>
{% empty %}
    <li>No articles yet.</li>
{% endfor %}
</ul>

<h1>{{ object.headline }}</h1>
<p>{{ object.content }}</p>
<p>Reporter: {{ object.reporter }}</p>
<p>Published: {{ object.pub_date|date }}</p>
<p>Date: {{ now|date }}</p>

path('', ArticleListView.as_view(), name='article-list'),
path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),

"""
