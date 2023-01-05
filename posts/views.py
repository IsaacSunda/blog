from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from posts.models import Message


# Create your views here.
class HomePageView(TemplateView):
    model = Message
    template_name = "posts/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Message.objects.all()
        return context


class MessageListView(ListView):
    model = Message
    template_name = "posts/messages.html"
    context_object_name = "posts"


class MessageDetailView(DetailView):
    model = Message
    template_name = "posts/message_detail.html"
    context_object_name = "post"


class MessageCreateView(CreateView):
    model = Message
    template_name = "posts/message_create.html"
    fields = '__all__'

class MessageUpdateView(UpdateView):
    model = Message
    template_name = "posts/message_update.html"
    fields = ["title", "message"]

class MessageDeleteView(DeleteView):
    model = Message
    template_name = "posts/message_delete.html"
    success_url = reverse_lazy("messages")
    context_object_name = "posts"
