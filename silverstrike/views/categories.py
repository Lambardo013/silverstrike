from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from silverstrike.models import Category


class CategoryIndex(LoginRequiredMixin, generic.ListView):
    template_name = 'silverstrike/category_index.html'
    context_object_name = 'categories'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'categories'
        return context


class CategoryCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories')


class CategoryUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    pass


class CategroyDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    pass