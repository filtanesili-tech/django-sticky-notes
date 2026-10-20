from django.db import models

class Note(models.Model):
    """A sticky note saved by a user."""
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=100, default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.title
