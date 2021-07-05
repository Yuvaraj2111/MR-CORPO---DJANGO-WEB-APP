from django.urls import path

from Corp.api.views import pincode,name,compliant,ViewGovt,ViewFeedback

app_name = "Corp"

urlpatterns = [
    path("pin/", pincode, name="api_pin"),
    path("name/", name, name="api_name"),
    path("compliants/",compliant,name="compliants"),
    path("viewgovt/",ViewGovt,name="viewgovt"),
    path("feedback/",ViewFeedback,name="Api_feedback"),
]
