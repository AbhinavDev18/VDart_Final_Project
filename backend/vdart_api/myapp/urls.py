from django.urls import path
from . import views

urlpatterns = [
    path('emails/', views.fetch_emails, name='fetch_emails'),
    path('send-mail/<str:email>/', views.send_mail, name='send_mail'),
    path('submit-form/<str:email>/<str:token>/', views.submit_form, name='submit_form'),
]
