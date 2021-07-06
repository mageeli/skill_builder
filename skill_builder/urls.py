from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [

    url(r'^skills/$', views.SkillView.as_view(), name='skills'),
    url(r'^skill/(?P<pk>[0-9]+)/$', views.SubSkillView.as_view(), name='skill'),
    url(r'^skilll/(?P<pk>[0-9]+)/$', views.HomePageView.as_view(), name='skill'),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^add_skills/$', views.AddSkillsView.as_view(success_url="/skills/"), name='add_skills'),
    url(r'^add_sub_skills/$', views.AddSubSkillsView.as_view(success_url="/skills/"), name='add_sub_skills'),
    path('', views.HomeView.as_view(), name='home'),
]