__author__ = 'Administrator'

from django.urls import path
from courses.views import CourseListView, CourseDetailView

app_name = 'courses'
urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    path('detail/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),
]

