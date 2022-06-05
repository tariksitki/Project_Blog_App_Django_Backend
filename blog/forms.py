
from django import forms
from .models import Post, Category

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "status", "content", "image")




class CategoryForm(forms.ModelForm):
     class Meta:
         model = Category
         fields = ("category",)




