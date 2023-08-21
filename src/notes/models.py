from django.db import models


class Notes(models.Model):
    title = models.CharField(null=False, max_length=200)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Note: {self.title}, Body={self.body[0:50]}: {self.created}>"
