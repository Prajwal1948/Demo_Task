from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from notes.views import NoteViewSet, notes_chart, index

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/dashboard/', notes_chart, name='notes-chart'),
]