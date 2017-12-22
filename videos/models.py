from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=120)
    embed_code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
            return '/videos/' #특별한경로가없으면 이쪽의 경로로이동