from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    # content=models.TextField()
    content = RichTextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    message = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
