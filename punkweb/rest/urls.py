from django.conf.urls import url, include
from rest_framework import routers

from apps.analytics.views import (
    AnalyticsEventViewSet,
    ClientErrorViewSet,
)

from apps.contact.views import (
    ContactFormViewSet,
)

from apps.music.views import (
    ArtistViewSet,
    AlbumViewSet,
    AudioViewSet,
    ArtistEventViewSet,
)

from punkweb_boards.rest.views import (
    BoardProfileViewSet,
    CategoryViewSet,
    SubcategoryViewSet,
    ThreadViewSet,
    PostViewSet,
    ConversationViewSet,
    MessageViewSet,
    ShoutViewSet,
)

from punkweb.rest.views import (
    UserViewSet,
    UserCreateView,
    obtain_auth_token,
)

router = routers.DefaultRouter()

router.register(
    r"analytics/analytics_events", AnalyticsEventViewSet, base_name="analytics_events")
router.register(
    r"analytics/client_errors", ClientErrorViewSet, base_name="client_errors")
router.register(r"contact_forms", ContactFormViewSet, base_name="contact_forms")

router.register(r"board/categories", CategoryViewSet, base_name="categories")
router.register(r"board/subcategories", SubcategoryViewSet, base_name="subcategories")
router.register(r"board/threads", ThreadViewSet, base_name="threads")
router.register(r"board/posts", PostViewSet, base_name="posts")
# router.register(r"board/conversations", ConversationViewSet, base_name="conversations")
# router.register(r"board/messages", MessageViewSet, base_name="messages")
router.register(r"board/shouts", ShoutViewSet, base_name="shouts")
router.register(r"board/profiles", BoardProfileViewSet, base_name="profiles")

router.register(r"artists", ArtistViewSet, base_name="artists")
router.register(r"albums", AlbumViewSet, base_name="albums")
router.register(r"audio", AudioViewSet, base_name="audio")
router.register(r"artist_events", ArtistEventViewSet, base_name="artist_events")
router.register(r"users", UserViewSet, base_name="users")

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^token-auth/", obtain_auth_token),
    url(r"^register/", UserCreateView.as_view(), name='create-account'),
]
