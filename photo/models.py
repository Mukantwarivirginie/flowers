# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.




class Profile(models.Model):
    name = models.CharField(max_length =60)
    picture = models.ImageField(upload_to='photo/', blank=True) 
    bio = models.CharField(max_length =500)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()
    def display_profile(self):
        self.display()


    class Meta:
        ordering = ['name']



class Bouquets(models.Model):
    
    # title = models.CharField(max_length =30)
    picture = models.ImageField(upload_to='photos/',null=True)
    bio = models.CharField(max_length =500)
    name= models.TextField()
    # link = models.TextField()

    def __str__(self):
        return self.title

    def save_bouquets(self):
        self.save()
    
   
    def display_bouquets(self):
        self.display()

    def delete_bouquets(self):
        self.delete()
    

    @classmethod
    def get_bouguets(cls,id):
        return Bouquets.objects.get(id=id)


    
class Decoration(models.Model):
    
    # title = models.CharField(max_length =30)
    picture = models.ImageField(upload_to='photos/',null=True) 
    bio = models.CharField(max_length =500)
    name= models.TextField()
    # link = models.TextField()

    def __str__(self):
        return self.title

    def save_decoration(self):
        self.save()
    
   
    def display_decoration(self):
        self.display()

    def delete_decoration(self):
        self.delete()
    




    

    @classmethod
    def search_by_title(cls,search_term):
        bouquets=Bouquets.objects.filter(title__icontains=search_term).all()
        return bouquets
     
 

    class Meta:
        ordering = ['title']


class SignUpRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


