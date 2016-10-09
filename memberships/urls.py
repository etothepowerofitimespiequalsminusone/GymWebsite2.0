from django.conf.urls import url

from . import views
app_name = 'memberships'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),

    url(r'^details/$',views.MembershipView.as_view(),name='details'),

    url(r'^classes/$',views.ClassesView.as_view(),name='classes'),

    url(r'^(?P<type_id>[0-9]+)/$', views.detail,name='detail')
]
