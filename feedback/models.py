from django.db import models

# Create your models here.
class Feedback(models.Model):
    guest_name = models.CharField(max_length=100)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
