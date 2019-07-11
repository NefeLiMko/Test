from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView,PostsInCategoryView

urlpatterns = [
	path('post/<int:pk>/delete',BlogDeleteView.as_view(),name="post_delete"),
	path('post/<int:pk>/edit',BlogUpdateView.as_view(), name="post_edit"),
	path('post/new/', BlogCreateView.as_view(), name="post_new"),
	path('post/<int:pk>/', BlogDetailView, name ="post_detail"),
	path('category/<str:title>/', PostsInCategoryView, name ="category_detail"),
	path('', BlogListView, name = 'home'),
]