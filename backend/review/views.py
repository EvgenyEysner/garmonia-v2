import os

from django.core.cache import cache
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from review.services.google_reviews import get_flow, save_credentials, fetch_all_reviews, generate_pkce_pair

STAR_MAP = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5}


class GoogleOAuthInitView(APIView):
    def get(self, request):
        code_verifier, code_challenge = generate_pkce_pair()

        flow = get_flow()
        auth_url, state = flow.authorization_url(
            access_type="offline",
            include_granted_scopes="true",
            prompt="consent",
            code_challenge=code_challenge,  # ← manuell übergeben
            code_challenge_method="S256",
        )

        # In Session speichern
        request.session["oauth_state"] = state
        request.session["oauth_code_verifier"] = code_verifier
        request.session.modified = True  # ← Session-Save erzwingen

        return redirect(auth_url)


class GoogleOAuthCallbackView(APIView):
    def get(self, request):
        code = request.GET.get("code")
        if not code:
            return Response({"error": "Kein Code erhalten"}, status=400)

        code_verifier = request.session.get("oauth_code_verifier")
        if not code_verifier:
            return Response({"error": "Session abgelaufen – bitte OAuth neu starten"}, status=400)

        flow = get_flow()
        token = flow.oauth2session.fetch_token(
            "https://oauth2.googleapis.com/token",
            code=code,
            code_verifier=code_verifier,
            client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
        )

        from google.oauth2.credentials import Credentials
        creds = Credentials(
            token=token["access_token"],
            refresh_token=token.get("refresh_token"),
            token_uri="https://oauth2.googleapis.com/token",
            client_id=os.environ.get("GOOGLE_CLIENT_ID"),
            client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
        )
        save_credentials(creds)

        request.session.pop("oauth_state", None)
        request.session.pop("oauth_code_verifier", None)

        return Response({"message": "✅ Authentifizierung erfolgreich! Token gespeichert."})


class GoogleReviewsView(APIView):
    def get(self, request):
        cache_key = "google_reviews_all"
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        try:
            raw_reviews = fetch_all_reviews()
            reviews = [
                {
                    "author": r.get("reviewer", {}).get("displayName", "Anonym"),
                    "profile_photo": r.get("reviewer", {}).get("profilePhotoUrl", ""),
                    "rating": STAR_MAP.get(r.get("starRating", ""), 0),
                    "text": r.get("comment", ""),
                    "date": r.get("createTime", ""),
                    "reply": r.get("reviewReply", {}).get("comment", None),
                }
                for r in raw_reviews
            ]
            cache.set(cache_key, reviews, timeout=3600)
            return Response(reviews)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
