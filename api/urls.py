from django.urls import path
from . import views


urlpatterns = [
    path('appraisal/', views.PostApprData.as_view(), name="appraisal_data_list"),
]
