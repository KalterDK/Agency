from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.home, name="Home page"),
    url(r'^portfolio/$', views.portfolio, name="Portfolio"),
    url(r'^faq/$', views.faq, name="FAQ"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^success-page/$', TemplateView.as_view(template_name="success_page.html"), name="Success page"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
