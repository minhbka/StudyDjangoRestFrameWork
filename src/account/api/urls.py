from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from account.api.views import registration_view, update_account_view, account_properties_view,ObtainAuthTokenView

app_name = 'account'

urlpatterns = [
    path('properties', account_properties_view, name='properties'),
    path('properties/update', update_account_view, name='update'),
    path('register', registration_view, name='register'),
    # path('login', obtain_auth_token, name='login'),
    path('login', ObtainAuthTokenView.as_view(), name='login'),

]