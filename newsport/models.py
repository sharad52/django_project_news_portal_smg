from django.db import models
from .choices import SPORTS_TYPES
from datetime import datetime

# Create your models here
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    phone_no = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/%y/%m/%d',blank=True)
    email = models.EmailField(blank=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'


class News(models.Model):
    news_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/%y/%m/%d',blank=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.DO_NOTHING)
    content = models.TextField()
    subtitle1 = models.TextField(blank=True,null=True)
    content1=models.TextField(blank=True,null=True)
    subtitle2 = models.TextField(blank=True,null=True)
    content2 = models.TextField(blank=True,null=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'



    
    
    