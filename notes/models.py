from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    """Represent a note owned by a user."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the title, or content if blank."""
        return self.title or self.content[:50]
