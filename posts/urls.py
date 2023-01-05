from django.urls import path

from posts.views import HomePageView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("messages/", MessageListView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("messages/create/", MessageCreateView.as_view(), name="message_create"),
    path("messages/<int:pk>/update/", MessageUpdateView.as_view(), name="messages_edit"),
    path("messages/<int:pk>/delete/", MessageDeleteView.as_view(), name="messages_delete")
]

