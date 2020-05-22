from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("contact/", include("contact.urls")),
    path("posts/", include("posts.urls")),
    path("users/", include("users.urls")),
    path("team/", include("team.urls")),
    path("payments/", include("payments.urls")),  # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
