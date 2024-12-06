from django.shortcuts import render
from .models import UploadedNote

def uploaded_notes(request):
    notes = UploadedNote.objects.all()
    return render(request, 'upload_notes/uploaded_notes.html', {'notes': notes})
