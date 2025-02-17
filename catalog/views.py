from django.shortcuts import render
from .models import Catalog, MediaItem

# Home Page - List all Catalogs

def home(request):
    catalogs = Catalog.objects.all()
    media_items = MediaItem.objects.order_by("-id")[:6]  # Get last 6 uploaded media files
    return render(request, "catalog/home.html", {"catalogs": catalogs, "media_items": media_items})

# Catalog Detail Page - Show media items inside a catalog
def catalog_detail(request, catalog_id):
    media_items = catalog.media_items.all()
    
    search_query = request.GET.get("search")
    if search_query:
        media_items = media_items.filter(title__icontains=search_query)

    members = catalog.members.all()
    return render(
        request,
        "catalog/catalog_detail.html",
        {"catalog": catalog, "media_items": media_items, "members": members},
    )
