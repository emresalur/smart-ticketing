from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^index$", index, name="index"),
    url(r"^faq$", faq, name="faq"),
    url(r"^requests$", jrequests, name="jrequests"),
    url(r"^myrequests$", myrequests, name="myrequests"),
    url(r"^teacher$", teacher, name="teacher"),
    url(r"^solved$", solved, name="solved"),
    url(r"^detail$", detail, name="detail"),
    url(r"^go_active$", go_active, name="go_active"),
    url(r"^active$", active, name="active"),
    url(r"^share$", share, name="share"),

    url(r"^admin_detail$", admin_detail, name="admin_detail"),
]
