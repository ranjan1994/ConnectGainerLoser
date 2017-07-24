from django.conf.urls import url
from django.contrib import admin
from . import views
from topper.views import work

app_name = 'topper'

urlpatterns = [
    url(r'^$',work.login_test, name='login_test'),
    url(r'^volume/$',work.volume, name='volume'),
    url(r'^change/$',work.change, name='change'),
    url(r'^loser/$',work.loser, name='loser'),
]
