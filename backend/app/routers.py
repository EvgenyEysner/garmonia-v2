from rest_framework.routers import DefaultRouter

from app.views import (
    GalleryViewSet,
    CategoryViewSet,
    TestimonialViewSet,
    TreatmentViewSet,
    MonthlyOfferViewSet,
)

router = DefaultRouter()

router.register("gallery", GalleryViewSet, "gallery")
router.register("category", CategoryViewSet, "category")
router.register("treatment", TreatmentViewSet, "treatment")
router.register("monthly-offer", MonthlyOfferViewSet, "monthly-offer")
router.register("testimonial", TestimonialViewSet, "testimonial")
