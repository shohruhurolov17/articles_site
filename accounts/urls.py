from django.urls import path
from .views import (SignUpView, ProfileUpdateView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]