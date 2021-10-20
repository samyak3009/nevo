from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    path('account/', views.AccountList.as_view()),
    path('account/<int:id>/', views.AccountDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)