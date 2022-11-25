from django.urls import path, include
from .views import *



urlpatterns = [   

   path("list-create-department", DepartmentListView.as_view(), name='department'),
   path("delete-update-department/<pk>", DepartmentDetailView.as_view(), name='department'),

   path("list-create-subdepartment", SubDepartmentListView.as_view(), name='subdepartment'),
   path("delete-update-subdepartment/<pk>", SubDepartmentDetailView.as_view(), name='subdepartment'),

   path("list-create-report", ReportListView.as_view(), name='report'),
   path("delete-update-report/<pk>", ReportDetailView.as_view(), name='report'),

   path('list-create-subreport', SubReportListView.as_view(), name='subreport'),
    path('delete-update-subreport/<pk>', SubReportDetailView.as_view(), name='subreport'),

   path("list-create-subdepartment", SubDepartmentListCreate.as_view(), name='subdepartment'),
   path("delete-update-subdepartment/<pk>", SubDepartmentRetrieveUpdateDestroy.as_view(), name='subdepartment'),
 ]