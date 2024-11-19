
from django import forms
from .models import BlogPosting

class BlogForm(forms.ModelForm):

    class Meta:

        model = BlogPosting
        fields = ['title','description','content','image']

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Description'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Content'}),
        }

class CommnetForm(forms.ModelForm):

    class Meta:

        model = BlogPosting
        fields = ['comment']

        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'comment'}),
        }
