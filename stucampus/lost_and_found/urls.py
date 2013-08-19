from django.conf.urls import patterns, url
from stucampus.lost_and_found.views import IndexView, add_message

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^add_message/$', add_message, name='add_message'),
)
