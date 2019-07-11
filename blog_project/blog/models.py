from django.db import models
from django import forms
from django.urls import reverse
import string
import secrets


# Create your models here.
def Crypto(*args):
	stringSource = args
	password = secrets.choice(string.ascii_lowercase)
	password += secrets.choice(string.ascii_uppercase)
	password += secrets.choice(string.digits)
	password += secrets.choice(string.punctuation)
	for i in range(6):
	    password += secrets.choice(stringSource)
	char_list = list(password)
	secrets.SystemRandom().shuffle(char_list)
	password = ''.join(char_list)
	return password

class Category(models.Model):
	title = models.CharField(max_length=255, verbose_name="Title")

	def __str__(self):
		return self.title

	def get_absolute_url(self):		
		return reverse('category_detail', args=[str(self.title)])


class Post(models.Model):
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
	password = models.CharField(max_length=50)
	body = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])
