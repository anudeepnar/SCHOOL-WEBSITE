from django.urls import path
from . import views

app_name = "curriculum"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contactus, name="contact_us"),
    path('standard/', views.StandardListView.as_view(), name="standard"),
    path('standard/<slug:slug>/', views.SubjectListView.as_view(), name="subject"),#slug=standard
    path('standard/<str:standard>/<slug:slug>/', views.LessonListView.as_view(), name="lesson"),#slug=subject
    path('standard/<str:standard>/<slug:slug>/create/', views.LessonCreateView.as_view(), name="lesson_create"), #slug=subject
    path('standard/<str:standard>/<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(), name="lesson_detail"),
    path('standard/<str:standard>/<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(), name="lesson_update"),
    path('standard/<str:standard>/<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(), name="lesson_delete")

]
