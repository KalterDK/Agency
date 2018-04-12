from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="Home page"),
    url(r'^portfolio/$', views.portfolio, name="Portfolio"),
    url(r'^faq/$', TemplateView.as_view(template_name="faq.html"), name="FAQ"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^success_page/$', TemplateView.as_view(template_name="success_page.html"), name="Success page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)