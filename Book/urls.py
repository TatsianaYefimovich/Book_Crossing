from django.urls import path
from Book.views import main_page, sign_up, register, log_in


urlpatterns = [
    path('book', main_page),
    path('sign_up', sign_up),
    path('submit', register),
    path('log_in',log_in),


]

