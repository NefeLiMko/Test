from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=255, verbose_name="Title")

	def __str__(self):
		return self.title



class Post(models.Model):
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
	author = models.ForeignKey(
		'auth.User',
		on_delete = models.CASCADE,
		)
	body = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])
