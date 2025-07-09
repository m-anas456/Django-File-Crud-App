from django.db import models


class UploadedFile(models.Model):
    # Optional: assign a user if you have authentication
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    filename = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    size = models.PositiveIntegerField()  # size in bytes
    
    def __str__(self):
        return self.filename

    def save(self, *args, **kwargs):
        # Automatically update filename and size on save
        if self.file:
            self.filename = self.file.name
            self.size = self.file.size
        super().save(*args, **kwargs)
