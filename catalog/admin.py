from django.contrib import admin
from .models import Catalog, Member, MediaItem

admin.site.register(Catalog)
admin.site.register(Member)
admin.site.register(MediaItem)
