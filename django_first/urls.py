from django.conf.urls import include, url
from django.contrib import admin
from apps.secondapp import views

urlpatterns = [
    url(r'^user/', include('apps.users.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]