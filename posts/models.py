from django.db import models
from categories.models import Category
from users.models import User


class Post(models.Model):
   
    title = models.CharField(max_length=255,db_index=True,verbose_name='Название')
    description = models.TextField(verbose_name='Описание',blank=True, null=True)
    images = models.ImageField(upload_to='post_imag',blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,related_name='product_category',on_delete=models.CASCADE,null=True, blank=True)


    def get_parent(self):
        return self.comment.filter(parent__isnull=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)

