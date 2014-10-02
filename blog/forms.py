from django import forms
from .models import Post

class PostForm(froms.modelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)
        