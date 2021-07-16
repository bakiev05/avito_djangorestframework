from django.db import models
from posts.models import Post

from users.models import User


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    owner = models.ForeignKey(User,related_name='user',verbose_name='Автор',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.id}"

