import random

from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import GalleryImage, Category, Treatment, MonthlyOffer, Testimonial
from app.serializers import (
    GallerySerializer,
    CategorySerializer,
    TreatmentSerializer,
    MonthlyOfferSerializer,
    TestimonialSerializer,
    EmailSerializer,
)
from app.services.email import ResendError, send_contact_email


class GalleryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        ids = list(self.get_queryset().values_list("pk", flat=True))
        sample_ids = random.sample(ids, min(9, len(ids))) if ids else []
        images = self.get_queryset().filter(pk__in=sample_ids)
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class TreatmentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Treatment.objects.select_related("category").all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.AllowAny]


class MonthlyOfferViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MonthlyOffer.objects.filter(active=True).select_related(
        "treatment__category"
    )
    serializer_class = MonthlyOfferSerializer
    permission_classes = [permissions.AllowAny]


class TestimonialViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]
    sample_size = 6

    def list(self, request, *args, **kwargs):
        ids = list(self.get_queryset().values_list("pk", flat=True))
        sample_ids = random.sample(ids, min(self.sample_size, len(ids))) if ids else []
        testimonials = self.get_queryset().filter(pk__in=sample_ids)
        serializer = self.get_serializer(testimonials, many=True)
        return Response(serializer.data)


class ContactView(APIView):
    throttle_scope = "contact"
    permission_classes = [permissions.AllowAny]
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            send_contact_email(
                serializer.validated_data, reply_to=request.data["email"]
            )
        except ResendError:
            return Response(
                {"message": "E-Mail konnte nicht gesendet werden."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return Response(
            {"message": "Ihre Anfrage wurde gesendet."},
            status=status.HTTP_201_CREATED,
        )
