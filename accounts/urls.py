from django.urls import path
from .views import SignUpView, AccountsPageView

urlpatterns = [
    path("", AccountsPageView.as_view(), name="accounts"),
    path('signup/', SignUpView.as_view(), name='signup'),
]