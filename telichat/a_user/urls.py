from django.urls import path 
from a_user.views import *

urlpatterns = [
    path('' , profileView , name='profileView'),
    path('edit/', profileEditView, name="profile-edit"),
    path('onboarding/', profileEditView, name="profile-onboarding"),
    path('@<username>/', profileView, name='profile'),
    path('settings/', profile_settings_view, name='profile_settings'),
    path('emailchange/', profile_emailchange, name="profile-emailchange"),
    path('emailverify/', profile_emailverify, name="profile-emailverify"),
    path('delete/', profile_delete_view, name="profile-delete"),
]
