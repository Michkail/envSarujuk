"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("accounts/", include('account.urls')),
    path("mock/charts/", mock_charts, name="mock-charts"),
    path("mock/forms/", mock_forms, name="mock-forms"),
    path("mock/icons/", mock_icons, name="mock-icons"),
    path("mock/tables/", mock_tables, name="mock-tables"),
    path("mock/feature/button/", mock_feature_button, name="mock-feature-button"),
    path("mock/feature/dropdown/", mock_feature_dropdown, name="mock-feature-dropdown"),
    path("mock/feature/typography/", mock_feature_typography, name="mock-feature-typography")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "core.views.bad_req"  # BAD REQUEST
handler403 = "core.views.permission_denied"  # PERMISSION DENIED
handler404 = "core.views.page_not_found"  # PAGE NOT FOUND
handler500 = "core.views.server_err"  # SERVER ERROR
