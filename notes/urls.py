from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, predict_age, notes_chart

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('predict-age/', predict_age, name='predict-age'),
    path('notes-chart/', notes_chart, name='notes-chart'),
]