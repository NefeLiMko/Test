from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Category, Post, Crypto
from .forms import PostForm, ValidForm
# Create your views

def BlogListView(request):
	categories = Category.objects.all()
	posts = Post.objects.all()
	template_name = 'home.html'
	return render(request,template_name,{
		'categories':categories,
		'posts':posts,	
		})

def PostsInCategoryView(request,*args,**kwargs):
	categories = Category.objects.all()
	for cat in categories:
		if str(cat.title) == str(kwargs['title']):
			category = cat
	posts_to_view = []
	posts = Post.objects.all()
	template_name = 'category_detail.html'
	for post in posts:
		if str(post.category) == str(kwargs['title']):
			posts_to_view.append(post)

	return render(request,template_name,{
		'posts':posts_to_view,
		'pos':posts,
		'categor':category,
		'categories':categories,
		})


def BlogDetailView(request,*args,**kwargs):
	form = ValidForm()
	categories = Category.objects.all()
	posts = Post.objects.all()
	for post in posts:
		if str(post.id) == str(kwargs['pk']):
			pos = post
			cryptoTitle = Crypto(str(pos.title))
			cryptoBody = Crypto(str(pos.body))
	template_name = 'post_detail.html'
	res = False
	if request.method == "GET":
		got = request.GET.get('password')
		if got == pos.password:
			res = True
	return render(request,template_name,{
		'posts':posts,
		'post':pos,
		'categories':categories,
		'form':form,
		'got':res,
		'cryptoTitle':cryptoTitle,
		'cryptoBody':cryptoBody,
		})

class BlogCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'category', 'body' , 'password']

class BlogUpdateView(UpdateView):
	model =Post
	template_name = 'post_edit.html'
	fields =['title','category', 'body']		

class BlogDeleteView(DeleteView):
	model = Post
	template_name="post_delete.html"
	success_url = reverse_lazy('home')