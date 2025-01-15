from django.contrib import admin
from .models import BonkProfile, HighScore
from cloudinary.models import CloudinaryField
from django.utils.html import format_html

# Register your models here.
# admin.site.register(BonkProfile)


@admin.register(BonkProfile)
class BonkProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'image_preview')

    def image_preview(self, obj):
        if obj.profile_pic:
            return format_html('<img src="{}" style="width: 100px; height: auto;">', obj.profile_pic.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

admin.site.register(HighScore)