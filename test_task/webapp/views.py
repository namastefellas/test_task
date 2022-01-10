from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from webapp.models import Card
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)
from webapp.forms import CardForm, SearchForm



class CardView(ListView):
    template_name = 'card/cards.html'
    model = Card
    context_object_name = 'cards'
    ordering = ('card_owner', '-created_at')

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(CardView, self).get(request, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(card_status=True,)

        if self.search_data:
            queryset = queryset.filter(
                Q(card_owner__icontains=self.search_data) |
                Q(card_balance__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class CardOwnerDetailView(DetailView):
    model = Card
    template_name = 'card/card_owner_view.html'

class CardCreateView(CreateView):
    template_name = 'card/card_create.html' 
    model = Card
    form_class = CardForm

    def form_valid(self, form):
        card = form.save()
        return redirect('webapp:card_owner', pk=card.pk)

class CardDeleteView(DeleteView):
    model = Card
    template_name = 'card/card_delete.html'
    context_object_name = 'card'
    success_url = reverse_lazy('webapp:card_list')

class CardDeactivateView(ListView):
    template_name = 'status/list_to_activate.html'
    model = Card
    context_object_name = 'cards'
    ordering = ('-created_at')

    def get_queryset(self):
        queryset = queryset = super().get_queryset()
        return queryset