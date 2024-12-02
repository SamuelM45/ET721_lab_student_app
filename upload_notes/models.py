from django.db import models

class NoteUpload(models.Model):
    title = models.CharField(max_length=200)
    note_file = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

