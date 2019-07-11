from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','category', 'body', 'password')

class ValidForm(forms.ModelForm):
	
	class Meta():
		model = Post
		fields = ('password',)