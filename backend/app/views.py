import random

from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response

from app.models import GalleryImage, Category, Treatment, MonthlyOffer, Testimonial
from app.serializers import (
    GallerySerializer,
    CategorySerializer,
    TreatmentSerializer,
    MonthlyOfferSerializer,
    TestimonialSerializer,
)


class GalleryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        count = self.queryset.count()

        qs = list(self.queryset)
        images = random.sample(qs, min(10, count)) if count else []
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class TreatmentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Treatment.objects.select_related("category").all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class MonthlyOfferViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MonthlyOffer.objects.all()
    serializer_class = MonthlyOfferSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class TestimonialViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
