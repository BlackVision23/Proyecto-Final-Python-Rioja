from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class PostSearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Buscar publicaciones'
    )

class UserSearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Buscar usuarios'
    )

    def search(self):
        query = self.cleaned_data['query']
        return User.objects.filter(username__icontains=query)