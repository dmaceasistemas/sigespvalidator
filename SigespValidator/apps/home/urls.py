from django.conf.urls import patterns, include, url


urlpatterns = patterns('SigespValidator.apps.home.views',
     
	url(r'^$','home_view',name='home_view'),   

	url(r'^validarConstancia/$','constancia_view',name='constancia_view'),   
)

