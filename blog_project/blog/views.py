from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Category, Post
# Create your views

def BlogListView(request):
	categories = Category.objects.all()
	posts = Post.objects.all()
	template_name = 'home.html'
	return render(request,template_name,{
		'categories':categories,
		'posts':posts,	
		})

class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title','category', 'author', 'body']	

class BlogUpdateView(UpdateView):
	model =Post
	template_name = 'post_edit.html'
	fields =['title','category', 'body']		

class BlogDeleteView(DeleteView):
	model = Post
	template_name="post_delete.html"
	success_url = reverse_lazy('home')