from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="Home page"),
    url(r'^portfolio/$', TemplateView.as_view(template_name="portfolio.html"), name="Portfolio"),
    url(r'^faq/$', TemplateView.as_view(template_name="faq.html"), name="FAQ"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^success_page/$', TemplateView.as_view(template_name="success_page.html"), name="Success page"),
]
