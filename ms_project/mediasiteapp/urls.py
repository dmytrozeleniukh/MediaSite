from django.conf.urls import url
from mediasiteapp.views import CategoryListView, CategoryDetailView

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name='base_view'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
]