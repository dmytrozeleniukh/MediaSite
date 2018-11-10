from django.views.generic.list import MultipleObjectMixin
from mediasiteapp.models import Category


class CategoryListMixin(MultipleObjectMixin):

	def get_context_data(self, *args, **kwarhs):
		context = {}
		context['categories'] = Category.objects.all()
		return context