from django import VERSION
if VERSION < (2, 0):
    from django.conf.urls import url
else:
    from django.urls import re_path as url

from authority.views import (
    add_permission,
    delete_permission,
    approve_permission_request,
    delete_permission,
)


urlpatterns = [
    url(
        r"^permission/add/(?P<app_label>[\w\-]+)/(?P<module_name>[\w\-]+)/(?P<pk>\d+)/$",
        view=add_permission,
        name="authority-add-permission",
        kwargs={"approved": True},
    ),
    url(
        r"^permission/delete/(?P<permission_pk>\d+)/$",
        view=delete_permission,
        name="authority-delete-permission",
        kwargs={"approved": True},
    ),
    url(
        r"^request/add/(?P<app_label>[\w\-]+)/(?P<module_name>[\w\-]+)/(?P<pk>\d+)/$",
        view=add_permission,
        name="authority-add-permission-request",
        kwargs={"approved": False},
    ),
    url(
        r"^request/approve/(?P<permission_pk>\d+)/$",
        view=approve_permission_request,
        name="authority-approve-permission-request",
    ),
    url(
        r"^request/delete/(?P<permission_pk>\d+)/$",
        view=delete_permission,
        name="authority-delete-permission-request",
        kwargs={"approved": False},
    ),
]
