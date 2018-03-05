from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^login/$', AdminLoginView.as_view(), name='adminlogin'),
    url(r'^$',
        AdminHomeView.as_view(), name='adminhome'),
    url(r'^admin-dash/$',
        AdminDashView.as_view(), name='admindash'),
    url(r'^admin-dash/logout/$',
        AdminLogoutView.as_view(), name='adminlogout'),
    url(r'^admin-dash/create/$',
        AdminCreateView.as_view(), name='admincreate'),
    url(r'^admin-dash/read/$',
        AdminReadView.as_view(), name='adminread'),
    url(r'^admin-dash/student/delete/(?P<pk>\d+)/$',
        AdminDeleteView.as_view(), name='admindelete'),
    url(r'^admin-dash/student/update/(?P<pk>\d+)/$',
        AdminUpdateView.as_view(), name='adminupdate'),
    url(r'^admin-dash/issues/$',
        AdminIssueListView.as_view(), name='adminstudentlist'),
    # book url
    url(r'^admin-dash/book/$',
        AdminBookView.as_view(), name="adminbooklist"),
    url(r'^admin-dash/bookadd/$',
        AdminAddBookView.as_view(), name='adminaddbook'),
    url(r'^admin-dash/book/delete/(?P<pk>\d+)/$',
        AdminBookDeleteView.as_view(), name="adminbookdelete"),
    url(r'^admin-dash/book/update/(?P<pk>\d+)/$',
        AdminBookUpdateView.as_view(), name="adminbookupdate"),

    # book isssue url
    url(r'^admin-dash/issues/$',
        AdminIssueListView.as_view(), name='adminstudentlist'),
    url('^admin-dash/issue/$',
        AdminIssueCreateView.as_view(), name="adminissue"),
    url('^admin-dash/issue-read/$',
        AdminIssueListView.as_view(), name="adminissuelist"),
]
