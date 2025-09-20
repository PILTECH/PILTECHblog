from django.db import models

#models


class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class EntryImage(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='entry_images/')

    def __str__(self):
        return f"Image for {self.entry.title}"
