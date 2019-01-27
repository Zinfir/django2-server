from django.urls import path, re_path

from accounts.views import login_view, logout_view, registration, account_update, profile, account_delete, verify, confirm_account


app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
    path('update/<int:pk>/', account_update, name='update'),
    path('delete/<int:pk>/', account_delete, name='delete'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', verify, name='verify' ),
    path('confirm_account/', confirm_account, name='confirm_account'),
]