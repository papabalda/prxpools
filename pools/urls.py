from django.conf.urls import patterns, include, url

urlpatterns = patterns('pools.views',
    # Examples:
    url(r'^$', 'index'),
    url(r'^home/$', 'index'),
    url(r'^ingresar/$', 'ingresar'),
    url(r'^ingresar/login/$', 'login_call'),
    url(r'^logout/$', 'logout_call'),
    #url(r'^ingresar/sucess$', 'index'),
    url(r'^quiniela/$', 'index'),
    url(r'^quiniela/(?P<quiniela_id>\d+)/$', 'detail'),

)
