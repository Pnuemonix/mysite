from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'mycv.views.skills', name='all_skills'),
]
