from django.conf.urls import patterns , url

from new import views

urlpatterns=patterns('',
	url(r'^$' , views.register , name='register')
)

