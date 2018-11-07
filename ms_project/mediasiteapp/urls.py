from django.conf.urls import url
from mediasiteapp.views import CategoryListView

urlpatterns = [
    url(r'^$', CategoryListView.as_view()),
]