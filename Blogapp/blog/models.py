from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='p_img')
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_body = models.TextField()
    post_img = models.ImageField(upload_to="post_img")
    post_date = models.DateTimeField(auto_now_add=False)
    post_update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title