from django import forms
from .models import UploadedNote

class UploadedNoteForm(forms.ModelForm):
    class Meta:
        model = UploadedNote
        fields = ['title', 'file']