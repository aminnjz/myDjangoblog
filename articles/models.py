
from email.mime import image
from email.policy import default
from email.quoprimime import body_check
from pyexpat import model
from statistics import mode
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100) 
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add =  True)
    image = models.ImageField(default = 'default.jpg', blank = True)
    # add in author
    
    def __str__(self):
        return self.title
    
    
    
    def snippet(self):
        return self.body[:50] + ' ...'
