from django.urls import path
from .views import RefbookListView, RefbookElementListView, ValidateRefbookElementView

urlpatterns = [
    path('refbooks/', RefbookListView.as_view(), name='refbook-list'),
    path('refbooks/<int:pk>/elements/', RefbookElementListView.as_view(), name='refbook-element-list'),
    path('refbooks/<int:pk>/check_element/', ValidateRefbookElementView.as_view(), name='refbook-element-validate'),
]


