from django.urls import path

from webapp import views

urlpatterns = [
 path('user-registration',views.UserRegistrationView.as_view(),name='user_registration'),
 path('employee-update',views.EmployeeUpdateView.as_view(),name='employee-update'),

]
