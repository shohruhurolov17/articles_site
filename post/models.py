from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField

import post


# Create your models here.


class Post(models.Model):

    objects = None
    title = models.CharField(max_length=130)
    body = RichTextField()
    photo = models.ImageField(upload_to='photos/')
    likes = models.ManyToManyField(get_user_model(), related_name='likes')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.pk)])



