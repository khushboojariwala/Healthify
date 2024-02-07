from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('dashbord_view/', dashbord_view, name ='dashbord_view'),    
    path('forgot_password_view/', forgot_password_view, name='forgot_password_view'),
    path('otp_verify_view/', otp_verify_view, name='otp_verify_view'),
    path('logout/', logout, name='logout') ,

    path('dashboard_view/', dashbord_view, name='dashboard_view'),
    path('doctors_view/', doctors_view, name='doctors_view'),
    path('patients_view/', patients_view, name='patients_view'),
    path('add_patients/', add_patients, name='add_patients'),

    path('patient_delete/<int:patient_id>', patient_delete, name='patient_delete'),
    path('patient_update/<int:patient_id>', patient_update, name='patient_update'),
    path('patient_account/<int:patient_id>', patient_account, name='patient_account'),
    path('profile_view/', profile_view, name='profile_view'),
]

