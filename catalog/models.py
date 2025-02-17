from django.db import models

# Catalog Model (e.g., Radio, TV)
class Catalog(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Member Model (Unique per Catalog)
class Member(models.Model):
    name = models.CharField(max_length=100)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return f"{self.name} ({self.catalog.name})"

# MediaItem Model (Videos, Music, Docs, Pics)
class MediaItem(models.Model):
    MEDIA_TYPES = [
        ('video', 'Video'),
        ('music', 'Music'),
        ('document', 'Document'),
        ('picture', 'Picture'),
    ]
    
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="media_files/")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="media_items")

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"
