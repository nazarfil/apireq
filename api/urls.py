from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^contact/$', views.ContactList.as_view()),
    url(r'^request/$', views.ResearchRequestList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)