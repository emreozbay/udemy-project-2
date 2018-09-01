from  django.conf.urls import url
from basicapp import views

app_name = 'basicapp'

urlpatterns = [

    #url(r'^$', views.users, name='users'),
    url(r'^relative/$',views.relative,name= 'relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^register/$', views.register, name='register'),
    url(r'user_login/$',views.user_login, name='user_login')

]
