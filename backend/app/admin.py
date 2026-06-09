from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from .models import Treatment, MonthlyOffer, Category, Testimonial, GalleryImage


@admin.register(Treatment)
class TreatmentAdmin(ModelAdmin):
    list_display = ("category", "name", "price")
    list_filter = ("category", "name")
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(MonthlyOffer)
class MonthlyOfferAdmin(ModelAdmin):
    list_display = ("title", "description", "active", "price")
    list_filter = ("title", "active")
    search_fields = ["title"]
    ordering = ["title"]


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("name",)
    ordering = ["name"]


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ("first_name", "last_name", "text")
    ordering = ["last_name"]


@admin.register(GalleryImage)
class GalleryAdmin(ModelAdmin):
    list_display = ("image_tag", "description")
    ordering = ["description"]

    @admin.display(description="Bild")
    def image_tag(self, obj):
        if not obj.image:
            return "—"
        return format_html(
            '<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" alt="" />',
            obj.image.url,
        )
