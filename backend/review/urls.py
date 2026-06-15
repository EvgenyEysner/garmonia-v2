from django.urls import path

from .views import GoogleOAuthInitView, GoogleOAuthCallbackView, GoogleReviewsView

urlpatterns = [
    path("oauth/start/", GoogleOAuthInitView.as_view(), name="google-oauth-start"),
    path("oauth/callback/", GoogleOAuthCallbackView.as_view(), name="google-oauth-callback"),
    path("", GoogleReviewsView.as_view(), name="google-reviews"),
]
