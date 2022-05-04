from django import forms

from blog.models import Post
from blog.models import FeedBack


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class FeedBackForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(label_suffix=' optional:')
    message = forms.CharField(widget=forms.Textarea)

    def save(self):
        feedback = FeedBack(**self.cleaned_data)
        feedback.save()
