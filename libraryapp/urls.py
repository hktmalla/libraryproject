from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', AdminLoginView.as_view(), name='adminlogin'),
    url(r'^admin-dash/$', AdminDashView.as_view(), name='admindash'),
    url(r'^admin-dash/logout/$',
        AdminLogoutView.as_view(), name='adminlogout'),
    url(r'^admin-dash/create/$',
        AdminCreateView.as_view(), name='admincreate'),
    url(r'^admin-dash/read/$',
        AdminReadView.as_view(), name='adminread'),
    url(r'^admin-dash/delete/(?P<pk>\d+)/$',
        AdminDeleteView.as_view(), name='admindelete'),
    url(r'^admin-dash/update/(?P<pk>\d+)/$',
        AdminUpdateView.as_view(), name='adminupdate'),
    url(r'^admin-dash/issues/$',
        AdminIssueListView.as_view(), name='adminstudentlist'),
    url(r'^admin-dash/category/$',
        AdminCategoryListView.as_view(), name='admincategory'),
]
