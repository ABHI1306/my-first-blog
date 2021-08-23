from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'blog_img')

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'blog_img')

    # def save(self, commit=True):
    #     blog_post = self.instance
    #     blog_post.title = self.cleaned_data['title']
    #     blog_post.text = self.cleaned_data['text']

    #     if self.cleaned_data['blog_img']:
    #         blog_post.blog_img = self.cleaned_data['blog_img']

    #     if commit:
    #         blog_post.save()
    #     return blog_post
