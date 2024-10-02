from django.db import models
from django.contrib.auth.models import User

class ChatBoard(models.Model):
    name = models.CharField(max_length=35, unique=True)
    details = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class ChatTopic(models.Model):
    subject = models.CharField(max_length=250)
    lastUpdate = models.DateTimeField(auto_now_add=True)
    boardname = models.ForeignKey(ChatBoard, related_name='topics', on_delete=models.CASCADE)
    boardStarter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject  # Add a string representation for better debugging

class Post(models.Model):
    message = models.TextField(max_length=5000)
    topic = models.ForeignKey(ChatTopic, related_name='posts', on_delete=models.CASCADE)  # Change 'post' to 'posts' for clarity
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(null=True, blank=True)  # Use 'blank=True' for form validation
    createdBy = models.ForeignKey(User, related_name='created_posts', on_delete=models.CASCADE)
    updatedBy = models.ForeignKey(User, null=True, related_name='updated_posts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message[:20]}..."  # Display the first 20 characters of the message
