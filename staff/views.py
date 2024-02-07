from django.shortcuts import render, redirect, get_object_or_404
from .models import StaffRegister
from doctor.models import *
from patient.models import *
from master.utils.generate_unique_id import genrate_otp
from django.core.mail import send_mail
import random
import humanize
from django.contrib import messages
from django.conf import settings
from django.utils import timezone

current_time = timezone.now()

def staff_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if 'staff_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login_view')  

    return wrapper

def login_view(request):
    print(request)
    if request.method == 'POST':
        login_id_ = request.POST['login_id']
        password_ = request.POST['password']
        try:
            print(login_id_, password_)
            get_staff = StaffRegister.objects.get(staff_id=login_id_)

        except StaffRegister.DoesNotExist:
            print("Invalid staff_id or password")
        else:
            if get_staff:
                print(password_ == get_staff.password)
                if password_ == get_staff.password:
                    request.session['staff_id'] = login_id_
                    request.session['role'] = get_staff.role.name
                    request.session['first_name'] = get_staff.first_name
                    request.session['last_name'] = get_staff.last_name
                    request.session['email'] = get_staff.email
                    request.session['mobile'] = get_staff.mobile
                    request.session['is_activated'] = get_staff.is_activated
                    return redirect('dashboard_view')
                    print("Now, you are logged in")
                else:
                    print("Your account is deactivated. Please contact to Admin.")
    return render(request, 'login.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        try:
            check_user = StaffRegister.objects.get(email=email_)
        except StaffRegister.DoesNotExist:
            print("User doesn't exist")
        else:
            if check_user:
                otp_ = genrate_otp()
                subject = "Authentication Code for [Forgot password]"
                message = f"Code for [Password Change]: {otp_}"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [f"{email_}"]
                send_mail(subject, message, from_email, recipient_list)
                check_user.otp = otp_
                check_user.save()
                context = {'email':email_}
                return render(request, 'otp-verification.html', context)
    return render(request, 'forgot-password.html')

def otp_verify_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        otp_ = request.POST['otp']
        new_password_ = request.POST['new_password']
        confirm_password_ = request.POST['confirm_password']

        try:
            check_user = StaffRegister.objects.get(email=email_)
        except StaffRegister.DoesNotExist:
            print("User doesn't exist")
        else:
            if check_user:
                if check_user.otp == otp_:
                    if new_password_ == confirm_password_:
                        check_user.password = new_password_
                        check_user.save()
                        print("Password Changed")
                        return redirect('login_view')
                    else:
                        print("New password and confirm password  doesn't match")
                        context = {'email':email_}
                        return render(request, 'otp-verification.html', context)
                else:
                    print("Invalid OTP!!!")
                    context = {'email':email_}
                    return render(request, 'otp-verification.html', context)

    return render(request, 'otp-verification.html')

def logout(request):
    request.session.clear()
    return redirect('login_view')

@staff_authenticated
def dashbord_view(request):
    return render(request, 'dashbord.html')

@staff_authenticated
def profile_view(request):
    return render(request, 'profile.html')

def get_doctor_details(doctor_id=None):
    if doctor_id is None:
        get_doctor = doctor.objects.all().order_by('-id')
    else:
        get_doctor = doctor.objects.get(id=doctor_id)
    return get_doctor


def doctors_view(request):
    context = {
        'doctors':get_doctor_details()
    }
    return render(request, 'doctor.html', context)


def get_patient_details(patient_id=None):
    if patient_id is None:
        get_patient = Patient.objects.all().order_by('-id')
    else:
        get_patient = Patient.objects.get(id=patient_id)
    return get_patient

def get_report_details(report_type_id=None):
    if report_type_id is None:
        get_report = ReportType.objects.all().order_by('-id')
    else:
        get_report = ReportType.objects.get(id=report_type_id)
    return get_report


def patients_view(request):
    today_patients = Patient.objects.filter(created_at__date=current_time.date())

    if request.method == 'POST':
        first_name_ = request.POST['firstname']
        last_name_ = request.POST['lastname']
        mobile_ = request.POST['mobile']
        doctor_id_ = request.POST['name']
        report_type_id_ = request.POST['report_type']
        address_ = request.POST['address']

        new_patient = Patient.objects.create(
            first_name=first_name_,
            last_name=last_name_,
            mobile=mobile_,
            doctor_id_id=doctor_id_,
            report_type_id = report_type_id_,
            address=address_
        )
        new_patient.save()
        print('Patient addedd')
        return redirect('patients_view')
    context = {
        'doctors':get_doctor_details(),
        'patients':get_patient_details(),
        'today_patients':today_patients,
        'current_time': current_time.date(),
    }
    return render(request, 'patients.html',context)

@staff_authenticated
def add_patients(request):
    today_patients = Patient.objects.filter(created_at__date=current_time.date())

    if request.method == 'POST':
        first_name_ = request.POST['firstname']
        last_name_ = request.POST['lastname']
        mobile_ = request.POST['mobile']
        doctor_id_ = request.POST['doctor']
        report_type_id_ = request.POST['report_type']
        address_ = request.POST['address']

        new_patient = Patient.objects.create(
            first_name=first_name_,
            last_name=last_name_,
            mobile=mobile_,
            doctor_id_id=doctor_id_,
            report_type_id = report_type_id_,
            address=address_
        )
        new_patient.save()
        print('Patient addedd')
        return redirect('patients_view')
    context = {
        'doctors':get_doctor_details(),
        'reports':get_report_details(),
        'patients':get_patient_details(),
        'today_patients':today_patients,
        'current_time': current_time.date(),
        'humanize': humanize.naturalday(current_time)

    }
    return render(request, 'add_patients.html',context)


@staff_authenticated
def patient_update(request, patient_id):
    get_patient = get_patient_details(patient_id=patient_id)
    if request.method == 'POST':
        first_name_ = request.POST['firstname']
        last_name_ = request.POST['lastname']
        mobile_ = request.POST['mobile']
        doctor_id_ = request.POST['doctor']
        report_type_id_ = request.POST['report_type']
        address_ = request.POST['address']

        get_patient.first_name = first_name_
        get_patient.last_name = last_name_
        get_patient.mobile = mobile_
        get_patient.doctor_id= doctor_id_
        get_patient.report_type = report_type_id_
        get_patient.address = address_
        get_patient.save()
        print("Patient data updated")
        return redirect('patients_view')
    

    
    context = {
        'patient':get_patient,
        'doctors':get_doctor_details(),
    }
    return render(request, 'update-patient.html', context)

@staff_authenticated
def patient_account(request, patient_id):
    get_patient = get_patient_details(patient_id=patient_id)
    payment_entries = payment_installment.objects.filter(patient_id=patient_id)

    if request.method == "POST":
        payment_installment_ = float(request.POST['payment_installment'])

        if payment_installment_ != 0:
            if payment_installment_ <= get_patient.remaining_amount:
                get_patient.paid_amount += payment_installment_
                get_patient.remaining_amount -= payment_installment_

                if get_patient.total_amount == get_patient.paid_amount:
                    get_patient.payment_status = 'Done'
                else:
                    get_patient.payment_status = 'Partially'      
                get_patient.save()

                new_payment_entry = payment_installment.objects.create(
                    patient_id_id = patient_id,
                    paid_payment = payment_installment_
                )
                new_payment_entry.save()
                print("payment added")
                return redirect('patient_account', patient_id=patient_id)
            else:
                print("Payment installment must be small than remaining amount")
                return redirect('patient_account', patient_id=patient_id)
        else:
            print("You can not add 0")
            return redirect('patient_account', patient_id=patient_id)

    context = {
        'patient':get_patient,
        'entreis':payment_entries
    }
    return render(request, 'patient-account.html', context)




@staff_authenticated
def patient_delete(request, patient_id):
    get_patient = get_patient_details(patient_id=patient_id)
    get_patient.delete()
    print('patient deleted')
    return redirect('patients_view')
