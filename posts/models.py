from django.db import models
from django.urls import reverse

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="image/", blank=True, null=True)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("message_detail", args=[str(self.id)])
        return reverse("messages")