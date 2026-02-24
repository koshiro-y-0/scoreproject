from django.urls import path, reverse_lazy
from . import views
# urlsからテンプレートを指定する機能
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup-success/', views.SignUpSuccessView.as_view(), name='signup-success'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html", email_template_name="password_reset_email.html", success_url=reverse_lazy('password-reset-done')), name='password-reset-form'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html", success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name='password_reset_complete'),
]
