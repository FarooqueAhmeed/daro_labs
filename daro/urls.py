from django.urls import path
from daro.views import *

app_name = 'daro'

urlpatterns = [

    path('',index, name='index'),
    path('about',about, name='about'),
    path('investment_plan_01',investment_plan_01, name='investment_plan_01'),
    path('investment_plan_02',investment_plan_02, name='investment_plan_02'),
    path('investment_plan_03',investment_plan_03, name='investment_plan_03'),
    path('user_dashboard',user_dashboard, name='user_dashboard'),
    path('investor',investor, name='investor'),
    path('affiliate',affiliate, name='affiliate'),
    path('mission_vision',mission_vision, name='mission_vision'),
    path('privacy_policy',privacy_policy, name='privacy_policy'),
    path('terms_of_service',terms_of_service, name='terms_of_service'),
    path('refund_policy',refund_policy, name='refund_policy'),
    path('faq',faq, name='faq'),
    path('error_404', error_404, name='error_404'),
    path('login', login, name='login'),
    path('sign_up', sign_up, name='sign_up'),
    path('blog', blog, name='blog'),
    path('blog_details', blog_details, name='blog_details'),
    path('contact', contact, name='contact'),
]