from django.conf.urls import patterns , url

from timeline import views

urlpatterns= patterns('',
    url(r'^$' , views.index , name='index')
)


