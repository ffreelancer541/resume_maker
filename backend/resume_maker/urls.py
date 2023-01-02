from django.urls import path
from .views import *
urlpatterns = [
    path('register/' , ResgisterView.as_view() , name='user-register'),
    # path('otp/', OtpView.as_view() , name='user-otp'),
    path('login/' , LoginView.as_view() , name='user-login'),
    path('resume_post/' , ResumePOST.as_view() , name='resume-post'),
    path('resume_templates/' , ResumeTemplateView.as_view() , name='resume-templates'),
]
