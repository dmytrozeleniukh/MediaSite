from django.conf.urls import url
from mediasiteapp.views import ArticleListView

urlpatterns = [
    url(r'^$', ArticleListView.as_view()),
]