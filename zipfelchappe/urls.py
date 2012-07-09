from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
    url(r'^projects/$',
        views.ProjectListView.as_view(),
        name='zipfelchappe_project_list'),
    url(r'^projects/(?P<slug>[\w-]+)/$',
        views.ProjectDetailView.as_view(),
        name='zipfelchappe_project_detail'),
    url(r'^category/(?P<slug>[\w-]+)/',
        views.ProjectCategoryListView.as_view(),
        name='zipfelchappe_project_category_list'),
    url(r'^back/(?P<slug>[\w-]+)/$',
        views.project_back_form,
        name='zipfelchappe_project_back_form'),
    url(r'^backer/authenticate/$',
        views.backer_authenticate,
        name='zipfelchappe_backer_authenticate'),
    url(r'^backer/login/$',
        views.BackerLoginView.as_view(),
        name='zipfelchappe_backer_login'),
    url(r'^backer/profile/$',
        login_required(views.BackerLoginView.as_view()),
        name='zipfelchappe_backer_profile'),
    url(r'^paynow/$',
        views.paynow,
        name='zipfelchappe_paynow'),
)
