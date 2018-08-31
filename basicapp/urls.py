from  django.conf.urls import url
from basicapp import views

urlpatterns = [
    url(r'^$', views.users, name='users'),

]
