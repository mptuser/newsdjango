from django import forms
from .models import Notes, Comments, Tags

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text', 'author',  'fk_tag']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'fk_tag': forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class TagForm(forms.ModelForm):
    class Meta:  
        model = Tags
        fields = ['tag_name']
        widgets = {
            'tag_name': forms.TextInput(attrs={'class':'form-control'}), 
        }

class CommentForm(forms.Form):
    comment_text = forms.CharField(label = '', widget = forms.Textarea(attrs={'class':'form-control'}))