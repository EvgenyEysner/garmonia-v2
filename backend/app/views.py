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
        count = self.get_queryset().count()

        qs = list(self.get_queryset())
        images = random.sample(qs, min(10, count)) if count else []
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
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


class ContactView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            send_contact_email(serializer.validated_data)
        except Treatment.DoesNotExist:
            return Response(
                {"treatment_id": ["Ungültige Behandlung."]},
                status=status.HTTP_400_BAD_REQUEST,
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
