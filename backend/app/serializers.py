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
        fields = ["id", "first_name", "last_name", "full_name", "text"]


class EmailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=30)
    treatment_id = serializers.IntegerField()
    message = serializers.CharField(required=False, allow_blank=True, max_length=2000)

    def validate_treatment_id(self, value):
        if not Treatment.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Behandlung existiert nicht.")
        return value
