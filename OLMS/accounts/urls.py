from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='accounts.signup'),
    path('login/', views.CustomLoginView.as_view(), name='accounts.login'),
    path('logout/', views.CustomLogoutView.as_view(), name='accounts.logout'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='accounts.password_change'),
    path('', views.ProfileView.as_view(), name='accounts.profile'),
    path('edit_profile/', views.EditProfileView.as_view(), name='accounts.edit_profile'),
        path('admin/users/', views.admin_user_list, name='accounts.admin_user_list'),
    path('admin/users/<int:user_id>/', views.admin_user_profile, name='accounts.admin_user_profile'),
]