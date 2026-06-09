from django.contrib import admin
from django.utils.html import format_html

from .models import Treatment, MonthlyOffer, Category, Testimonial, GalleryImage


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "price")
    list_filter = ("category", "name")
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(MonthlyOffer)
class MonthlyOfferAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "active", "price")
    list_filter = ("title", "active")
    search_fields = ["title"]
    ordering = ["title"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ["name"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "text")
    ordering = ["last_name"]


@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" style="width: 50px; height: 50px;"/>'
        )

    image_tag.short_description = "Bild"

    list_display = ("image_tag", "description")
    ordering = ["description"]
