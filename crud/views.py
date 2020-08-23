from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Message


class MessageList(ListView):
    model = Message


class MessageDetail(DetailView):
    model = Message


class MessageCreate(CreateView):
    model = Message
    fields = '__all__'


class MessageUpdate(UpdateView):
    model = Message
    fields = "__all__"


class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy("crud:message-list")