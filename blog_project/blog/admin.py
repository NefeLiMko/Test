from django.contrib import admin
from .models import Post,Category
# Register your models here.

"""class PostInline(admin.TabularInline):
	model = Post

class CategoryAdmin(admin.ModelAdmin):
	inlines=[
		PostInline,
	]

"""

admin.site.register(Category)