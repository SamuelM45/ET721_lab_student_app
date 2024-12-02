from django.shortcuts import render
from .models import NoteUpload
from .forms import NoteUploadForm

def upload_notes(request):
    if request.method == 'POST':
        form = NoteUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_notes:success')
    else:
        form = NoteUploadForm()
    return render(request, 'upload_notes/upload_notes.html', {'form': form})