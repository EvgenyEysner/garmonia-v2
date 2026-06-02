from rest_framework import serializers

from app.models import GalleryImage, Category, Treatment, MonthlyOffer, Testimonial


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ["id", "image", "description"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TreatmentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    name = serializers.CharField(source="get_treatment_name", read_only=True)

    class Meta:
        model = Treatment
        fields = ["id", "name", "category", "description", "price"]


class MonthlyOfferSerializer(serializers.ModelSerializer):
    treatment = TreatmentSerializer(read_only=True)

    class Meta:
        model = MonthlyOffer
        fields = ["id", "treatment", "title", "description", "image", "active", "price"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "full_name", "text"]
